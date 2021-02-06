import os
import subprocess
import time
import re

from selenium import webdriver


class ModDownload():

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')

    def get_page(self):
        self.browser.get('https://aslain.com/index.php?/topic/13-download-%E2%98%85-world-of-tanks-%E2%98%85-modpack/')
        time.sleep(1)

    def accept_cookies(self):
        self.accept = self.browser.find_elements_by_xpath('//*[@id="elGuestTerms"]/div/div/div[2]/a')[0]
        time.sleep(1)
        self.accept.click()
        time.sleep(1)

    def mod_download(self):
        self.direct = self.browser.find_elements_by_xpath(
            '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[8]/span[1]/a')[0]
        time.sleep(1)
        self.direct.click()

    def get_mod_version_number(self):
        self.version = self.browser.find_elements_by_xpath(
            '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[7]/span[1]/span/strong')

        ver_data = []

        for value in self.version:
            ver_data.append(value.text)
            # print(value.text)

        text = ver_data[0]

        m = re.search('ModPack v(.+?) ', text)
        if m:
            version_num = m.group(1)
        # print(version)
        return version_num

    def get_next_number(self):
        self.number = self.browser.find_elements_by_xpath(
            '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[7]/span[2]/span/strong')

        num_data = []

        for v in self.number:
            num_data.append(v.text)
            v.text.replace('#', '_')
            # print(v.text)

        number = num_data[0].replace('#', '_')
        # print(number)

        return number

    def get_installer_from_dir(self):
        directory = r"C:\Users\dklec\Downloads"
        subprocess.Popen(os.path.join(directory, "Aslains_WoT_Modpack_Installer_v."
                                      + self.get_mod_version_number()
                                      + self.get_next_number() + ".exe"))


mods = ModDownload()
mods.get_page()
mods.accept_cookies()
mods.mod_download()
mods.get_mod_version_number()
mods.get_next_number()
mods.get_installer_from_dir()
