from selenium import webdriver
import time


class ModDownload():

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')
        print('Mod do pobierania najnowszych modow Aslaina do World Of Tanks')
        time.sleep(1.0)
        print('AlainModsAutoDownload ver. 1.0')
        time.sleep(1.0)

    def get_page(self):
        self.browser.get('https://aslain.com/index.php?/topic/13-download-%E2%98%85-world-of-tanks-%E2%98%85-modpack/')
        time.sleep(1)

    def accept_cookies(self):
        self.accept = self.browser.find_elements_by_xpath('//*[@id="elGuestTerms"]/div/div/div[2]/a')[0]
        time.sleep(1)
        self.accept.click()
        time.sleep(1)

    def get_mod(self):
        self.acceptbutton = self.browser.find_elements_by_xpath(
            '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[8]/span[1]/a')[0]
        time.sleep(1)
        self.acceptbutton.click()


mods = ModDownload()
mods.get_page()
mods.accept_cookies()
mods.get_mod()
