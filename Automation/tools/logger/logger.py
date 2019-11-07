import os
import sys
import traceback
import inspect
from config.settings import LOG_LEVEL
from log_resources import LogColors, LogLevels
from config.settings import LOG_TIMESTAMP, LOG_TO_JSON, OPEN_HTML_ON_FINISH
import webbrowser
import json


LOG_DIR = '%s/logs' % os.path.split(__file__)[0]
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

LOG_FILE_WITHOUT_EXT = '%s/logfile_%s' % (LOG_DIR, LOG_TIMESTAMP)

class Logger:
    def __init__(self, level):
        self._log_to_console_method = (lambda *args, **kwargs: None) if level < LOG_LEVEL else self._log_to_console
        self.level = level
        self.text_color = 0

    def log(self, msg, critical=False):
        frame = inspect.currentframe()
        outerframes = inspect.getouterframes(frame)[1]
        self._log(msg=msg, outerframes=outerframes, critical=critical)

    def log_exception(self, skip_console=True):
        """
        :type exc_obj: Exception
        """
        tb = sys.exc_traceback
        while True:
            if tb.tb_next is None:
                break
            tb = tb.tb_next
        frame = tb.tb_frame
        outerframes = inspect.getouterframes(frame)[0]
        msg = traceback.format_exc()
        html_msg = '<span style="white-space: pre-wrap; color: red">%s</span>' % msg
        self._log(msg=msg, outerframes=outerframes, critical=True, skip_console=skip_console, html_formatted_msg=html_msg)

    def _log(self, msg, outerframes, critical=False, skip_console=False, html_formatted_msg=None):
        path, lineno = outerframes[1], str(outerframes[2])
        filepath, filename = os.path.split(path)
        source, startlineno = inspect.getsourcelines(outerframes[0])
        if not skip_console:
            self._log_to_console_method(filename=path, lineno=lineno, msg=msg, critical=critical)
        if LOG_TO_JSON is True:
            json_msg = html_formatted_msg or msg
            source = ''.join(['%s:\t%s' % (x + startlineno, y) for x, y in enumerate(source)])
            self._log_to_json(path=filepath, filename=filename, lineno=lineno, msg=json_msg, source=''.join(source), critical=critical)

    def _log_to_console(self, filename, lineno, msg, critical):
        level = LogLevels.critical if critical else self.level
        file_text_color = LogColors.level_color.get(level)
        file_text = '{c}File "{f}", line {l}{e}'.format(c=file_text_color, f=filename, l=lineno, e=LogColors.end)
        print(file_text + str(msg))

    def _log_to_json(self, path, filename, lineno, msg, source, critical):
        level = LogLevels.critical if critical else self.level
        with open('%s.json' % LOG_FILE_WITHOUT_EXT, 'a+') as f:
            json.dump({"path": path, "filename": filename, "lineno": lineno, "text": str(msg), "source": source, "log_level": level}, f)
            f.write('\n')


