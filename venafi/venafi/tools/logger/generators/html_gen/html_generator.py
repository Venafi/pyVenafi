from typing import List, Dict, Optional, Tuple
import os
import shutil
import re
import uuid
from pathlib import Path
from datetime import datetime
from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters.html import HtmlFormatter
import asyncio
import htmlmin
from venafi.tools.logger.sqlite.dal import LoggerSql, SelectResult
from venafi.tools.logger.generators.bases import Generator, GeneratorType
from venafi.tools.logger.config import LogTag

CSS_RESOURCE = os.path.abspath(f'{os.path.dirname(__file__)}/styles.css')
JS_RESOURCE = os.path.abspath(f'{os.path.dirname(__file__)}/actions.js')


class HtmlLogGenerator(Generator):
    def __init__(self):
        super().__init__(GeneratorType.html)
        self._sql = None  # type: Optional[LoggerSql]

    def generate(self, log_file: str, title: str = None, include_code: bool = True,
                 datetime_range: Tuple[datetime, datetime] = None, exclude_files: List[str] = None):
        asyncio.run(self._generate(log_file=log_file, title=title, include_code=include_code,
                                   datetime_range=datetime_range, exclude_files=exclude_files))

    async def _generate(self, log_file: str, title: str, include_code: bool,
                        datetime_range: Tuple[Optional[datetime], Optional[datetime]],
                        exclude_files: List[str]):
        # region Get Content Of Log File
        log_file = Path(log_file)
        self._sql = LoggerSql(log_file)
        # endregion Get Content Of Log File

        # region Create HTML File
        log_tags = self._sql.select(
            query=f'select * from {self._sql.log_tags.table_name}'
        )
        log_tags = self._get_log_tags(log_tags=log_tags)

        log_entries_query = f'select * from {self._sql.log_entries.table_name}'
        if isinstance(datetime_range, (tuple, list)):
            if not len(datetime_range) == 2:
                raise ValueError(f'Datetime range must be a Tuple object of size 2 where the first '
                                 f'element, a datetime object, represents the "from" date and the '
                                 f'second, also a datetime object, represents the "to" date. To omit '
                                 f'one or the other, set the value to None.')
            dt_fmt = lambda x: x.strftime('%Y-%m-%d %H:%M:%S')
            if start := datetime_range[0]:
                if end := datetime_range[1]:
                    log_entries_query += f" where timestamp between '{dt_fmt(start)}' and '{dt_fmt(end)}'"
                else:
                    log_entries_query += f" where timestamp >= '{dt_fmt(start)}'"
            elif end := datetime_range[1]:
                log_entries_query += f" where timestamp <= '{dt_fmt(end)}'"
        log_entries = self._sql.select(query=log_entries_query)

        title = title or 'Log Results'
        code_blocks = self._get_code_blocks(log_entries=log_entries,
                                            exclude_files=exclude_files) if include_code else None
        html = htmlmin.minify(f"""
        <html>
            <head>
                <title>{title}</title>
                <link rel="stylesheet" type="text/css" href="./{Path(CSS_RESOURCE).stem}.css" />
                <script type="text/javascript" src="./{Path(JS_RESOURCE).stem}.js"></script>
                <style>
                    {await self._get_styles(log_tags=log_tags, include_code=include_code)}
                </style>
            </head>
            <body>
                <!-- Title -->
                <div id="title">
                    <h1>{title.upper()}</h1>
                </div>
                <!-- Legend -->
                <div id="legend">
                    {await self._legend(log_tags=log_tags)}
                </div>
                <!-- Code Blocks -->
                <div class="hide" id="code-blocks">
                    {''.join([cb['block'] for cb in code_blocks.values()]) if code_blocks else ''}
                </div>
                <!-- Log Entries -->
                <div id="log-entries">
                    {await self._get_log_entries(log_tags=log_tags, log_entries=log_entries,
                                                 code_blocks=code_blocks if include_code else None)}
                </div>
            </body>
            {'<br/>' * 12}
        </html>
        """, remove_comments=True, remove_empty_space=True)
        # endregion Create HTML File

        # region Send Files To Log Directory
        resources = f'{log_file.parent}'
        file_path = ''
        for part in resources.split(os.sep):
            file_path += part + os.sep
            if not os.path.exists(file_path):
                os.mkdir(file_path)

        if code_blocks:
            for values in code_blocks.values():
                with open(f"{resources}/{values['path']}", 'w') as f:
                    f.write(values['code'])

        shutil.copy(
            src=CSS_RESOURCE,
            dst=resources
        )
        shutil.copy(
            src=JS_RESOURCE,
            dst=resources
        )
        with open(f'{log_file.parent}/{log_file.stem}.html', 'w') as f:
            f.write(html)
        # endregion Send Files To Log Directory

    def _get_log_tag_from_dict(self, tag: SelectResult):
        tag = tag.dict
        return LogTag(
            name=tag[self._sql.log_tags.name],
            value=tag[self._sql.log_tags.value],
            html_color=tag[self._sql.log_tags.color]
        )

    def _get_log_tags(self, log_tags: SelectResult):
        return {
            tag[self._sql.log_tags.name]: LogTag(
                name=tag[self._sql.log_tags.name],
                value=tag[self._sql.log_tags.value],
                html_color=tag[self._sql.log_tags.color]
            )
            for tag in log_tags.iterate()
        }

    @staticmethod
    async def _get_styles(log_tags: Dict[str, LogTag], include_code: bool):
        colors = []
        classes = []
        for ll in log_tags.values():
            colors.append(f'--{ll.alias}: {ll.html_color};')
            classes.append(f"""
            .{ll.alias} {{
                border-left: var(--{ll.alias}) solid 5px;
                border-bottom: lightgrey solid 2px;
                transition: border-bottom 0.2s ease-in-out;
            }}

            .{ll.alias}:hover {{
                border-bottom: var(--{ll.alias}) solid 2px;

            }}
            """)
        colors = '\n\t'.join(colors)
        classes = '\n'.join(classes)
        return f"""
        :root {{
            {colors}
            --log-entry-btns: {3 if include_code else 2}
        }}

        {classes}
        """

    @staticmethod
    async def _legend(log_tags: Dict[str, LogTag]):
        def add_filter(log_tag: LogTag):
            return f"""
            <div class="log-tag fancy-checkbox" 
                 aria-label="{log_tag.alias}" 
                 aria-valuetext="{log_tag.value}"
                 onclick="handleLogTagFilter(this)">
                <label class="switch">
                    <input id="{log_tag.alias}" type="checkbox" checked>
                    <span 
                        class="slider round" 
                        style="background-color: {log_tag.html_color}; box-shadow: 0 0 10px {log_tag.html_color};">
                    </span>
                </label>
                <span>{log_tag.name}</span>
            </div>
            """

        filters = '\n'.join([
            add_filter(log_tag=log_tag)
            for log_tag in log_tags.values()
        ])
        return f"""
        <div id="filters-container">
            <div id="filters-controls">
                <button id="filters-btn" class="btn" onclick="handleShowFilter(this)">Hide Filters</button>
            </div>
            <div id="filters-wrapper">
                <div id="filters" class="decompressed">
                    <div id="log-tags">
                        {filters}
                    </div>
                    <div class="divider"></div>
                    <div id="search-container">
                        <div id="search-params">
                            <div class="search-param fancy-checkbox">
                                <label class="switch">
                                    <input id="search-in-msg" type="checkbox" checked>
                                    <span class="slider round"></span>
                                </label>
                                <span>Include Message Blocks</span>
                            </div>
                            <div class="search-param fancy-checkbox">
                                <label class="switch">
                                    <input id="search-in-info" type="checkbox">
                                    <span class="slider round"></span>
                                </label>
                                <span>Include Info Blocks</span>
                            </div>
                            <div></div>
                            <div class="search-param fancy-checkbox">
                                <label class="switch">
                                    <input id="search-whole-word" type="checkbox">
                                    <span class="slider round"></span>
                                </label>
                                <span>Whole Word Only</span>
                            </div>
                            <div class="search-param fancy-checkbox">
                                <label class="switch">
                                    <input id="search-regex" type="checkbox">
                                    <span class="slider round"></span>
                                </label>
                                <span>Use Regular Expression</span>
                            </div>
                            <div class="search-param fancy-checkbox">
                                <label class="switch">
                                    <input id="search-match-case" type="checkbox">
                                    <span class="slider round"></span>
                                </label>
                                <span>Match Case</span>
                            </div>
                        </div>
                        <div id="search-controls">
                            <input id="search" type="text" placeholder="Search for text..." onkeyup="searchOnEnter(event, this.id)">
                            <button id="go-btn" class="btn" onclick="search('search')">Go</button>
                        </div>
                        <div id="search-count"></div>
                    </div>
                </div>
            </div>
        </div>
        """

    def _get_code_blocks(self, log_entries: SelectResult, exclude_files: List[str] = None):
        exclude_files = exclude_files or []
        cols = self._sql.log_entries
        codes = {}  # type: Dict
        fc = 0
        if exclude_files:
            exclude_regexes = "(" + ")|(".join(exclude_files) + ")"
        else:
            exclude_regexes = None
        for le in list(log_entries.iterate()):
            fp = le[cols.file_path]
            if fp not in codes.keys():
                if exclude_regexes and re.match(pattern=exclude_regexes, string=fp, flags=re.IGNORECASE):
                    continue
                with open(fp, 'r') as f:
                    code = f.read()
                code_html = highlight(
                    code=code,
                    lexer=PythonLexer(),
                    formatter=HtmlFormatter(linenos='inline')
                )
                fc += 1
                file_id = f"file-id-{fc}"
                code = htmlmin.minify(f"""
                <html>
                    <head>
                        <link rel=stylesheet type=text/css href=styles.css>
                        <script>
                            window.addEventListener("message", function(event) {{
                                console.log(event);
                                line_num =
                                Number(event.data);
                                view_line = line_num > 2 ? line_num - 3 : 0;
                                linenos = document.querySelectorAll('.lineno');
                                if(linenos.length > 0) {{
                                    linenos.forEach(line => {{line.style.backgroundColor = 'transparent';}})
                                    linenos[line_num - 1].style.backgroundColor = 'lightgreen';
                                    body = document.querySelector('body');
                                    body.scrollTo({{top: linenos[view_line].offsetTop, behavior: 'smooth'}});
                                }}
                            }})
                        </script>
                    </head>
                    <body>
                        {code_html}
                    </body>
                </html>
                """, remove_empty_space=True)
                path = f'{uuid.uuid3(uuid.NAMESPACE_OID, fp).hex}.html'
                codes[fp] = {
                    'id'   : file_id,
                    'path' : path,
                    'block': f'''
                        <div class="code-block hide" id="{file_id}" aria-label="{Path(fp).stem}.html">
                            <div class="code-block-controls">
                                <span class="filepath" title="{le[cols.file_path]}">{le[cols.file_path]}</span>
                                <button class="close-code" onclick="hideCode('{file_id}')">X</button>
                            </div>
                            <div>
                                <iframe class="code" src="./{path}" type="text/html"></iframe>
                            </div>
                        </div>
                    ''',
                    'code' : code
                }
        return codes

    async def _get_log_entries(self, log_tags: Dict[str, LogTag], log_entries: SelectResult,
                               code_blocks: Dict[str, Dict[str, str]]):
        cols = self._sql.log_entries

        file_names = []

        def format_info_block(le: dict):
            return f'File: {le[cols.file_path]}\n' \
                   f'Line Number: {le[cols.line_num]}\n' \
                   f'Qualified Name: {le[cols.function_name]}\n' \
                   f'Thread Id: {le[cols.thread_id]}\n' \
                   f'Thread Name: {le[cols.thread_name]}\n' \
                   f'Timestamp: {le[cols.timestamp]}\n' \
                   f'Log Tag: {le[cols.tag_name]}'

        logs = [
            f"""
            <div id="log-entries-controls">
                <div class="btn">
                    <button id="reset-btn" onclick="resetLogBlocks()">Reset</button>
                </div>
            </div>
            """
        ]

        def organize(les: List[dict]):
            results = []
            threads = {}  # type: Dict[str, Tuple[int, List[Dict]]]
            main_counter = 0
            for le in les:
                if bool(le[cols.is_main_thread]):
                    results.append(le)
                    main_counter += 1
                else:
                    if (thread_id := le[cols.thread_id]) not in threads.keys():
                        threads[thread_id] = (main_counter, [le])
                    else:
                        threads[thread_id][1].append(le)
            for thread_id, value in threads.items():
                index, entries = value
                original = results.copy()
                new = original[:index]
                new.extend(entries)
                new.extend(original[index:])
                results = new

            return results

        log_entries = organize(les=list(log_entries.iterate()).copy())

        for e, log_entry in enumerate(log_entries):
            log_tag = log_tags[log_entry[cols.tag_name]]
            log_entry_id = f'log-entry-{e}'
            msg_block_id = f'msg-block-{e}'
            code_block_id = f'code-block-{e}'
            info_block_id = f'info-block-{e}'
            log_group_id = f'log-group-{e}'

            display = "hide" if log_entry[cols.depth] > 0 else "show"
            if e < (len(log_entries) - 1) and \
                    log_entries[e + 1][cols.depth] > log_entry[cols.depth]:
                expand_btn = f"""
                <div class="btn item-container">
                    <button class="exp-btn hide-logs" onclick="toggleExpLogs('{log_entry_id}')"></button>
                </div>
                """
            else:
                expand_btn = f"""
                <div class="item-container">
                    <div class="no-exp">-</div>
                </div>
                """
            if code_blocks:
                code_block = code_blocks.get(log_entry[cols.file_path])
                fid, fp = code_block.get('id'), code_block.get('path')
                code_btn = f'''
                    <div class="code-btn btn item-container">
                        <button onclick="showCode('{fid}', '{fp}', {log_entry[cols.line_num]})">Code</button>
                    </div>
                '''
            else:
                code_btn = ''
            func_def = f'{log_entry[cols.function_name]}:{log_entry[cols.line_num]}'
            logs.append(f"""
            <div id='{log_entry_id}' 
                 class="log-entry {display}"
                 aria-valuetext="{log_tag.alias}" 
                 aria-label="{log_entry[cols.depth]}">
                <div class="log-row {log_tag.alias}" style="margin-left: {log_entry[cols.depth] * 25}px;">
                    {expand_btn}
                    <div class="func item-container">
                        <span title="{func_def}">{func_def}</span>
                    </div>
                    <div class="preview item-container">
                        <span>{log_entry[cols.msg]}</span>
                    </div>
                    <div class="msg-btn btn item-container">
                        <button onclick="handleLogContent(this, '{msg_block_id}')">Message</button>
                    </div>
                    <div class="info-btn btn item-container">
                        <button onclick="handleLogContent(this, '{info_block_id}')">Info</button>
                    </div>
                    {code_btn}
                </div>
                <div 
                    class="log-block-container" 
                    style="border-left: var(--{log_tag.alias}) solid 5px; margin-left: {log_entry[cols.depth] * 25}px;"
                >
                    <div id="info-block-{e}" class="info-block log-block hide">
                        <pre>{format_info_block(log_entry)}</pre>
                    </div>
                    <div id="msg-block-{e}" class="msg-block log-block hide">
                        <pre>{log_entry[cols.msg]}</pre>
                    </div>
                </div>
            </div>
            """)
            e += 1
        return ''.join(logs)


if __name__ == '__main__':
    import time

    start = time.time()
    html = HtmlLogGenerator()
    html.generate('/Users/tyler.spens/PycharmProjects/spitest/logs/dev/log_20200507135041090761.db')
    print(time.time() - start)
