#!/usr/bin/env python3
import re
import sqlite3
import glob
from shutil import copyfile

bible_chapter_number = {
        '01': '01_Genesis',
        '02': '02_Exodus',
        '03': '03_Leviticus',
        '04': '04_Numbers',
        '05': '05_Deuteronomy',
        '06': '06_Joshua',
        '07': '07_Judges',
        '08': '08_Ruth',
        '09': '09_1_Samuel',
        '10': '10_2_Samuel',
        '11': '11_1_Kings',
        '12': '12_2_Kings',
        '13': '13_1_Chronicles',
        '14': '14_2_Chronicles',
        '15': '15_Ezra',
        '16': '16_Nehemiah',
        '17': '17_Esther',
        '18': '18_Job',
        '19': '19_Psalms',
        '20': '20_Proverbs',
        '21': '21_Ecclesiastes',
        '22': '22_Song_of_Songs',
        '23': '23_Isaiah',
        '24': '24_Jeremiah',
        '25': '25_Lamentations',
        '26': '26_Ezekiel',
        '27': '27_Daniel',
        '28': '28_Hosea',
        '29': '29_Joel',
        '30': '30_Amos',
        '31': '31_Obadiah',
        '32': '32_Jonah',
        '33': '33_Micah',
        '34': '34_Nahum',
        '35': '35_Habakkuk',
        '36': '36_Zephaniah',
        '37': '37_Haggai',
        '38': '38_Zechariah',
        '39': '39_Malachi',

        '40': '40_Matthew',
        '41': '41_Mark',
        '42': '42_Luke',
        '43': '43_John',
        '44': '44_Acts',
        '45': '45_Romans',
        '46': '46_1_Corinthians',
        '47': '47_2_Corinthians',
        '48': '48_Galatians',
        '49': '49_Ephesians',
        '50': '50_Philippians',
        '51': '51_Colossians',
        '52': '52_1_Thessalonias',
        '53': '53_2_Thessalonias',
        '54': '54_1 Timothy',
        '55': '55_2_Timothy',
        '56': '56_Titus',
        '57': '57_Philemon',
        '58': '58_Hebrews',
        '59': '59_James',
        '60': '60_1_Peter',
        '61': '61_2_Peter',
        '62': '62_1_John',
        '63': '63_2_John',
        '64': '64_3_John',
        '65': '65_Jude',
        '66': '66_Revelation',
        }

bible_chapter_name = {
        '창세기': '01',
        '출애굽기': '02',
        '레위기': '03',
        '민수기': '04',
        '신명기': '05',
        '여호수아': '06',
        '사사기': '07',
        '룻기': '08',
        '사무엘상': '09',
        '사무엘하': '10',
        '열왕기상': '11',
        '열왕기하': '12',
        '역대상': '13',
        '역대하': '14',
        '에스라': '15',
        '느헤미야': '16',
        '에스더': '17',
        '욥기': '18',
        '시편': '19',
        '잠언': '20',
        '전도서': '21',
        '아가': '22',
        '이사야': '23',
        '예레미야': '24',
        '예레미야애가': '25',
        '에스겔': '26',
        '다니엘': '27',
        '호세아': '28',
        '요엘': '29',
        '아모스': '30',
        '오바댜': '31',
        '요나': '32',
        '미가': '33',
        '나훔': '34',
        '하박국': '35',
        '스바냐': '36',
        '학개': '37',
        '스가랴': '38',
        '말라기': '39',
        '마태복음': '40',
        '마가복음': '41',
        '누가복음': '42',
        '요한복음': '43',
        '사도행전': '44',
        '로마서': '45',
        '고린도전서': '46',
        '고린도후서': '47',
        '갈라디아서': '48',
        '에베소서': '49',
        '빌립보서': '50',
        '골로새서': '51',
        '데살로니가전서': '52',
        '데살로니가후서': '53',
        '디모데전서': '54',
        '디모데후서': '55',
        '디도서': '56',
        '빌레몬서': '57',
        '히브리서': '58',
        '야고보서': '59',
        '베드로전서': '60',
        '베드로후서': '61',
        '요한1서': '62',
        '요한2서': '63',
        '요한3서': '64',
        '유다서': '65',
        '요한계시록': '66',
        }

def main():
    entries = glob.glob('./*.txt')
    for src_file in entries:
        dst_file = './new_files/%s.txt' % bible_chapter[src_file[2:4]]
        copyfile(src_file, dst_file)


if __name__ == '__main__':
    main()
