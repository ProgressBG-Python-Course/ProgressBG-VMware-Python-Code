from urllib import request
from bs4 import BeautifulSoup
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
	products_list = bs_parser.find('ul', class_='products')

	for product in products_list.find_all("li"):			
		try:
			name = product.select("a h2")[0].string
			price_str = str(product.select("span.price")[0])
			price = re.findall(r'class="price">(\d+)', price_str)[0]
		except:
			continue			

		products.append((name,int(price)))

def print_scraped_data(products):
	sorted_by_price = sorted(products, key=lambda p: p[1])
	for i in sorted_by_price:
		print("{} - {}".format(i[0],i[1]))


start_url = "https://laptop.bg/laptops-lenovo"
pages = 1
products = []

for i in range(1,pages+1):
	# https://laptop.bg/laptops-lenovo?page=2
	url = start_url+f'?page={i}'
	print("Scraping URL:", url)
	page_content = get_html(url)
	scrape_data(page_content)

	
print_scraped_data(products)



