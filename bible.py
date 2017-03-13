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
        command = 'iconv -f euc-kr -t utf-8 /Users/byungwoo/git/BibleAnal/Bible/%s > /Users/byungwoo/git/BibleAnal/Bible/new_%s' % (file_name, file_name)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode != 0:
            print('[ERR]', command)


def main():
    # Make the help output a little less jarring.
    help_factory = (lambda prog: argparse.RawDescriptionHelpFormatter(
        prog=prog, max_help_position=28))

    parser = argparse.ArgumentParser(prog='bible_analysis', fromfile_prefix_chars='@', formatter_class=help_factory)
    parser.add_argument("-c", "--change_encoding", metavar='PATH', nargs=1, help="[mandatory] file path")
    args = parser.parse_args()
    if args.change_encoding:
        change_file_encoding(args.change_encoding[0])
        sys.exit(0)

    entries = glob.glob('./text/*.txt')
    for file_name in entries:
        count_word(file_name)
        # break

    for key, value in bible_word.items():
        print(key, value)


if __name__ == '__main__':
    main()
