#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import glob
import sys
import subprocess
from collections import Counter

bible_word = {}


def count_word(file_name):
    f = open(file_name, 'r')
    wc = Counter(f.read().split())
    for item in sorted(wc.items(), key=lambda pair: pair[1], reverse=False):
        if (item[0].find(':') >= 0):
            continue
        if (item[0].find('<') >= 0):
            continue
        if (item[0].find('>') >= 0):
            continue
        # print("{}\t{}".format(*item))
        w = item[0].strip()
        cnt = item[1]
        try:
            bible_word[w]
            last_count = bible_word[w]
            total = last_count + cnt
            bible_word[w] = total
        except KeyError:
            bible_word[w] = cnt
            continue
    f.close()


def change_file_encoding(file_path):
    path = '%s/*.txt' % file_path
    entries = glob.glob(path)
    for entry in entries:
        e = entry.split('/')
        file_name = e[-1]
        new_file_name = file_name.split()
        print(file_name, new_file_name[1])
        command = 'iconv -f euc-kr -t utf-8 "/Users/byungwoo/git/theCross/bible/%s" > "/Users/byungwoo/git/theCross/bible/%s"' % (
                file_name, new_file_name[1])
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode != 0:
            print('[ERR]', command)


def main():
    change_file_encoding('../bible')


if __name__ == '__main__':
    main()
