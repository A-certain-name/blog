drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);
drop table if exists comment;
create table comment (
  id integer primary key autoincrement,
  name string not null,
  text string not null
);
