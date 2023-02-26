import os
from selenium import webdriver


def scraping(request):
    # ドライバーセッティング
    driver = webdriver.Chrome(
            os.getcwd() + "/tmp/chromedriver", options=setting_chrome_options())
    
    driver.get('https://en.wikipedia.org/wiki/Special:Random')
    line = driver.find_element_by_class_name('firstHeading').text
    print(line)
    driver.quit()
    return line



def setting_chrome_options():

    driverPath = "/tmp" + "/chromedriver"
    headlessPath = "/tmp" + "/headless-chromium"

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--hide-scrollbars")
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--log-level=0")
    chrome_options.add_argument("--v=99")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.binary_location = os.getcwd() + headlessPath

    # print("get driver")
    return chrome_options


if __name__ == "__main__":
    scraping()
