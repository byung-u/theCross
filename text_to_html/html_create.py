#!/usr/bin/env python3
import glob

holynet_link = {"01": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=1&CN=1&CV=99",
                "14": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=14&CN=1&CV=99",
                "27": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=27&CN=1&CV=99",
                "02": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=2&CN=1&CV=99",
                "15": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=15&CN=1&CV=99",
                "28": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=28&CN=1&CV=99",
                "03": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=3&CN=1&CV=99",
                "16": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=16&CN=1&CV=99",
                "29": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=29&CN=1&CV=99",
                "04": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=4&CN=1&CV=99",
                "17": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=17&CN=1&CV=99",
                "30": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=30&CN=1&CV=99",
                "05": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=5&CN=1&CV=99",
                "18": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=18&CN=1&CV=99",
                "31": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=31&CN=1&CV=99",
                "06": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=6&CN=1&CV=99",
                "19": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=19&CN=1&CV=99",
                "32": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=32&CN=1&CV=99",
                "07": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=7&CN=1&CV=99",
                "20": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=20&CN=1&CV=99",
                "33": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=33&CN=1&CV=99",
                "08": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=8&CN=1&CV=99",
                "21": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=21&CN=1&CV=99",
                "34": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=34&CN=1&CV=99",
                "09": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=9&CN=1&CV=99",
                "22": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=22&CN=1&CV=99",
                "35": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=35&CN=1&CV=99",
                "10": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=10&CN=1&CV=99",
                "23": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=23&CN=1&CV=99",
                "36": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=36&CN=1&CV=99",
                "11": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=11&CN=1&CV=99",
                "24": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=24&CN=1&CV=99",
                "37": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=37&CN=1&CV=99",
                "12": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=12&CN=1&CV=99",
                "25": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=25&CN=1&CV=99",
                "38": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=38&CN=1&CV=99",
                "13": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=13&CN=1&CV=99",
                "26": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=26&CN=1&CV=99",
                "39": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=39&CN=1&CV=99",
                "40": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=40&CN=1&CV=99",
                "49": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=49&CN=1&CV=99",
                "58": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=58&CN=1&CV=99",
                "41": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=41&CN=1&CV=99",
                "50": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=50&CN=1&CV=99",
                "59": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=59&CN=1&CV=99",
                "42": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=42&CN=1&CV=99",
                "51": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=51&CN=1&CV=99",
                "60": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=60&CN=1&CV=99",
                "43": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=43&CN=1&CV=99",
                "52": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=52&CN=1&CV=99",
                "61": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=61&CN=1&CV=99",
                "44": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=44&CN=1&CV=99",
                "53": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=53&CN=1&CV=99",
                "62": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=62&CN=1&CV=99",
                "45": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=45&CN=1&CV=99",
                "54": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=54&CN=1&CV=99",
                "63": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=63&CN=1&CV=99",
                "46": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=46&CN=1&CV=99",
                "55": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=55&CN=1&CV=99",
                "64": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=64&CN=1&CV=99",
                "47": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=47&CN=1&CV=99",
                "56": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=56&CN=1&CV=99",
                "65": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=65&CN=1&CV=99",
                "48": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=48&CN=1&CV=99",
                "57": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=57&CN=1&CV=99",
                "66": "http://www.holybible.or.kr/B_RHV/cgi/bibleftxt.php?VR=RHV&VL=66&CN=1&CV=99",
                }


