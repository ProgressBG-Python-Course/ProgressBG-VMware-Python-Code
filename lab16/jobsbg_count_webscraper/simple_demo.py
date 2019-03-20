from urllib import request
from bs4 import BeautifulSoup
from datetime import datetime
import re


def get_html(url):
	if url.startswith("http"):
		# make the request - change UA to prevent server deny for scripts
		req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

		# get response
		respone = request.urlopen(req)
		return respone.read()
	else:
		with open(url,"r") as f:
		  return f.read()

def scrape_data(page):
	bs_parser = BeautifulSoup(page, 'html.parser')	

	# <span style="color:#8dbe35;font-weight:bold;">37 568</span>
	jobs_counts = bs_parser.find_all(
		'span', 
		attrs={"style": "color:#8dbe35;font-weight:bold;"},
	)

	return {
		'all_jobs': int(jobs_counts[0].string.replace(' ','')), 
		'daily_jobs': int(jobs_counts[1].string.replace(' ','')), 
		'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	}
		

def print_scraped_data(products):
	sorted_by_price = sorted(products, key=lambda p: p[1])
	for i in sorted_by_price:
		print("{} - {}".format(i[0],i[1]))


url = "https://www.jobs.bg/"
page_content = get_html(url)
scraped_data = scrape_data(page_content)
print(scraped_data)


