import re
import urllib

x = 1214

while x < 1846:
    source = urllib.urlopen("https://www.xkcd.com/" + str(x)).read()
    for link in re.findall("https://imgs.xkcd.com/comics/(.*)", source):
        print x
        print link
        pic_link = "https://imgs.xkcd.com/comics/" + link
        file_out = link
        urllib.urlretrieve(pic_link, file_out)
    x = x + 1

exit(1)