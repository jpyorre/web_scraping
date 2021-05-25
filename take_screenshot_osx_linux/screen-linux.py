# install the following:
# pip install selenium
# pip install Pillow
# see the README, first section for linux

from selenium import webdriver
import time, os
from PIL import Image
from selenium.webdriver.chrome.options import Options

url = 'https://www.google.com'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)   # Get at https://chromedriver.chromium.org/
driver.set_page_load_timeout(5)	#How long before you give up?
driver.get(url)	# go get it
time.sleep(4)	# wait this many seconds before stopping - in case you want to let the page fully load. Adjust as needed
driver.save_screenshot('temp.png')	# save as temp.png - it's filesize is kind of large
temp_screenshot = Image.open('temp.png')	# open that temp.png for resizing
s = list(temp_screenshot.size)  # Assign the width/height values to a list for resizing
resized = temp_screenshot.resize((int(s[0]/2),int(s[1]/2)),Image.ANTIALIAS) # resize image to half the size (change the 2 to whatever percentage you want in both fields)
resized.save('screenshot.png', optimize=True,quality=95) # Save resized screenshot
time.sleep(1) # wait a second before quitting. Not sure if you need this.
os.remove('temp.png')	# Delete the large file version
driver.quit()	# chrome quits here