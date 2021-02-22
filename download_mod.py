# from __future__ import print_function

import os, sys, time, download_mod_headless

from pywinauto import Application

# TODO po chuj to tu jest, ogarnac i wywalic if not necessary
os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))


# Custom "wait"
def wait_for_dialog(app, pages_names, page_num):
    while True:
        try:
            app.connect(title_re=pages_names[page_num])
            break
        except Exception:
            time.sleep(1.0)
            print('Waiting ...')
            continue


# Navigation through installer dialogs
def click_next_button(app, pages_names, num):
    app.connect(title_re=pages_names[num])
    dlg = app.window(title_re=pages_names[num])
    dlg.child_window(title='Dalej >', class_name='TNewButton').click()
    time.sleep(0.1)


class ModInstall:
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
        """ Mod downloading headless, store in Project Folder as .exe"""
        download_mod_headless.ModDownload()

    # Installing downloaded mods
    def open_and_connect_dialog(self, app):
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

    def dialog_click_next(self, app, pages_names):

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
                wait_for_dialog(app, pages_names, 1), click_next_button(app, pages_names, 1)

            if i == 2:
                click_next_button(app, pages_names, 2)

            if i == 3:
                click_next_button(app, pages_names, 3)

            if i == 4:
                click_next_button(app, pages_names, 4)

            if i == 5:
                time.sleep(1.5)
                click_next_button(app, pages_names, 5)

            if i == 6:
                click_next_button(app, pages_names, 6)

            if i == 7:
                time.sleep(0.1)
                dlg = app.window(title_re=pages_names[7])
                dlg.child_window(title='&Instaluj', class_name='TNewButton').click()

            if i == 8:
                wait_for_dialog(app, pages_names, 8)

                dlg = app.window(title_re=pages_names[8])
                dlg.child_window(title='&Zakończ', class_name='TNewButton').click()


install = ModInstall()
install.open_and_connect_dialog(ModInstall.app)
install.dialog_click_next(ModInstall.app, ModInstall.pages_names)
