import os
from os.path import normpath, join

path = normpath(join(os.getcwd(), 'data/'))
print(f'path: {path}')

stat_obj = os.stat(path)
print(f"{path} stat is:\n")
print(stat_obj)
