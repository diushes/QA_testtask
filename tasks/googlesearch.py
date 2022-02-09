from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogSearchPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://www.google.com/"

    def go(self):
        self.browser.get(self.url)

    def search(self, text):
        searchbox = self.browser.find_element_by_name('q')
        searchbox.clear()
        searchbox.send_keys(text)
        searchbox.send_keys(Keys.ENTER)
    
    def get_results(self):
        results = self.browser.find_elements_by_class_name("yuRUbf a")[:20]
        links = [ link.get_attribute('href') for link in results ]
        return links 

    
browser = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver')
searchproductpage = GoogSearchPage(browser=browser)
searchproductpage.go()
searchproductpage.search('купить кофемашину bork c804')
links = searchproductpage.get_results()
if "https://www.mvideo.ru/products/kofeinaya-stanciya-bork-c804-4000182" in links:
    print("Search results contain mvideo webpage")
