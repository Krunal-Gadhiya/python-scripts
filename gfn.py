#!/usr/bin/env python3

# Desired Output
# 'file-name','file-name','file-name','file-name','file-name','file-name','file-name','file-name','file-name'

import os
from sys import argv

basePath = argv[1]
fileExtension = argv[2]
finalStr = ''

with os.scandir(basePath) as entries:
    for entry in entries:
        if entry.is_file() and entry.name.endswith(fileExtension):
            tempName = entry.name.replace(fileExtension, '')
            finalStr += ("'" + tempName + "',")

finalStr = finalStr[:-1]

print(finalStr)
