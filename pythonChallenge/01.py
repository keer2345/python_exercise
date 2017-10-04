#!/usr/bin/env python
# -*- encoding:utf-8 -*-

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
    s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
    s2 = convert(s)
    print(s2)

#  根据字符转换规律，转换url的map-->ocr
#  http://www.pythonchallenge.com/pc/def/ocr.html
