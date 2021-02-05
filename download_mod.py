from selenium import webdriver
import subprocess
import time
import os


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

    # def show_downloaded_files(self):
    #     self.browser.get('chrome://downloads/')
    #     time.sleep(1)
    #
    # def download_installator(self):
    #     self.installator = self.browser.find_elements_by_xpath('//*[@id="file-link"]')
    #     time.sleep(1)
    #     self.installator.click()

# TODO podmienic nazwe wersji installera pobierajac scraperem aktualna wersje ze strony, i dokonczyc przeklikanie instalacji


    def get_installer_from_dir(self):
        directory = r"C:\Users\dklec\Downloads"
        subprocess.Popen(os.path.join(directory, "Aslains_WoT_Modpack_Installer_v.1.11.1.2_02.exe"))







mods = ModDownload()
mods.get_page()
mods.accept_cookies()
mods.get_mod()
# mods.show_downloaded_files()
# mods.download_installator()
mods.get_installer_from_dir()
