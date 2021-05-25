# install the following:
# pip install selenium
# pip install Pillow
# see the README, second section for osx
from selenium import webdriver
import time, os
from PIL import Image

# This one, unlike the linux one, isn't set to be headless. You'll actually see a chrome browser window open while it runs. You can make it headless if needed - just look at the linux version.

url = "https://google.com"

DRIVER = './chromedriver'
driver = webdriver.Chrome('chromedriver') # Get at https://chromedriver.chromium.org/
driver.set_page_load_timeout(5)
driver.get('https://evol13.com')
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