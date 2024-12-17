import os
import subprocess
from time import time

BASE_URL="https://www.lambdatest.com"
URI_PLAYGROUND="selenium-playground"
BASE_URL_TEST=f"{BASE_URL}/{URI_PLAYGROUND}"

LAMBDA_WSS="wss://cdp.lambdatest.com/playwright?capabilities="

LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

PLAYWRIGHT_VERSION = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]

BROWSER_SETUP = [{"browser": "Chrome", "platformName": "Windows 10"}, 
                 {"browser": "MicrosoftEdge", "platformName": "macOS Sonoma"}]

timestamp = int(time())

CAPABILITY = {
                'browserName': "Chrome",  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
                'browserVersion': 'latest',
                'LT:Options': {
                        'platform': "Windows 10",
                        'build': f'New Build - {timestamp}',
                        'name': "Testing Settings",
                        'user': LT_USERNAME,
                        'accessKey': LT_ACCESS_KEY,
                        'network': True,
                        'video': True,
                        'console': True
                }
        }