from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

'''
https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
pip install selenium


https://sites.google.com/chromium.org/driver/
ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. 
version must match

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN wget https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip && mv chromedriver /usr/bin/chromedriver
'''

'''


How to invoke ?  Any of these steps should do the trick:
include the ChromeDriver location in your PATH environment variable
(Java only) specify its location via the webdriver.chrome.driver system property (see sample below)
(Python only) include the path to ChromeDriver when instantiating webdriver.Chrome (see sample below)

ChromeOptions
https://sites.google.com/chromium.org/driver/capabilities?authuser=0
'''

'''
sudo apt-get install python3-bs4 
'''
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--user-data-dir={profile}/{cognito}")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--verbose")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-session-crashed-bubble")
chrome_options.add_argument("window-size=1920x1080")
chrome_options.add_argument("user-agent=User-Agent: Mozilla/5.0 "
                            "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                            " (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")

driver = webdriver.Chrome('/home/sandeep/chromedriver/chromedriver', chrome_options=chrome_options)
driver.get("https://www.python.org")

print(driver.title)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# https://stackoverflow.com/questions/61308799/unable-to-locate-elements-in-selenium-python
search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()

search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

print(driver.current_url)
driver.close()

'''
ActionChains drag and drop
ActionChains are a way to automate low level interactions such as mouse movements, 
mouse button actions, key press, and context menu interactions. 
 This is useful for doing more complex actions like hover over and drag and drop.
https://selenium-python.readthedocs.io/navigating.html#drag-and-drop

proxy

remote webdriver
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webdriver
https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol

driver.forward/backward

option.click
element.submit

page object
https://selenium-python.readthedocs.io/page-objects.html

LoadableComponent
https://www.ontestautomation.com/using-the-loadablecomponent-pattern-for-better-page-object-handling-in-selenium/
not supported in python
https://www.selenium.dev/selenium/docs/api/py/api.html

headless download
https://gist.github.com/sudoxx2/2ebbdb52373a6cf3913668aaa2280245

scroll page
https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
'''


'''
https://github.com/SeleniumHQ/selenium/wiki

'''
