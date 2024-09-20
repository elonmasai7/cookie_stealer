from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    url = input("Please enter the URL you want to visit (e.g., http://example.com): ")
    driver.get(url)
    time.sleep(10)
    cookies = driver.get_cookies()
    print("Cookies obtained:")
    for cookie in cookies:
        print(cookie)

finally:
    driver.quit()
