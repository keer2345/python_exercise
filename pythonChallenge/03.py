#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import requests
import re


def getHtml(url):
    html = requests.get(url)
    html_text = html.text

    html_text = html_text[html_text.find(
        "<!--") + len("<!--") + 1:html_text.find("-->") - 1]

    return html_text


def getStr(html):
    #  regex = re.compile(r"[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}")
    regex = re.compile(r"[^A-Z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]{1}", re.S)
    str = regex.findall(html)

    result = ""

    for s in str:
        result += s[4:5]

    return result


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    html = getHtml(url)
    print(getStr(html))

#  最后找到单词elinkedlist:
#  http://www.pythonchallenge.com/pc/def/linkedlist.php
