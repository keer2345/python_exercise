#!/usr/bin/env python
# -*- encoding:utf-8 -*-

#  http://www.pythonchallenge.com/pc/def/map.html

import requests
from bs4 import BeautifulSoup


def getFromUrl(url):
    html = requests.get(url)
    html_text = html.text

    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.find('font', attrs={'color': '#f000f0'})
    text = text.contents[0]

    return text


def convert(str):
    newStr = ""
    for s in str:
        if s >= 'a' and s <= 'x':
            newStr += chr(ord(s) + 2)
        else:
            if s >= 'y' and s <= 'z':
                newStr += chr(ord(s) - 26 + 2)
            else:
                newStr += s
    return newStr


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/map.html'

    str = getFromUrl(url)

    s2 = convert(str)
    print(s2)

#  根据字符转换规律，转换url的map-->ocr
#  http://www.pythonchallenge.com/pc/def/ocr.html
