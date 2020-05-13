-- pragma
pragma foreign_keys = ON;
pragma journal_mode = wal;

-- Legend
create table if not exists log_tags (
    name text not null primary key,
    value integer not null,
    color text not null
);

-- Log Entries
create table if not exists log_entries (
    id integer primary key autoincrement,
    file_path text not null,
    function_name text,
    line_num integer not null,
    msg text not null,
    tag_name text not null,
    depth integer not null,
    thread_id integer,
    thread_name text,
    is_main_thread int not null,
    timestamp datetime default (datetime('now', 'localtime'))
);
