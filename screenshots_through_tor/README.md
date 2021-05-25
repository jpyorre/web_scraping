Take screenshots using TOR - Used to look at domains that we have blocked.

To use, you need to install the command line version of TOR.

sudo apt install tor

By default, Tor runs on port 9050. Confirm with: ss | grep 9050

Test connectivity without TOR to see your IP

wget -qO - https://api.ipify.org; echo

Check through TOR:

torsocks wget -qO - https://api.ipify.org; echo

Restart TOR for with:

sudo systemctl restart tor

-----------------
Install requirements:

pip3 install -r requirements.txt

Grab a copy of the correct chromedriver for your system here: https://sites.google.com/a/chromium.org/chromedriver/ and put it in this folder.

Run the screenshots_through_tor.py script with a list of domains to attempt to grab screenshots. TOR can be slow, so it might fail. This script could be modified to point towards a faster SOCKS proxy outside the Umbrella network.

python3 screenshots_through_tor.py domains.txt
