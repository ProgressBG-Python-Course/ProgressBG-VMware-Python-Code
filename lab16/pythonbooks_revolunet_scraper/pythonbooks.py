from urllib import request
import json


def get_html(url):
	""" Summary
	
			Args:
			    url (string): a URL to get content from 
			
			Returns:
			    string: the content of URL
	"""
	
	# make the request - change UA to prevent server deny for scripts
	req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

	# get response
	respone = request.urlopen(req)
	
	return respone.read()
	

if __name__ == '__main__':	
	# using the 'https://pythonbooks.revolunet.com/' URL will return us the HTML, which is rendered by JavaScript on client-side. And that will make the scraper very difficult.
	# So, it is better to find the RestAPI/JSON file:
	url = "https://raw.githubusercontent.com/revolunet/PythonBooks/master/issues.json"	

	page_content = get_html(url)

	books = json.loads(page_content)
	
	print(books['books'][0])



