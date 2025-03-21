DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS txn;

CREATE TABLE book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    author TEXT NOT NULL
);

CREATE TABLE member (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE txn (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    FOREIGN KEY (book_id) REFERENCES book (id),
    FOREIGN KEY (member_id) REFERENCES member (id)
);
