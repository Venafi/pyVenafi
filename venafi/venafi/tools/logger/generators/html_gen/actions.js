RegExp.escape = function(string) {
  return string.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&')
};

function toggleCompression(el, compress=null) {
    if(compress !== null) {
        if(compress === true) {
            el.classList.replace('decompressed', 'compressed');
        } else {
            el.classList.replace('compressed', 'decompressed');
        }
    } else {
        el.classList.toggle('compressed');
        el.classList.toggle('decompressed');
    }
}

function toggleShowHide(el, hide=null) {
   if(hide !== null) {
       if(hide === true) {
           el.classList.replace('show', 'hide');
       } else {
           el.classList.replace('hide', 'show');
       }
   } else {
       el.classList.toggle('hide');
       el.classList.toggle('show');
   }
}

function handleShowFilter(filters_btn) {
    filters = document.getElementById('filters');
    toggleCompression(filters);
    filters_btn.textContent = filters.classList.contains('decompressed') ? "Hide Filters" : "Show Filters";
}

function search(el, event) {
    if(event.key === 'Enter') {
        console.log('Searching...')
    }
    return;
}

/* Log Content Handles */
function expandLogs(log_entry) {
    log_entry.classList.add('expanded');
    exp_btn = log_entry.querySelector('.exp-btn');
    exp_btn.classList.replace('hide-logs', 'show-logs');
    depth = log_entry.getAttribute('aria-label');
    for(var i=log_entry.nextElementSibling; i!==null; i=i.nextElementSibling) {
        if(Number(i.getAttribute('aria-label')) == (Number(depth) + 1)) {
            toggleShowHide(i, hide=false);
        }
        else if (Number(i.getAttribute('aria-label')) > (Number(depth) + 1)) {
            continue;
        }
        else {
            break;
        }
    }
}

function collapseLogs(log_entry) {
    log_entry.classList.remove('expanded');
    exp_btn = log_entry.querySelector('.exp-btn');
    if(exp_btn) {
        exp_btn.classList.replace('show-logs', 'hide-logs');
    }
    depth = log_entry.getAttribute('aria-label');
    for(var i=log_entry.nextElementSibling; i!==null; i=i.nextElementSibling) {
        if(depth < i.getAttribute('aria-label')) {
            toggleShowHide(i, hide=true);
            exp_btn = i.querySelector('.exp-btn');
            if(exp_btn) {
                exp_btn.classList.replace('show-logs', 'hide-logs');
            }
        }
        else {
            break;
        }
    }
}

function toggleExpLogs(log_entry_id) {
    log_entry = document.getElementById(log_entry_id);
    if(!log_entry_id) {
        return;
    }
    if(log_entry.classList.contains('expanded')) {
        collapseLogs(log_entry);
    }
    else {
        expandLogs(log_entry);
    }
}

function handleLogContent(btn, block_id, hide=null) {
    block = document.getElementById(block_id);
    toggleShowHide(block, hide);
    if(hide === true) {
        btn.classList.remove('bold');
    } else if(hide === false) {
        btn.classList.add('bold');
    } else {
        btn.classList.toggle('bold');
    }
}

// Handle Code Blocks
function showCode(file_id, file_name, line_num) {
    code_blocks = document.querySelector('#code-blocks');
    code_blocks.classList.replace('hide', 'show');
    code_block = document.querySelector('#'+file_id);
    code_block.classList.replace('hide', 'show');
    code = code_block.querySelector('.code');
    code_blocks.scrollTo({top: code.offsetTop, behavior: 'smooth'});
    code.contentWindow.postMessage(line_num.toString(), "*");
}

function hideCode(file_id) {
    code_block = document.querySelector('#'+file_id);
    code_block.classList.replace('show', 'hide');
    code = code_block.querySelector('.code');
    code.innerHTML = "";
    code_blocks = document.querySelector('#code-blocks');
    if(code_blocks.querySelectorAll('.show').length <= 0) {
        code_blocks.classList.replace('show', 'hide');
    }
}

