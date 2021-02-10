import os
import re
import subprocess
import time

from selenium.webdriver.chrome.options import Options

from selenium import webdriver


class ModDownload:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=selenium")

        self.browser = webdriver.Chrome(options=chrome_options)

    def get_page(self):
        url = 'https://aslain.com/index.php?/topic/13-download-%E2%98%85-world-of-tanks-%E2%98%85-modpack/'
        print("***Getting URL***")

        self.browser.get(url)
        time.sleep(1)

    def accept_cookies(self):
        self.accept = self.browser.find_elements_by_xpath('//*[@id="elGuestTerms"]/div/div/div[2]/a')[0]
        time.sleep(1)
        self.accept.click()
        time.sleep(1)

    def mod_download(self):
        download_href_1 = '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[9]/span/a'
        download_href_2 = '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[10]/span/a'
        download_href_3 = '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[11]/span[3]/a'

        while True:

            try:
                print("***Attempt to download link ...")
                time.sleep(1.0)
                self.direct = self.browser.find_elements_by_xpath(download_href_1)[0]
                break
            except Exception as e:
                print("***Invalid link!*** ", e)
                time.sleep(1.0)

            try:
                print("***Attempt to download next link ...")
                time.sleep(1.0)
                self.direct = self.browser.find_elements_by_xpath(download_href_2)[0]
                break
            except Exception as e:
                print("***Invalid link!*** ", e)
                time.sleep(1.0)

            try:
                print("***Attempt to download next link ...")
                time.sleep(1.0)
                self.direct = self.browser.find_elements_by_xpath(download_href_3)[0]
                break
            except Exception as e:
                print("***Invalid link!*** ", e)
                break

        time.sleep(1)
        self.direct.click()
        print("***Aslain's Mods Downloading***")
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

        file_name = "Aslains_WoT_Modpack_Installer_v." + self.get_mod_version_number() + self.get_next_number() + ".exe"
        full_file_path = path_downloads + '\\' + file_name

        while not os.path.exists(full_file_path):
            time.sleep(3.0)
            print("***File not found, retry ...")

            # TODO wylaczyc program jezeli przegladarka zostala zamknieta
            # if 1:
            #     webdriver.Chrome.close(self.browser)

        try:
            print("***File was found! Opening ...")
            subprocess.Popen(os.path.join(path_downloads, file_name))

            webdriver.Chrome.close(self.browser)

        except Exception as e:
            print(e)


mods = ModDownload()
mods.get_page()
mods.accept_cookies()
mods.mod_download()
mods.get_mod_version_number()
mods.get_next_number()
mods.wait_for_file_and_open()
