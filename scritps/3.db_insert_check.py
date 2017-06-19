#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3


def main():
    conn = sqlite3.connect('bible.db')
    c = conn.cursor()
    query = 'SELECT gospels,chapter,paragraph FROM bible'
    for row in c.execute(query):
        if (row[2] == 1):
            num = 1
            continue
        if int(row[2]) == (num + 1):
            print(row[2], num+1)
            num += 1
            # print('ok')
        else:
            print('[ERROR] ', row)


if __name__ == '__main__':
    main()