// Search
function resetLogBlocks() {
    blocks = document.querySelectorAll('.log-block');
    blocks.forEach((block) => {
        log_entry = block.parentElement.parentElement;
        if(block.classList.contains('info-block')) {
            btn = log_entry.querySelector('.info-btn > button');
        } else if(block.classList.contains('msg-block')) {
            btn = log_entry.querySelector('.msg-btn > button');
        } else if(block.classList.contains('code-block')) {
            btn = log_entry.querySelector('.code-btn > button');
        }
        handleLogContent(btn, block.id, compress=true);
        block.firstElementChild.style.backgroundColor = 'transparent';
    })

    log_entries = document.querySelectorAll('.log-entry');
    log_entries.forEach((log_entry) => {
        exp_btn = log_entry.querySelector('.exp-btn');
        if(exp_btn) {
            exp_btn.classList.replace('show-logs', 'hide-logs');
            collapseLogs(log_entry);
        }
    })
    search_results = document.querySelector('#search-count');
    search_results.innerHTML = '';
}

function searchRegex(text) {
    var wwo = document.querySelector('#search-whole-word');
    var regex = document.querySelector('#search-regex');
    var mc = document.querySelector('#search-match-case');

    var expr = RegExp.escape(text);
    var params = 'm';
    if(regex.checked) {
        expr = text;
    }
    if(wwo.checked) {
        expr = `\\b${expr}\\b`;  // whole word only
    }
    if(!mc.checked) {
        params += 'i';  // case insensitive
    }
    return new RegExp(expr, params);
}

function processSearch(text, tag_toggled=false) {
    resetLogBlocks();
    var include_msg_block = document.querySelector('#search-in-msg');
    var include_code_block = document.querySelector('#search-in-code');
    var include_info_block = document.querySelector('#search-in-info');
    var regex = searchRegex(text);
    var total_num_results = 0;
    var shown_num_results = 0;

    log_blocks = document.querySelectorAll('.log-block');
    for(var x=0; x < log_blocks.length; x++) {
        if(log_blocks[x].textContent.match(regex)) {
            total_num_results += 1;
            found = log_blocks[x];
            log_entry = found.parentElement.parentElement;
            if(include_info_block.checked && found.classList.contains('info-block')) {
                btn = log_entry.querySelector('.info-btn > button');
            } else if(include_msg_block.checked && found.classList.contains('msg-block')) {
                btn = log_entry.querySelector('.msg-btn > button');
            } else {
                continue;
            }
            if(log_entry.style.display !== 'none') {
                shown_num_results += 1;
            }
            toggleShowHide(log_entry, hide=false);

            cur_depth = Number(log_entry.getAttribute('aria-label'));
            for(var j=log_entry.previousElementSibling; j !== null; j=j.previousElementSibling) {
                depth = Number(j.getAttribute('aria-label'));
                if(depth < cur_depth) {
                    cur_depth = depth;
                    expandLogs(j);
                } else if (depth <= 0) {
                    break;
                }
            }
            handleLogContent(btn, found.id, compress=false);
            found.firstElementChild.style.backgroundColor = 'rgba(0, 255, 0, 0.1)';
        }
    }

    search_results = document.querySelector('#search-count');
    search_results.innerHTML = total_num_results + ' total results match "' + text + '".<br/>' + shown_num_results + ' results shown.';
}

function search(search_el_id, tag_toggled=false) {
    search_el = document.querySelector('#'+search_el_id);
    search_results = document.querySelector('#search-count');
    search_results.innerHTML = 'Searching...';

    text = search_el.value;
    if(text.length == 0) {
        if(!tag_toggled) {
            search_results.innerHTML = 'Type something to search.';
        }
        return;
    }

    setTimeout(function () { processSearch(text, tag_toggled); }, 120);
}

function searchOnEnter(event, search_el_id) {
    if(event.keyCode === 13) {
        search(search_el_id);
    }
}

// Hide/Show By Log Tag
function handleLogTagFilter(filter) {
    log_tag = filter.querySelector('input[type="checkbox"]');
    log_entries = document.querySelectorAll('.log-entry');
    display = log_tag.checked ? 'block' : 'none';
    triggered_depth = -1;
    triggered = false;
    log_entries.forEach((log_entry) => {
        var name = log_entry.getAttribute('aria-valuetext');
        if(name !== null && name == log_tag.id) {
            log_entry.style.display = display;
            triggered = true;
            triggered_depth = Number(log_entry.getAttribute('aria-label'));
        } else if(triggered) {
            var depth = log_entry.getAttribute('aria-label');
            if(Number(depth) > triggered_depth) {
                log_entry.style.display = display;
            } else {
                triggered = false;
            }
        }
    })
    search('search', tag_toggled=true);
}
