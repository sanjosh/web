
from selenium import webdriver
from PIL import Image # pip install Pillow
from urllib.parse import urlparse

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--user-data-dir={profile}/{cognito}")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
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
url = "https://www.cnn.com/"
url_p = urlparse(url)
screenshot_file = url_p.netloc + '_' + url_p.path.replace('/', '_') + '.png'
driver.set_page_load_timeout(30)

driver.get(url)
driver.save_screenshot(screenshot_file)
screenshot = Image.open(screenshot_file)
screenshot.show()
