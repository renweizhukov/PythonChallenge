#!/usr/bin/python2.7

# http://www.pythonchallenge.com/pc/def/map.html

def rotateLetter(ch):
    if ch.isalpha():
        if ch.islower():
            return chr((ord(ch) - ord('a') + 2) % 26 + ord('a'))
        else:
            return chr((ord(ch) - ord('A') + 2) % 26 + ord('A'))
    else:
        return ch

scrambledStr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print ''.join(rotateLetter(ch) for ch in scrambledStr)    

url = 'map'

print ''.join(rotateLetter(ch) for ch in url)