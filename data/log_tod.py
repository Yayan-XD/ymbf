import requests, os, bs4, re, random, time, sys
from data import logo as asy
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel

### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
### WARNA MODULE RICH ###
tebal  = '[b]'
merah  = '[#FF0022]'
pink   = '[deep_pink3]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[bold cyan]'
#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    print("")
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r  {N}[{O}•{N}] {H}proses...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
# ------- ORANG GANTENG --------
def yayanxd():
    WAR = random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
    asy.henceut()
    prints(Panel(f"""[{WAR}01[/]]. Login menggunakan token
[{WAR}02[/]]. Login menggunakan cookie
[{WAR}03[/]]. Login menggunakan user dan password"""))
    p = input(f"  [{K}?{N}] pilih : ")
    if p =="":
        print(f"\n  [{M}!{N}] Jangan kosong");time.sleep(3);yayanxd()
    elif p in["1","01"]:
        login_token()
    elif p in["2","02"]:
        login_cookie()
    elif p in["3","03"]:
        login_passwod()
    else:
        print(f"\n  [{M}!{N}] input yang benar.");time.sleep(3);yayanxd()
# ------- LOGIN TOKEN --------
def login_token():
    prints(Panel("      [[green]•[/]] masukan token facebook anda [[green]•[/]]"))
    tokenz = input(f"  [{O}?{N}] token fb :{H} ")
    loading()
    try:
        nama = requests.get("https://graph.facebook.com/me?access_token="+tokenz).json()["name"]
        open('.token.txt', 'a').write(tokenz)
        prints(Panel(f"""[[green]✓[/]] selamat [green]{nama}[/] token kamu valid!
[[bold red]>[/]] gunakan dengan bijak yah tools nya!"""));time.sleep(0.3)
        exit(f"\n  [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py id")
    except requests.exceptions.ConnectionError:
        prints(Panel("😭[bold red] Tidak ada koneksi internet"));exit()
    except (KeyError,IOError,AttributeError):
        prints(Panel("😔[bold red] Token kamu invalid"));exit()
# ------- LOGIN COOKIE --------
def login_cookie():
    prints(Panel("      [[green]•[/]] masukan cookie facebook anda [[green]•[/]]"))
    cookie = input(f"  [{O}?{N}] cookie fb :{H} ")
    loading()
    try:
        tokk = requests.get("https://business.facebook.com/business_locations",headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer":"https://www.facebook.com/","host":"business.facebook.com","origin":"https://business.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        tokn = re.search("(EAAG\w+)", tokk.text).group(1)
        nama = requests.get("https://graph.facebook.com/me?access_token="+tokn).json()["name"]
        open('.cokie.txt', 'a').write(cookie)
        open('.token.txt', 'a').write(tokn)
        prints(Panel(f"""[[green]✓[/]] selamat [green]{nama}[/] cookie kamu valid!
[[bold red]>[/]] gunakan dengan bijak yah tools nya!"""));time.sleep(0.3)
        exit(f"\n  [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py id")
    except requests.exceptions.ConnectionError:
        prints(Panel("😭[bold red] Tidak ada koneksi internet"));exit()
    except (KeyError,IOError,AttributeError):
        prints(Panel("😔[bold red] Cookie kamu invalid"));exit()
# ------- MASUK PASSWORD --------
def login_passwod():
    prints(Panel("   [[green]•[/]] masukan username dan password facebook anda [[green]•[/]]"))
    session=requests.Session()
    user = input(f"  [{K}?{N}] masukan username : ")
    pasw = input(f"  [{K}?{N}] masukan password : ")
    loading()
    try:
        session=requests.Session()
        header = {"Host":"mbasic.facebook.com", "origin":"https://mbasic.facebook.com", "upgrade-insecure-requests" : "1",
        "user-agent":"Mozilla/5.0 (Linux; Android 11; Nokia 3.2) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-user": "empty","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/","accept-encoding": "gzip, deflate br","accept-language":"fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4"}
        cin = session.get("https://www.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
        das = {"lsd":re.search('name="lsd" value="(.*?)"', str(cin.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(cin.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pasw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
        yan = session.post("https://www.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header, allow_redirects = False)
        if 'c_user' in session.cookies.get_dict():
            cooz = session.cookies.get_dict()
            coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
            data = session.get("https://business.facebook.com/business_locations", headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer":"https://www.facebook.com/","host":"business.facebook.com","origin":"https://business.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":coki})
            dasw = re.search("(EAAG\w+)", data.text)
            tokn = dasw.group(1)
            nama = session.get("https://graph.facebook.com/me?access_token="+tokn).json()["name"]
            open('.cokie.txt', 'a').write(coki)
            open('.token.txt', 'a').write(tokn)
            prints(Panel(f"""[[green]✓[/]] selamat [green]{nama}[/] username dan password kamu valid!
[[bold red]>[/]] gunakan dengan bijak yah tools nya!"""));time.sleep(2)
            print(f"\n  [{M}×{N}] tunggu sebentar sedang menampilkan cookie dan token.\n");time.sleep(4)
            print(f"  [{H}✓{N}] Cookie : {H}{coki}{N}");time.sleep(2)
            print(f"  [{H}✓{N}] Token  : {H}{tokn}{N}");time.sleep(2)
            exit(f"\n  [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py id")
        elif 'checkpoint' in session.cookies.get_dict():
            prints(Panel("😔[bold red] akun terkena checkpoint"));exit()
        else:
            prints(Panel("😔[bold red] username dan password tidak benar!"));exit()
    except session.exceptions.ConnectionError:
        prints(Panel("😭[bold red] Tidak ada koneksi internet."));exit()
