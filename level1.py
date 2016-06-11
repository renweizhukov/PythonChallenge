#!/usr/bin/python2.7
from string import maketrans

# http://www.pythonchallenge.com/pc/def/map.html

intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
outtab = "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB"
transTab = maketrans(intab, outtab)

scrambledStr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print scrambledStr.translate(transTab)   

url = 'map'
print url.translate(transTab)