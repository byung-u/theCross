#!/usr/bin/env python3
from random import choice
from bs4 import BeautifulSoup
from requests import get, codes

from define_bible import bible_chapter_name
USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko  ) '
                'Chrome/19.0.1084.46 Safari/536.5'),
               ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/  19.0.1084.46'
                'Safari/536.5'), )


def match_soup_class(self, target, mode='class'):
    def do_match(tag):
        classes = tag.get(mode, [])
        return all(c in classes for c in target)
    return do_match

def request_and_get(url):
    try:
        r = get(url, headers={'User-Agent': choice(USER_AGENTS)})
        if r.status_code != codes.ok:
            print([url], 'request error, code=', r.status_code)
            return False
        return r
    except TypeError:
        print([url], 'connect fail')
        return False


def main():
    url = 'http://www.holybible.or.kr/B_RHV/'
    base_url = 'http://www.holybible.or.kr'
    r = request_and_get(url)
    soup = BeautifulSoup(r.content.decode('euc-kr', 'replace'), 'html.parser')
    print('holynet_link = {')
    for idx1, table in enumerate(soup.find_all('table')):
        if idx1 != 8 and idx1 != 11:
            continue
        for idx2, tr in enumerate(table.find_all('tr')):
            if idx2 % 2 == 1:
                continue
            if idx2 < 2:
                continue
            if idx1 == 8:  # 구약 2 ~ 26
                if idx2 > 26:
                    break
            elif idx1 == 11: # 신약 2 ~ 18
                if idx2 > 18:
                    break
            for td in tr.find_all('td'):
                for li in td.find_all('li'):
                    href = li.a['href']
                    break
                else:
                    continue
                bible_ch = td.text.split('(')
                num = bible_chapter_name[bible_ch[0].strip().replace(' ', '')]
                print('        "%02d": "%s/%s",' % (int(num), base_url, href))
                # print('        "%02d_%s": "%s/%s",' % (cnt, td.text, base_url, href))
                # href_url = '%s/%s' % (base_url, href)
                # chapter = '%02d_%s' % (cnt, td.text)
    print('}')


if __name__ == '__main__':
    main()