def log_to_html():
    json_file = "%s.json" % LOG_FILE_WITHOUT_EXT
    if not os.path.exists(json_file):
        print("Cannot open %s because it does not exist." % json_file)
        return

    log_item_counter = 0
    json_output = []
    with open(json_file, 'r') as f:
        for line in f.readlines():
            json_output.append(dict(json.loads(line)))

    if not isinstance(json_output, list):
        json_output = [json_output]

    file_text_colors = {
        LogLevels.api: 'palegoldenrod',
        LogLevels.feature: 'lightcyan',
        LogLevels.test: 'hotpink',
        LogLevels.critical: 'red'
    }

    legend = ''
    for level, value in sorted(LogLevels.__dict__.items()):
        legend_item_color = file_text_colors.get(value)
        if not legend_item_color:
            continue
        legend += """
        <div class='legend-item'>    
            <label class='checkbox-label'>
                <input id='log-level-{level}-cb' type='checkbox' checked onchange='filterLogLevel(this.id, {value})'>
                <span class='checkbox-custom rectangular'></span>
            </label>
            <div class='input-title' style='background-color: {color}; cursor: default'>{level}</div>
        </div>    
        """.format(level=level, value=value, color=legend_item_color)

    rows = ''
    for output in json_output:
        file_text_color = file_text_colors.get(output['log_level'], 'orange')
        rows += """
        <div class='log-item-container log-level-{log_level}'>
            <div id='log-{counter}' class='log-item-row-1'>
                <span id='exp-{counter}' class='log-item exp' onClick=togglePlusMinus({counter})>+</span>
                <span class='log-item line-info' style='background-color: {ftc};'>{filename}: {lineno}</span>
                <span id='log-text-{counter}' class='log-item log-text' style='white-space: nowrap'>{text}</span>
            </div>
            <div id='source-{counter}' class='log-item-row-2' style='display: none'>
                <span class='source-code'>{source}</span>
            </div>
        </div>
        """.format(counter=str(log_item_counter), path=output['path'], filename=output['filename'], lineno=output['lineno'],
                   text=output['text'], source=output['source'], ftc=file_text_color, log_level=output['log_level'])
        log_item_counter += 1

    f = open('%s.html' % LOG_FILE_WITHOUT_EXT, 'w')

    message = """
    <html>
        <head>
            <script>
                function togglePlusMinus(counter) {{
                    exp_el = document.getElementById('exp-'+counter);
                    text = document.getElementById('log-text-'+counter);
                    source = document.getElementById('source-'+counter);
                    log = document.getElementById('log-'+counter);
                    sign = exp_el.innerHTML;
                    if(sign === '+') {{
                        text.style.whiteSpace = 'unset';
                        text.style.overflowWrap = 'break-word';
                        text.style.wordWrap = 'break-word';
                        source.style.display = 'flex';
                        log.style.borderRadius = '5px 5px 0px 0px';
                        exp_el.innerHTML = '-';
                        exp_el.style.background = 'linear-gradient(-45deg, #07D, transparent)';
                    }}
                    else {{
                        text.style.whiteSpace = 'nowrap';
                        text.style.overflowWrap = 'unset';
                        text.style.wordWrap = 'unset';
                        source.style.display = 'none';
                        log.style.borderRadius = '5px';
                        exp_el.innerHTML = '+';
                        exp_el.style.background = 'none';
                    }}                    
                }}
                
                function filterLogLevel(id, level) {{
                    checkbox = document.getElementById(id);
                    logs = document.querySelectorAll('.log-level-' + level);
                    display = checkbox.checked ? 'block' : 'none';
                    for(var i=0; i < logs.length; i++) {{
                        logs[i].style.display = display;
                    }} 
                }}
            </script>
            <style>
                #page-title {{
                    color: grey;
                    text-align: center;
                }}


                #log-container {{
                    width: 90%;
                    margin: 0 auto;
                    font-size: medium;
                    font-family: cursive;
                }}

                .log-item-row-1 {{
                    height: auto;
                    display: flex;
                    border: solid lightgrey 2px;
                    border-radius: 5px;
                    margin: 2px 2px 0px 2px;
                }}

                .log-item-row-2 {{
                    margin: 0px 2px 0px 2px;
                    white-space: pre-wrap;
                    font-family: cursive;
                    display: flex;
                    justify-content: center;
                    border: solid lightgrey;
                    border-width: 0px 2px 2px 2px;
                    border-radius: 0px 0px 5px 5px;
                    background-color: whitesmoke;
                    padding: 30px;
                    max-height: 500px;
                    overflow: auto;
                }}

                .log-item {{
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                }}

                .exp {{
                    min-width: 40px !important;
                    border-right: solid lightgrey 2px;
                    text-align: center;
                    cursor: pointer;
                }}

                .line-info {{
                    text-align: center;
                    padding-left: 10px;
                    padding-right: 10px;
                    border-right: solid lightgrey 2px;
                    min-width: 200px !important;
                }}

                .log-text {{
                    padding-left: 10px;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    display: inline-block;
                }}

                .source-code {{
                    width: 100%;
                }}
                
                /* Styling Checkbox Starts */
                #legend-title {{
                    text-align: center;
                    width: 100%;
                    margin: auto;
                    margin-bottom: 10px;
                    color: #444;
                }}
            
                #legend-container {{
                    width: 90%;
                    margin: 0 auto;
                }}
                
                #legend {{
                    border-radius: 5px;
                    display: flex;
                    flex-wrap: wrap;
                    position: relative;
                    justify-content: space-evenly;
                    width: 300px;
                    margin: 30px auto;
                    border: solid lightgrey 2px;
                    padding: 10px;
                    background-color: mediumaquamarine;
                }}
                
                .legend-item {{
                    height: 45px;
                    width: 120px;
                    display: block;
                }}
                
                .input-title {{
                    display: inline-block;
                    width: 50%;
                    text-align: center;
                    margin-left: 6px;
                    font-size: medium; 
                    font-family: cursive; 
                }}
                
                .checkbox-label {{
                    display: inline-block;
                    position: relative;
                    cursor: pointer;
                    height: 24px;
                    width: 24px;
                    clear: both;
                    top: 4px;
                }}
                
                .checkbox-label input {{
                    position: absolute;
                    opacity: 0;
                    cursor: pointer;
                }}
                
                .checkbox-label .checkbox-custom {{
                    position: absolute;
                    top: 0px;
                    left: 0px;
                    height: 24px;
                    width: 24px;
                    background-color: transparent;
                    border-radius: 5px;
                    transition: all 0.3s ease-out;
                    -webkit-transition: all 0.3s ease-out;
                    -moz-transition: all 0.3s ease-out;
                    -ms-transition: all 0.3s ease-out;
                    -o-transition: all 0.3s ease-out;
                    border: 2px solid #888;
                }}
                
                
                .checkbox-label input:checked ~ .checkbox-custom {{
                    background-color: #FFFFFF;
                    border-radius: 5px;
                    -webkit-transform: rotate(0deg) scale(1);
                    -ms-transform: rotate(0deg) scale(1);
                    transform: rotate(0deg) scale(1);
                    opacity:1;
                    border: 2px solid #888;
                }}
                
                
                .checkbox-label .checkbox-custom::after {{
                    position: absolute;
                    content: '';
                    left: 12px;
                    top: 12px;
                    height: 0px;
                    width: 0px;
                    border-radius: 5px;
                    border: solid #009BFF;
                    border-width: 0 3px 3px 0;
                    -webkit-transform: rotate(0deg) scale(0);
                    -ms-transform: rotate(0deg) scale(0);
                    transform: rotate(0deg) scale(0);
                    opacity:1;
                    transition: all 0.3s ease-out;
                    -webkit-transition: all 0.3s ease-out;
                    -moz-transition: all 0.3s ease-out;
                    -ms-transition: all 0.3s ease-out;
                    -o-transition: all 0.3s ease-out;
                }}
                
                
                .checkbox-label input:checked ~ .checkbox-custom::after {{
                  -webkit-transform: rotate(45deg) scale(1);
                  -ms-transform: rotate(45deg) scale(1);
                  transform: rotate(45deg) scale(1);
                  opacity:1;
                  left: 8px;
                  top: 3px;
                  width: 6px;
                  height: 12px;
                  border: solid #009BFF;
                  border-width: 0 2px 2px 0;
                  background-color: transparent;
                  border-radius: 0;
                }}
                
                
                
                /* For Ripple Effect */
                .checkbox-label .checkbox-custom::before {{
                    position: absolute;
                    content: '';
                    left: 10px;
                    top: 10px;
                    width: 0px;
                    height: 0px;
                    border-radius: 5px;
                    border: 2px solid #888;
                    -webkit-transform: scale(0);
                    -ms-transform: scale(0);
                    transform: scale(0);    
                }}
                
                .checkbox-label input:checked ~ .checkbox-custom::before {{
                    left: -3px;
                    top: -3px;
                    width: 24px;
                    height: 24px;
                    border-radius: 5px;
                    -webkit-transform: scale(3);
                    -ms-transform: scale(3);
                    transform: scale(3);
                    opacity:0;
                    z-index: 999;
                    transition: all 0.3s ease-out;
                    -webkit-transition: all 0.3s ease-out;
                    -moz-transition: all 0.3s ease-out;
                    -ms-transition: all 0.3s ease-out;
                    -o-transition: all 0.3s ease-out;
                }}

            </style>
            <title>Testing Log</title>
        </head>
        <body>
            <h1 id='page-title'>TESTING LOG</h1>
            <div id='legend-container'>
                <div id='legend'>
                    <h3 id='legend-title'>Log Filter</h3>
                    {legend}
                </div>
            </div>
            <div id='log-container'>
                {rows}
            </div>
        </body>
    </html>
    """.format(legend=legend, rows=rows)

    f.write(message)
    f.close()

    if OPEN_HTML_ON_FINISH is True:
        webbrowser.open_new_tab('%s.html' % LOG_FILE_WITHOUT_EXT)