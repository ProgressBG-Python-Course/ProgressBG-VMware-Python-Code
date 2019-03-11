# TASK:
# print the size in bytes of 'lines.txt' file

import os

stat = os.stat('lines.txt')
print(stat.st_mtime)
print(stat.st_birthtime)


# TODO: upload stat demo in slides for getting file creation time