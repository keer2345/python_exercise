#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import requests


def findCharacter(url):
    html = requests.get(url)
    html_text = html.text

    html_text = html_text[html_text.find("-->"):]

    str = ""

    for c in html_text:
        if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
            str += c

    return str


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    print(findCharacter(url))

#  最后找到单词equality:
#  http://www.pythonchallenge.com/pc/def/equality.html
