from bs4 import BeautifulSoup as bs
import requests, re


class ModDownload:

    def __init__(self):
        url = 'https://aslain.com/index.php?/topic/13-download-%E2%98%85-world-of-tanks-%E2%98%85-modpack/'

        self.r = requests.get(url)
        self.store = self.store_data()

    def store_data(self):
        soup = bs(self.r.text, 'lxml')
        installer_links = []

        # TODO przeanalizowac linki, dac inny regex.compile
        for link in soup.find_all('a', href=re.compile('.*Aslains_WoT_Modpack_Installer.*')):
            print(link['href'])
            installer_links.append(link['href'])

        # TODO przerobic tak by nie pisac installer_links[1], zrobic dictionary
        while True:
            try:
                target_file = requests.get(installer_links[1])
                break
            except Exception as e:
                print("***Invalid Link!***", e)

            try:
                target_file = requests.get(installer_links[0])
                break
            except Exception as e:
                print("***Invalid Link!***", e)

            try:
                target_file = requests.get(installer_links[2])
                break
            except Exception as e:
                print("***Invalid Link!***", e)

            try:
                target_file = requests.get(installer_links[3])
                break
            except Exception as e:
                print("***Invalid Link!***", e)

        # Writing file in project folder
        with open('Aslain_mod.exe', 'wb') as f:

            f.write(target_file.content)
            return f


