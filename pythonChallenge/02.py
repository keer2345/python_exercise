#!/usr/bin/env python
# -*- encoding:utf-8 -*-

#  http://www.pythonchallenge.com/pc/def/ocr.html

import requests
import re


def findCharacter(url):
    html = requests.get(url)
    html_text = html.text

    html_text = html_text[html_text.find("-->"):]

    #  str = ""

    #  for c in html_text:
    #  if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
    #  str += c

    regex = re.compile("[a-zA-Z]+")
    str = regex.findall(html_text)
    str = "".join(str)

    return str


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    print(findCharacter(url))

#  最后找到单词equality:
#  http://www.pythonchallenge.com/pc/def/equality.html
