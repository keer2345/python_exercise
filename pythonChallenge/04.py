#!/usr/bin/env python
# -*- encoding:utf-8 -*-

#  http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests
import re
import time


def getHtml(url, nothing):
    list = []
    i = 1

    param = {'nothing': nothing}
    html = requests.get(url, params=param)
    html_text = html.text

    regex = re.compile(r'[0-9]+$')
    nothing2 = regex.findall(html_text)
    nothing2 = "".join(nothing2)

    while True:
        #  time.sleep(1)
        if html_text.split()[-1] == nothing2:
            i = i + 1
            html_text = requests.get(url, params={'nothing': nothing2}).text
            if html_text == 'Yes. Divide by two and keep going.':
                nothing2 = str(int(int(nothing2) / 2))
                html_text = html_text + " " + nothing2
            else:
                nothing2 = "".join(regex.findall(html_text))
            print("i:" + str(i) + ",nothing:" + nothing2)
        else:
            break

    list.append(i)
    list.append(html_text)
    return list


#  最后得到peak.html
#  http://www.pythonchallenge.com/pc/def/peak.html

if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    nothing = '12345'
    print(getHtml(url, nothing))
