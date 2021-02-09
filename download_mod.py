import logging
import os
import subprocess
import time
import re

from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ModDownload():

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=selenium")

        self.browser = webdriver.Chrome(options=chrome_options)

    def get_page(self):
        print("***Pobieranie url***")
        self.browser.get('https://aslain.com/index.php?/topic/13-download-%E2%98%85-world-of-tanks-%E2%98%85-modpack/')
        time.sleep(1)

    def accept_cookies(self):
        self.accept = self.browser.find_elements_by_xpath('//*[@id="elGuestTerms"]/div/div/div[2]/a')[0]
        time.sleep(1)
        self.accept.click()
        time.sleep(1)

    # TODO dodac try i except na klikanie roznych directow, przejsc do chrome downloads zeby dac allow na pobranie pliku
    def mod_download(self):

        self.direct = self.browser.find_elements_by_xpath(
            '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[9]/span/a')[0]
        time.sleep(1)
        self.direct.click()
        print("***Pobieranie moda***")
        time.sleep(1.0)

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

    def wait_for_file_and_open(self):
        path_downloads = r"C:\Users\dklec\Downloads"
        full_file_path = r"C:\Users\dklec\Downloads\Aslains_WoT_Modpack_Installer_v.1.11.1.3_00.exe"

        file_name = "Aslains_WoT_Modpack_Installer_v." + self.get_mod_version_number() + self.get_next_number() + ".exe"

        while not os.path.exists(full_file_path):
            time.sleep(3.0)

            print("File doesnt exist, retry ...")
        try:
            subprocess.Popen(os.path.join(path_downloads, file_name))

            webdriver.Chrome.close(self.browser)

        except Exception as e:
            print(e)


# def get_installer_from_dir(self):
#     directory = r"C:\Users\dklec\Downloads"
#     file_name = "Aslains_WoT_Modpack_Installer_v."
#
#     full_name = ("Aslains_WoT_Modpack_Installer_v."
#                  + self.get_mod_version_number()
#                  + self.get_next_number() + ".exe.torrent")
#
#     subprocess.Popen(os.path.join(directory, file_name
#                                   + self.get_mod_version_number()
#                                   + self.get_next_number() + ".exe"))
#
#     print("***Mod " + full_name + " - został pomyślnie zainstalowany***")
#     webdriver.Chrome.close(self.browser)


mods = ModDownload()
mods.get_page()
mods.accept_cookies()
mods.mod_download()
mods.get_mod_version_number()
mods.get_next_number()
mods.wait_for_file_and_open()
