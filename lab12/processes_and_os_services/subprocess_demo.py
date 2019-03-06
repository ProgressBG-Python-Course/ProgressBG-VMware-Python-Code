import subprocess

output = subprocess.check_output(["pwd"])
print(output)