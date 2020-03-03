#!/usr/bin/python 
# -*- coding: UTF-8 -*-

import os
import re
import platform

f = open('D:\ipconfig.txt','w')
system = platform.system()
if system == 'windows':
    for line in os.popen('ipconfig /all'):
        f.write(line)
else:
    outs = os.popen("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1").read()
    for line in outs:
        f.write(line)
f.close()



