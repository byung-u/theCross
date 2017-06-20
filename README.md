theCross
========
Bible analysis


사용 가능 저작권 확인
------------
http://www.bskorea.or.kr/about/book/faq.aspx#faq01


숫자로 보는 성경
------

- 성경 권수
```
sqlite> SELECT COUNT(DISTINCT gospels) FROM bible;
66
```

- 문자 수 예시
```
sqlite> SELECT content FROM bible LIMIT 1;
태초에 하나님이 천지를 창조하시니라
sqlite> SELECT LENGTH(content) FROM bible LIMIT 1;
19
sqlite> SELECT LENGTH(REPLACE(content, ' ', '')) FROM bible LIMIT 1;
16
```

- 공백 포함한 문자 수
```
SELECT gospels, SUM(LENGTH(content)) AS count FROM bible GROUP BY gospels UNION ALL SELECT 'SUM' gospels, SUM(LENGTH(content)) FROM bible;
```
- 공백 제거한 문자 수
```
SELECT gospels, SUM(LENGTH(content))-(SUM(LENGTH(content))-SUM(LENGTH(replace(content, ' ', '')))) AS count FROM bible GROUP BY gospels UNION ALL SELECT 'SUM' gospels, SUM(LENGTH(content))-(SUM(LENGTH(content))-SUM(LENGTH(replace(content, ' ', '')))) FROM bible;
```

- 합쳐서 한번에
```
SELECT
    gospels,
    SUM(LENGTH(content)),
    SUM(LENGTH(content))-(SUM(LENGTH(content))-SUM(LENGTH(REPLACE(content, ' ', ''))))
    AS count
FROM
    bible
GROUP BY
    gospels
UNION ALL
    SELECT 'SUM'
        gospels,
        SUM(LENGTH(content)),
        SUM(LENGTH(content))-(SUM(LENGTH(content))-SUM(LENGTH(REPLACE(content, ' ', ''))))
    FROM
        bible;

```


- 성경 절수
```
SELECT
    gospels,
    SUM(paragraph)
FROM bible
GROUP BY
    gospels
UNION ALL
    SELECT 'SUM'
        gospels,
        SUM(paragraph)
    FROM
        bible;
```

- 성경 장수
```
SELECT
    gospels,
    MAX(chapter)
FROM bible
GROUP BY
    gospels;
```
