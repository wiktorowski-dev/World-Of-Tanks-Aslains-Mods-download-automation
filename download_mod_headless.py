from bs4 import BeautifulSoup as bs
import requests, re


class ModDownload:

    def __init__(self):
        url = 'https://aslain.com/index.php?/topic/13-download-%E2%98%85-world-of-tanks-%E2%98%85-modpack/'

        self.r = requests.get(url)
        self.store = self.store_data()

    def store_data(self):
        soup = bs(self.r.text, 'lxml')
        installer_links = {}

        # Get all links with specified re.compile
        num_links = 0
        for link in soup.find_all('a', href=re.compile('.*Aslains_WoT_Modpack_Installer.*')):
            installer_links[f'link {num_links}'] = link['href']
            num_links += 1

        # Its necessary to pop this link cause its .exe.torrent,
        # user in that case need qBittorrent app to open that link
        installer_links.pop('link 0')
        print(installer_links)

        # Writing file in project folder
        with open('Aslain_mod.exe', 'wb') as f:
            print('***Download has started ...')

            # From some reasons other links are invalid, don't have .content
            target_file = requests.get(installer_links['link 1'])

            # serv
            print(target_file.headers)
            # user
            print(target_file.request.headers)

            print('***Saving into file...')
            f.write(target_file.content)

            return f

# For tests only
#
# download = ModDownload()
# download.store_data()
