#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
from abbreviation import ABBREVIATION_DICT


def main():
    conn = sqlite3.connect('bible.db')
    c = conn.cursor()

    query = 'SELECT gospels, chapter, MAX(paragraph) FROM bible GROUP BY gospels,chapter;'
    temp = {}
    for row in c.execute(query):
        try:
            if temp[row[0]] != 0:
                temp[row[0]] += row[2]
        except:
            temp[row[0]] = row[2]

    # print(temp)
    for idx, abb in enumerate(ABBREVIATION_DICT):
        gospel = ABBREVIATION_DICT[abb]
        print(gospel, temp[gospel])
        u_query = 'UPDATE bible_len SET id=%d,paragraph=%s WHERE gospels="%s"' % (idx+1, temp[gospel], gospel)
        c.execute(u_query)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