def syntax_highlighting(line):
    if line.find('유다왕') != -1:
        line = line.replace('유다왕', '<a href="https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%A4_%EC%99%95%EA%B5%AD" target="_blank">유다왕</a>')
    else:
        line = line.replace('유다', '<a href="https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%A4_%EC%99%95%EA%B5%AD#/media/File:Kingdoms_of_Israel_and_Judah_map_830.svg" target="_blank">유다</a>')
    line = line.replace('바벨론', '<a href="http://classic.scriptures.lds.org/ko/biblemaps/9" target="_blank">바벨론</a>')
    line = line.replace('갈대아인', '<a href="http://www.kcm.kr/dic_view.php?nid=40724" target="_blank">갈대아인</a>')
    line = line.replace('에돔', '<a href="https://ko.wikipedia.org/wiki/%EC%97%90%EB%8F%94" target="_blank">에돔</a>')
    line = line.replace('모압', '<a href="https://ko.wikipedia.org/wiki/%EB%AA%A8%EC%95%84%EB%B8%8C" target="_blank">모압</a>')
    line = line.replace('암몬', '<a href="https://ko.wikipedia.org/wiki/%EC%95%94%EB%AA%AC%EC%9D%B8" target="_blank">암몬</a>')
    # line = line.replace('', '<a href="" target="_blank"></a>')
    line = line.replace('인자야', '<span style="background-color: #f44265">인자야</span>')

    line = line.replace('그러므로', '<span style="background-color: #f44242">그러므로</span>')

    line = line.replace(' 내가', '<span style="background-color: #42f4ee"> 내가</span>')

    line = line.replace('네게', '<span style="background-color: #e29aba">네게</span>')
    line = line.replace('네가', '<span style="background-color: #e29aba">네가</span>')
    line = line.replace('너를', '<span style="background-color: #e29aba">너를</span>')
    line = line.replace('너희는', '<span style="background-color: #e29aba">너희는</span>')

    line = line.replace('그때에', '<span style="background-color: #FFFF00">그때에</span>')
    line = line.replace('그 날에', '<span style="background-color: #FFFF00">그 날에</span>')
    line = line.replace('여호와여', '<span style="background-color: #FFFF00">여호와여</span>')

    line = line.replace('말하노라', '<span style="background-color: #9ab6e2">말하노라</span>')
    line = line.replace('가라사대', '<span style="background-color: #9ab6e2">가라사대</span>')
    line = line.replace('이르기를', '<span style="background-color: #9ab6e2">이르기를</span>')

    line = line.replace('여호와께서', '<span style="background-color: #9ab6e2">여호와께서</span>')
    line = line.replace('여호와의 말이', '<span style="background-color: #9ab6e2">여호와의 말이</span>')
    line = line.replace('여호와의 말씀이', '<span style="background-color: #9ab6e2">여호와의 말씀이</span>')

    # 유다
    # 왕의 이름 뒤에 붙는 접두사
    # 은, 는, 이, 가, 와, 을, 를, 의, 왕,
    # (공백), (콤마)

    line = line.replace('사울', '사울<sub>(유다 1050~1010, 1 😨)</sub>')
    line = line.replace('다윗', '다윗<sub>(유다 1010~970, 2 😍)</sub>')
    line = line.replace('솔로몬', '솔로몬<sub>(유다 970~930, 3 😨)</sub>')
    line = line.replace('르호보암', '르호보암<sub>(유다 930~913, 4 😨 )</sub>')
    line = line.replace('아비야', '아비야<sub>(유다 913~911, 5 😨)</sub>')
    line = line.replace('아비얌', '아비얌<sub>(유다 913~911, 5 😨)</sub>')
    line = line.replace('여호사밧', '여호사밧<sub>(유다 870~853, 7 😀)</sub>')
    line = line.replace('여호람', '여호람<sub>(유다 853~841, 8 😨)</sub>')
    line = line.replace('아하시야', '아하시야<sub>(유다 841~841, 9 😨)</sub>')
    line = line.replace('아달랴', '아달랴<sub>(유다 841~835, 10 😱)</sub>')
    line = line.replace('요아스', '요아스<sub>(유다 835~796, 11 😀)</sub>')
    line = line.replace('아마샤', '아마샤<sub>(유다 796~767, 12 😀)</sub>')
    line = line.replace('웃시야', '웃시야<sub>(유다 767~750, 13 😀)</sub>')
    line = line.replace('요담', '요담<sub>(유다 750~743, 14 😀)</sub>')
    line = line.replace('히스기야', '히스기야<sub>(유다 728~697, 16 😀)</sub>')
    line = line.replace('므낫세', '므낫세<sub>(유다 697~642, 17 😱)</sub>')
    line = line.replace('아몬', '아몬<sub>(유다 642~640, 18 😨)</sub>')
    line = line.replace('요시야', '요시야<sub>(유다 640~609, 19 😆)</sub>')
    line = line.replace('여호아김', '여호아김<sub>(유다 609~597, 21 😨)</sub>')
    line = line.replace('여호아긴', '여호아긴<sub>(유다 597~597, 22 😨)</sub>')
    line = line.replace('여고냐', '여고냐<sub>(유다 597~597, 22 😨)</sub>')
    line = line.replace('고니야', '고니야<sub>(유다 597~597, 22 😨)</sub>')
    line = line.replace('시드기야', '시드기야<sub>(유다 597~586, 23 😨)</sub>')
    if line.find('여호아하스') != -1:
        line = line.replace('여호아하스', '여호아하스<sub>(유다 609~609, 20 😨)</sub>')
    else:
        line = line.replace('아하스', '아하스<sub>(유다 743~728, 15 😨)</sub>')
    if line.find('아사랴') != -1:
        line = line.replace('아사랴', '아사랴<sub>(유다 767~750, 13 😀)</sub>')
    else:
        line = line.replace('아사', '아사<sub>(유다 911~870, 6 😀)</sub>')
    # ...
    return '<p>%s</p>\n' % line


def main():
    entries = glob.glob('./*.txt')
    for src_file in entries:
        dst_file = src_file.replace('.txt', '.html')
        fw = open(dst_file, 'w')
        fw.write('<meta charset="utf-8">\n')
        with open(src_file) as f:
            bible_idx = src_file[2:4]
            b_link = '<a>%s</a><br>\n' % holynet_link[bible_idx]
            fw.write(b_link)
            for line in f:
                msg = syntax_highlighting(line)
                fw.write(msg)
        fw.close()
    return


if __name__ == '__main__':
    main()
