import os

cwd = os.getcwd()
data_path = cwd + '/data/'

entries = os.listdir( path=data_path )

print( list(filter( lambda entry: entry.startswith(('a','A')), entries) ))


#/home/nemsys/projects/courses/ProgressBG/ProgressBG-VMware-Python/ProgressBG-VMware-Python-Code/lab12/using_the_filesystem

# TASK: print the entries witch names starts with 'a'


TASK:
# create 'data/test1', 'data/test2' entries