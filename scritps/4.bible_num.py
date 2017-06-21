#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3


def char_len(conn):
    c = conn.cursor()
    query = '''
SELECT
    gospels,
    SUM(LENGTH(content)),
    SUM(LENGTH(content))-(SUM(LENGTH(content))-SUM(LENGTH(REPLACE(content, ' ', ''))))
    AS count
FROM
    bible
GROUP BY
    gospels
'''
    u_c = conn.cursor()
    for row in c.execute(query):
        u_query = 'INSERT INTO bible_len (gospels, char_all, char) VALUES ("%s", %s, %s)' % (row[0], row[1], row[2])
        u_c.execute(u_query)
        print(u_query)
    conn.commit()


def chapter_len(conn):
    total = 0
    c = conn.cursor()
    query = '''
SELECT
    gospels,
    MAX(chapter)
FROM bible
GROUP BY
    gospels;
'''
    u_c = conn.cursor()
    for row in c.execute(query):
        total += int(row[1])
        u_query = 'UPDATE bible_len SET chapter=%s WHERE gospels="%s"' % (row[1], row[0])
        u_c.execute(u_query)
        print(row[0], row[1])

    u_query = 'UPDATE bible_len SET chapter=%d WHERE gospels="SUM"' % (total)
    u_c.execute(u_query)
    print('SUM ', total)
    conn.commit()


def main():
    conn = sqlite3.connect('bible.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bible_len(
            "id" UNSIGNED INT NULL,
            "gospels" CHAR(16) NULL,
            "chapter" UNSIGNED INT NULL,
            "paragraph" UNSIGNED INT NULL,
            "char_all" UNSIGNED INT NULL,
            "char" UNSIGNED INT NULL,
            UNIQUE(gospels))
            ''')
    char_len(conn)
    chapter_len(conn)

    conn.close()

if __name__ == '__main__':
    main()
