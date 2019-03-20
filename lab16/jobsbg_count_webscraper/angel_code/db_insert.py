#!/bin/env python
import sqlite3
from lxml import html
import requests
import datetime
page = requests.get('http://jobs.bg/index.php')
tree = html.fromstring(page.content)

#Addind craped numbers to a list
jobs = tree.xpath('//span[@style="color:#8dbe35;font-weight:bold;"]/text()')

#Checking if list of 2 elements
if len(jobs) < 2:
    jobs.append('0')

#Writing the result into a file
file = open("jobsnumber.txt","a")
file.write(str(datetime.datetime.now())) 
file.write("    ")
file.write(str(jobs) + '\n')
file.close()

#Writing the stats into a DB
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("INSERT INTO jobstats (date, time, totaljobs, newjobs) VALUES (?, ?, ?, ?)",(date, time, jobs[0], jobs[1]))
conn.commit()
