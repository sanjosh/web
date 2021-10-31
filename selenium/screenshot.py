
from selenium import webdriver
from PIL import Image # pip install Pillow

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

driver = webdriver.Chrome(executable_path = '/home/sandeep/chromedriver/chromedriver')
url = "https://www.google.com/"
driver.get(url)
driver.save_screenshot('selenium_screenshot.png')
screenshot = Image.open('selenium_screenshot.png')
screenshot.show()
