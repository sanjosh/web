'''
https://stackoverflow.com/questions/43149534/selenium-webdriver-how-to-download-a-pdf-file-with-python

https://stackoverflow.com/questions/56897041/how-to-save-opened-page-as-pdf-in-selenium-python
'''
import json

from selenium import webdriver

download_dir = "/home/sandeep/chromedriver/" # for linux/*nix, download_dir="/usr/Public"

chrome_options = webdriver.ChromeOptions()

# profile = {
#             "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
#            "download.default_directory": download_dir,
#            "download.extensions_to_open": "applications/pdf"
#            }
# chrome_options.add_experimental_option("prefs", profile)

# chrome_options.add_argument(f"--user-data-dir={profile}/{cognito}")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--verbose")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-session-crashed-bubble")
chrome_options.add_argument("window-size=1920x1080")
# chrome_options.add_argument("user-agent=User-Agent: Mozilla/5.0 "
#                             "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
#                             " (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")

settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),
           'savefile.default_directory': '/home/sandeep/kognitos'}
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')

driver = webdriver.Chrome('/home/sandeep/chromedriver/chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(5)

url = 'https://dol.ny.gov/unemployment-insurance-rate-information'
driver.get(url)
driver.execute_script('window.print();')
sleep(10)
driver.quit()
