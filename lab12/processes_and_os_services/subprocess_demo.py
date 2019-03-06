import subprocess


# TASK:
# print the CWD ( `pwd` )

date_output = subprocess.check_output("pwd")

print(date_output)