#!/usr/bin/env python
# -*- encoding:utf-8 -*-

#  http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests
import pickle


def getHtml(url):
    html = requests.get(url)
    html_text = html.text

    return html_text


def unPicker(content):
    result = pickle.loads(content)
    return result


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    content = getHtml(url)
    #  str to byte
    content = str.encode(content)
    result = unPicker(content)
    #  print(result)
    print('\n'.join([''.join([p[0] * p[1] for p in row]) for row in result]))

#  最后得到channel.html
#  http://www.pythonchallenge.com/pc/def/channel.html
