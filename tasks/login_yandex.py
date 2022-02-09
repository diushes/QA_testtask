from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class YandexLoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://yandex.ru/'
    
    def goLoginpage(self):
        self.browser.get(self.url)
        self.browser.find_element_by_class_name('desk-notif-card__login-new-item-title').click()
    
    def typeInCredentials(self, login, password):
        login_field = self.browser.find_element_by_name('login')
        login_field.send_keys(login)
        login_field.send_keys(Keys.ENTER)

        password_field = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "passp-field-passwd")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)



browser = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver')
login = "awesome.diushes"
password = "i.awesome.diushes"

testYandexLogin = YandexLoginPage(browser=browser)
testYandexLogin.goLoginpage()
testYandexLogin.typeInCredentials(login, password)
