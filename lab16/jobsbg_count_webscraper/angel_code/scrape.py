from lxml import html
import requests
import datetime
page = requests.get('http://jobs.bg/index.php')
tree = html.fromstring(page.content)
#print(tree)
#This will create a list of buyers:
jobs = tree.xpath('//span[@style="color:#8dbe35;font-weight:bold;"]/text()')
#print(jobs)
file = open("jobsnumber.txt","a")
file.write(str(datetime.datetime.now())) 
file.write("    ")
file.write(str(jobs) + '\n')
file.close()