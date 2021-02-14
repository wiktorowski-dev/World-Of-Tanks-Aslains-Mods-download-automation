from __future__ import print_function

import os
import sys
import re
import time

from pywinauto import Application
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))


class ModDownload:
    app = Application(backend='win32')

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=selenium")

        self.browser = webdriver.Chrome(options=chrome_options)


    def get_page(self):
        url = 'https://aslain.com/index.php?/topic/13-download-%E2%98%85-world-of-tanks-%E2%98%85-modpack/'
        print("***Getting URL***")

        self.browser.get(url)
        time.sleep(0.5)

    def accept_cookies(self):
        self.accept = self.browser.find_elements_by_xpath('//*[@id="elGuestTerms"]/div/div/div[2]/a')[0]
        self.accept.click()

    def mod_download(self):
        download_href_1 = '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[9]/span/a'
        download_href_2 = '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[10]/span/a'
        download_href_3 = '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[11]/span[3]/a'

        while True:

            try:
                print("***Attempt to download link ...")
                self.direct = self.browser.find_elements_by_xpath(download_href_1)[0]
                break
            except Exception as e:
                print("***Invalid link!*** ", e)

            try:
                print("***Attempt to download next link ...")
                self.direct = self.browser.find_elements_by_xpath(download_href_2)[0]
                break
            except Exception as e:
                print("***Invalid link!*** ", e)

            try:
                print("***Attempt to download next link ...")
                self.direct = self.browser.find_elements_by_xpath(download_href_3)[0]
                break
            except Exception as e:
                print("***Invalid link!*** ", e)
                break

        self.direct.click()
        print("***Aslain's Mods Downloading***")

    def get_mod_version_number(self):
        self.version = self.browser.find_elements_by_xpath(
            '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[7]/span[1]/span/strong')

        ver_data = []

        for value in self.version:
            ver_data.append(value.text)

        text = ver_data[0]

        m = re.search('ModPack v(.+?) ', text)
        if m:
            version_num = m.group(1)
        return version_num

    def get_next_number(self):
        self.number = self.browser.find_elements_by_xpath(
            '//*[@id="comment-13_wrap"]/div[2]/div[1]/p[7]/span[2]/span/strong')

        num_data = []

        for value in self.number:
            num_data.append(value.text)
            value.text.replace('#', '_')

        number = num_data[0].replace('#', '_')

        return number

    # Open file from \Downloads path
    def open_and_connect_dialog(self, app):
        downloads_path = r"C:\Users\dklec\Downloads"
        file_name = "Aslains_WoT_Modpack_Installer_v." + self.get_mod_version_number() + self.get_next_number() + ".exe"

        full_file_path = downloads_path + '\\' + file_name

        # Wait when file will be visible
        while not os.path.exists(full_file_path):
            time.sleep(3.0)
            print("***File not found, retry ...")

        try:
            print("***File was found! Opening ...")
        except Exception as e:
            print(e)

        # Close browser, no need anymore
        time.sleep(1.0)
        webdriver.Chrome.quit(self.browser)

        # Open and connect file path
        app.start(full_file_path)
        app.connect(path=file_name)

    def dialog_click_next(self, app):

        try:
            for i in range(0, 9):
                if i == 0:
                    time.sleep(0.1)
                    app.connect(title='Język instalacji')
                    app.window(title='Język instalacji').wait('ready', timeout=5.0, retry_interval=0.1)

                    dlg = app.window(title='Język instalacji')
                    dlg.child_window(title='OK', class_name='TNewButton').click()

                    print("***Button 'OK' was clicked ...")
                    time.sleep(0.5)
                    print("***Waiting for Installer Setup Dialog ...")

                if i == 1:
                    time.sleep(0.1)
                    # time.sleep(20.0)
                    while True:
                        try:
                            app.connect(title_re=".*Welcome.*")
                            print('***Connected***')
                            break
                        except Exception:
                            time.sleep(1.0)
                            print('***')
                            continue

                    dlg = app.window(title_re=".*Welcome.*")
                    dlg.child_window(title='Dalej >', class_name='TNewButton').click()

                    print("*** ", i, " dialog clicked ...")

                if i == 2:
                    time.sleep(0.1)
                    app.connect(title_re=".*Read-Me.*")
                    dlg = app.window(title_re=".*Read-Me.*")
                    dlg.child_window(title='Dalej >', class_name='TNewButton').click()

                    print("*** ", i, " dialog clicked ...")

                if i == 3:
                    time.sleep(0.1)
                    app.connect(title_re=".*Change-Log.*")
                    dlg = app.window(title_re=".*Change-Log.*")
                    dlg.child_window(title='Dalej >', class_name='TNewButton').click()

                    print("*** ", i, " dialog clicked ...")

                if i == 4:
                    time.sleep(0.1)
                    app.connect(title_re=".*Directory Selection.*")
                    dlg = app.window(title_re=".*Directory Selection.*")
                    dlg.child_window(title='Dalej >', class_name='TNewButton').click()

                    print("*** ", i, " dialog clicked ...")

                if i == 5:
                    time.sleep(1.5)

                    app.connect(title_re=".*Mod Selection.*")
                    dlg = app.window(title_re=".*Mod Selection.*")
                    dlg.child_window(title='Dalej >', class_name='TNewButton').click()

                    print("*** ", i, " dialog clicked ...")

                if i == 6:
                    time.sleep(0.1)
                    app.connect(title_re=".*Task Selection.*")
                    dlg = app.window(title_re=".*Task Selection.*")
                    dlg.child_window(title='Dalej >', class_name='TNewButton').click()

                    print("*** ", i, " dialog clicked ...")

                if i == 7:
                    time.sleep(0.1)
                    app.connect(title_re=".*Ready Page.*")
                    dlg = app.window(title_re=".*Ready Page.*")
                    dlg.child_window(title='&Instaluj', class_name='TNewButton').click()

                    print("*** ", i, " dialog clicked ...")

                if i == 8:
                    while True:
                        try:
                            app.connect(title_re=".*Finished Page.*")
                            print('***Connected***')
                            break
                        except Exception:
                            time.sleep(1.0)
                            print('***')
                            continue

                    dlg = app.window(title_re=".*Finished Page.*")
                    dlg.child_window(title='&Zakończ', class_name='TNewButton').click()

                    print("*** ", i, " dialog clicked ...")

        except Exception as e:
            print(e)

        print("***Mods instalation complete***")


mods = ModDownload()
mods.get_page()
mods.accept_cookies()
mods.mod_download()
mods.get_mod_version_number()
mods.get_next_number()
mods.open_and_connect_dialog(ModDownload.app)
mods.dialog_click_next(ModDownload.app)
