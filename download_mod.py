import download_mod_headless
import os
import sys
import time

from pywinauto import Application

# TODO po chuj to tu jest, ogarnac i wywalic if not necessary
os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))


class ModInstall(object):
    app = Application(backend='win32')

    # Installer Dialog re page names
    pages_names = ["Język instalacji",
                   ".*Welcome.*",
                   ".*Read-Me.*",
                   ".*Change-Log.*",
                   ".*Directory Selection.*",
                   ".*Mod Selection.*",
                   ".*Task Selection.*",
                   ".*Ready Page.*",
                   ".*Finished Page.*"]

    def __init__(self):
        super(ModInstall, self).__init__()
        """ Mod downloading headless, store in Project Folder as .exe"""
        download_mod_headless.ModDownload()

    # Installing downloaded mods
    @staticmethod
    def open_and_connect_dialog(app):
        # todo SEPARATE PATH TO EXTERNAL FILE
        downloads_path = r"C:\Users\dklec\PycharmProjects\wot_mod_automatization"
        file_name = "Aslain_mod.exe"

        full_file_path = downloads_path + '\\' + file_name
        print(full_file_path)

        # Wait when file will be visible
        while not os.path.exists(full_file_path):
            time.sleep(3.0)
            print("***File not found, retry ...")

        print("***File was found! Opening ...")

        # Open and connect file path
        app.start(full_file_path)
        app.connect(path=file_name)

    # Navigation through installer dialogs
    @staticmethod
    def click_next_button(app, page_name):
        app.connect(title_re=page_name)
        dlg = app.window(title_re=page_name)
        dlg.child_window(title='Dalej >', class_name='TNewButton').click()
        time.sleep(0.1)

    # Custom "wait"
    @staticmethod
    def wait_for_dialog(app, page_name):
        # Infinite loop, what if the script will never connect? Make some raise exception if too many attempts
        i = 0
        while True:
            try:
                app.connect(title_re=page_name)
                break
            except Exception:
                i += 1
                time.sleep(1.0)
                print('Waiting ...')

            i += 1
            if i > 10:
                raise Exception("Couldn't connect in wait_for_dialog")

    def dialog_click_next(self, app, pages_names):

        for i in range(len(pages_names)):

            if i == 0:
                time.sleep(0.5)
                app.connect(title=pages_names[i])
                app.window(title=pages_names[i]).wait('ready', timeout=5.0, retry_interval=0.1)

                dlg = app.window(title=pages_names[i])
                dlg.child_window(title='OK', class_name='TNewButton').click()

                time.sleep(0.5)
                print("***Waiting for Installer Setup Dialog ...")

            if 1 < i < 7:
                self.__base_click_button(app, pages_names, i)

            if i == 1:
                # This micro delays are necessary?
                time.sleep(0.1)
                self.wait_for_dialog(app, pages_names[i])
                self.click_next_button(app, pages_names[i])

            if i == 7:
                time.sleep(0.1)
                dlg = app.window(title_re=pages_names[i])
                dlg.child_window(title='&Instaluj', class_name='TNewButton').click()

            if i == 8:
                self.wait_for_dialog(app, pages_names[i])

                dlg = app.window(title_re=pages_names[8])
                dlg.child_window(title='&Zakończ', class_name='TNewButton').click()

    def __base_click_button(self, app, pages_names, i):
        time.sleep(1)
        self.click_next_button(app, pages_names[i])


if __name__ == '__main__':
    install = ModInstall()
    install.open_and_connect_dialog(ModInstall.app)
    install.dialog_click_next(ModInstall.app, ModInstall.pages_names)
