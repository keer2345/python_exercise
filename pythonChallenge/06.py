import os
import re
import zipfile

path = "/home/qinjh/download/channel"
#  将工作目录转到该目录
os.chdir(path)

p = re.compile(r"Next nothing is (\d+)")
seed = '90052'
comments = []
z = zipfile.ZipFile("channel.zip", "r")
while True:
    fname = seed + ".txt"
    comments.append(bytes.decode(z.getinfo(seed + ".txt").comment))

    text = z.read(fname)
    text = bytes.decode(text)
    print(text)

    lists = p.findall(text)

    if lists:
        seed = lists[0]
        print("   Next is ", seed)
    else:
        break

print("".join(comments))
