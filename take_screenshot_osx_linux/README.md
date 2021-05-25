Take screenshots of websites with python:


To get the screenshot tool working, you need two things:
chromedriver
google chrome browser
=====================================
Headless version (linux with no GUI):
=====================================
Download chromedriver here:
https://chromedriver.chromium.org/

Make sure to download the linux one.


and put it somewhere, then reference it in screen-linux.py on this line:
driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)

Then, do get chrome browser:
sudo apt-get install -y libglib2.0-0 libnss3 libappindicator1 fonts-liberation libx11-xcb1
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb

See if it runs:
google-chrome-stable --headless --disable-gpu

If will hopefully give you an error message that looks something like this:

google-chrome-stable : Depends: libappindicator3-1 but it is not going to be installed
                        Depends: libasound2 (>= 1.0.16) but it is not going to be installed
                        Depends: libatk-bridge2.0-0 (>= 2.5.3) but it is not going to be installed
                        Depends: libatspi2.0-0 (>= 2.9.90) but it is not going to be installed
                        Depends: libgtk-3-0 (>= 3.9.10) but it is not going to be installed
                        Depends: libxss1 but it is not going to be installed
                        Depends: libxtst6 but it is not going to be installed
                        Depends: xdg-utils (>= 1.0.2) but it is not going to be installed
                        Recommends: libu2f-udev but it is not going to be installed

To fix, run:
sudo apt --fix-broken install

Then try again:
google-chrome-stable --headless --disable-gpu

It should just work.

Now try to get a screenshot using screen-linux.py


=====================================
Run on Mac OSX:
=====================================
Download chromedriver here:
https://chromedriver.chromium.org/
Get the one for OSX

