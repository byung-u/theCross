#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sqlite3
import glob
from abbreviation import ABBREVIATION_DICT


def db_init():
    conn = sqlite3.connect('bible.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bible(
            "gospels" char(16) NULL,
            "chapter" UNSIGNED TINYINT NULL,
            "paragraph" UNSIGNED TINYINT NULL,
            "subject" char(128) NULL,
            "content" text NULL,
            UNIQUE(gospels, chapter, paragraph))
            ''')
    return conn


def get_blble_gospel(gospel_info):
    # 창1:1
    r = re.compile('(\D+)(\d+):(\d+)')
    m = r.match(gospel_info)
    if m is None:
        print('[ERROR1] ', gospel_info)
        return None, None, None

    if len(m.groups()) == 3:
        return ABBREVIATION_DICT[m.group(1)], m.group(2), m.group(3)
    else:
        print('[ERROR2] ', gospel_info)
        return None, None, None


def get_bible_contents(contents_array):
    subject = []
    content = []
    find_subject = 0
    for c in contents_array:
        if find_subject == 0:
            if (c.find('<') != -1):
                subject.append(c.replace('<', ''))
            elif (c.find('>') != -1):
                subject.append(c.replace('>', ''))
                find_subject = 1
            else:
                subject.append(c)
        else:
            content.append(c)
    return (' '.join(subject)), (' '.join(content))


def db_insert(conn, gos, ch, pa, subject, content):
    ic = conn.cursor()
    query = 'INSERT INTO bible VALUES("%s", %s, %s, "%s", "%s")' % (
            gos, ch, pa, subject, content)
    ic.execute(query)
    conn.commit()


def db_update(conn, gos, ch, pa, content):
    uc = conn.cursor()
    query = '''
        UPDATE bible
        SET content="%s"
        WHERE gospels="%s" AND chapter=%d AND paragraph=%d
    ''' % (content, gos, int(ch), int(pa))
    uc.execute(query)
    conn.commit()


def read_and_dump(conn, file_name):
    with open(file_name) as f:
        for line in f:
            b = line.split()
            print(b)
            gos, ch, pa = get_blble_gospel(b[0])
            if gos is None:
                raise('get bible info failed', line)
            db_update(conn, gos, ch, pa, ' '.join(b[1:]))
    f.closed


def read_and_dump_need_pay(conn, file_name):
    subject = None
    with open(file_name) as f:
        for line in f:
            if (line.find('<') != -1) and (line.find('>') != -1):
                b = line.split()
                gos, ch, pa = get_blble_gospel(b[0])
                if gos is None:
                    raise('get bible info failed', line)

                subject, content = get_bible_contents(b[1:])
            else:
                b = line.split(' ')
                gos, ch, pa = get_blble_gospel(b[0])
                if gos is None:
                    raise('get bible info failed', line)

                content = ' '.join(b[1:])

            db_insert(conn, gos, ch, pa, subject, content)
    f.closed


def main():
    conn = db_init()

    # TODO: option
    mode = 1
    entries = glob.glob('../bible/*.txt')
    if mode == 0:  # 개역개정 유료
        for file_name in entries:
            read_and_dump_need_pay(conn, file_name)
    else:   #
        for file_name in entries:
            read_and_dump(conn, file_name)


if __name__ == '__main__':
    main()
