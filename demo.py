from selenium import webdriver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
wd = webdriver.Chrome('chromedriver',options=options)
# wd.get("https://www.creditchina.gov.cn/")
wd.get("https://www.creditchina.gov.cn/xinyongdongtai/?navPage=1")
print(wd.page_source)
