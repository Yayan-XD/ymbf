#Ngapain bro Mau recode?
#Mikir dong goblok Lo pikir gampang buat script

import requests as r

from rich.panel import Panel
from rich import print as prints

from src import loz as qq
from data import logo as asy

def cek_server():
    asy.henceut()
    try:
        req = r.get("https://pastebin.com/raw/2hKSXLwD").text
        if "tidak" in req:
            qq.moch_yayan()
        elif "error" in req:
            prints(Panel("""mohon maaf kepada user brute, script sedang bermasalah. tunggu beberapa saat waktu admin sedang berusaha memperbaiki nya 😉
untuk mendapatkan info selanjutnya kunjungi situs web ini:[green] https://www.yayanxd.my.id[/] lalu klik ikon [green]WhatsApp[/]""",title="BERMASALAH"));exit()
        else:
            prints(Panel("[bold red]gagal menghubungkan ke server[/]"))
    except r.exceptions.ConnectionError:
        print("");prints(Panel("😔[bold red] gagal menghubungkan ke server, silahkan cek koneksi anda dan mainkan mode pesawat 5 detik."));exit()
