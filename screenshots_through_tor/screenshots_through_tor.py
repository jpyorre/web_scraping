import requests,sys,time,os
import tldextract as tld
from PIL import Image
# from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options

chromedrive_path = './chromedriver'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "socks5://127.0.0.1:9050"
prox.ssl_proxy = "socks5://127.0.0.1:9050"
capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)
driver = webdriver.Chrome(chromedrive_path,options=chrome_options, desired_capabilities=capabilities)
driver.set_page_load_timeout(5)

screenshot_path, success, fail = './', 'success.txt','fail.txt'
inputdata =sys.argv[1]
# domain = ininputdataput	# one domain

domains =[]	# multiple domains
with open(inputdata, 'r') as f:
	for line in f:
		nl=line.strip()
		domains.append(nl)

def write_append(filename, line):
	writefile = open(filename, "a")
	writefile.write(line)
	writefile.write("\n")
	writefile.close()

def screenshot_url(url):
	url = url.lstrip('.')
	print("Taking screenshot for {}".format(url))
	urlcomponents = tld.extract(url)
	filename = ".".join(i for i in urlcomponents).lstrip('.')
	driver.get(url)
	time.sleep(1)
	driver.save_screenshot(screenshot_path + '{}.png'.format(filename))
	time.sleep(1)
	driver.quit()
	final_filename = "{}.png".format(filename)
	return final_filename

def print_tor_ip(): # if you want to see your IP:
		proxies = {
	    'http': 'socks5://127.0.0.1:9050',
	    'https': 'socks5://127.0.0.1:9050'
		}
		tor_ip = requests.get('https://ident.me', proxies=proxies).text
		print("Used TOR IP '{}'".format(tor_ip))

for domain in domains:
	if not (domain.startswith('https://') or domain.startswith('http://')):
		url = "http://{}".format(domain)
		try:
			filename = screenshot_url(url)
			line = ("{}: Success".format(filename))
			print(line)
			write_append(success,line)
		except Exception as e:
			print(e)
			# url = "https://{}".format(domain)
			# line = ("{}: Failed".format(domain))
			# print(line)
			# write_append(fail,line)


# print_tor_ip() # if you want to see your IP: