import requests
from colorama import Fore, Back, Style

print(Fore.RED + "----------------------------")
print(Fore.YELLOW + "github.com/TalhaDevv")
print(Fore.RED + "----------------------------")
# Hangi kullanıcının projeleri listelenicekse onun adını input ile alıyoruz
github_username = input(Fore.GREEN + "Github Kullanıcı Adı: " + Style.RESET_ALL)
print(Fore.BLUE + github_username + "`in Projeleri")
print(Fore.YELLOW + "----------------------------")
# Githubun kendi api bağlantısı, kullanıcının ismini {} içinde belirtip projelerine bakıyoruz
api_url = f"https://api.github.com/users/{github_username}/repos"

# GET isteği ile üst tarafta ayaraldığımız api_url yi alıyoruz.
response = requests.get(api_url)

# Başarılı olma durumunda proje isimlerini yazıcak kod.
if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(Fore.RED + repo['name'])
else:
    print("İstek başarısız oldu.")

input()
