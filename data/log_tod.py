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
[{WAR}02[/]]. Login menggunakan cookie"""))
    p = input(f"  [{K}?{N}] pilih : ")
    if p =="":
        print(f"\n  [{M}!{N}] Jangan kosong");time.sleep(3);yayanxd()
    elif p in["1","01"]:
        login_token()
    elif p in["2","02"]:
        login_cookie()
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
        exit(f"\n  [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py")
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
        exit(f"\n  [{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py")
    except requests.exceptions.ConnectionError:
        prints(Panel("😭[bold red] Tidak ada koneksi internet"));exit()
    except (KeyError,IOError,AttributeError):
        prints(Panel("😔[bold red] Cookie kamu invalid"));exit()
