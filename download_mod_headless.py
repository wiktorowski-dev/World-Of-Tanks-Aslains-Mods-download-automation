from bs4 import BeautifulSoup as bs
import requests, re
import time


start_time = time.time()

url = 'https://aslain.com/index.php?/topic/13-download-%E2%98%85-world-of-tanks-%E2%98%85-modpack/'
# headers = {
#             'content-type' : 'application/octet-stream',}
r = requests.get(url)

soup = bs(r.text, 'lxml')


installator_links = []

for link in soup.find_all('a', href=re.compile('.*Aslains_WoT_Modpack_Installer.*')):
    print(link['href'])
    installator_links.append(link['href'])

exe_file = requests.get(installator_links[1])
print("--- %s seconds ---" % (time.time() - start_time))
with open('Aslain_mod.exe', 'wb') as file:

    file.write(exe_file.content)




