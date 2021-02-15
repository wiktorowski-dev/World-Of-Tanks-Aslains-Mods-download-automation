from __future__ import print_function

import os
import sys
import re
import time

from pywinauto import Application
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))


def wait_for_dialog(app, pages_names, page_num):
    while True:
        try:
            app.connect(title_re=pages_names[page_num])
            break
        except Exception:
            time.sleep(1.0)
            print('*')
            continue


def click_next_button(app, pages_names, num):
    app.connect(title_re=pages_names[num])
    dlg = app.window(title_re=pages_names[num])
    dlg.child_window(title='Dalej >', class_name='TNewButton').click()


class ModDownload:
    app = Application(backend='win32')

    pages_names = ["Język instalacji", ".*Welcome.*", ".*Read-Me.*", ".*Change-Log.*", ".*Directory Selection.*",
                   ".*Mod Selection.*", ".*Task Selection.*", ".*Ready Page.*", ".*Finished Page.*"]

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

    def dialog_click_next(self, app, pages_names):

        try:
            for i in range(len(pages_names)):

                if i == 0:
                    time.sleep(0.5)
                    app.connect(title=pages_names[0])
                    app.window(title=pages_names[0]).wait('ready', timeout=5.0, retry_interval=0.1)

                    dlg = app.window(title=pages_names[0])
                    dlg.child_window(title='OK', class_name='TNewButton').click()

                    time.sleep(0.5)
                    print("***Waiting for Installer Setup Dialog ...")

                if i == 1:
                    time.sleep(0.1)
                    wait_for_dialog(app, pages_names, 1)

                    click_next_button(app, pages_names, 1)

                if i == 2:
                    time.sleep(0.1)
                    click_next_button(app, pages_names, 2)

                if i == 3:
                    time.sleep(0.1)
                    click_next_button(app, pages_names, 3)

                if i == 4:
                    time.sleep(0.1)
                    click_next_button(app, pages_names, 4)

                if i == 5:
                    time.sleep(1.5)
                    click_next_button(app, pages_names, 5)

                if i == 6:
                    time.sleep(0.1)
                    click_next_button(app, pages_names, 6)

                if i == 7:
                    time.sleep(0.1)
                    dlg = app.window(title_re=pages_names[7])
                    dlg.child_window(title='&Instaluj', class_name='TNewButton').click()

                if i == 8:
                    wait_for_dialog(app, pages_names, 8)

                    dlg = app.window(title_re=pages_names[8])
                    dlg.child_window(title='&Zakończ', class_name='TNewButton').click()

        except Exception as e:
            print(e)


mods = ModDownload()
mods.get_page()
mods.accept_cookies()
mods.mod_download()
mods.get_mod_version_number()
mods.get_next_number()
mods.open_and_connect_dialog(ModDownload.app)
mods.dialog_click_next(ModDownload.app, ModDownload.pages_names)
