# Apalo ajg

import sys, os
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel

bir = '[bold cyan]'
hps = '[/]'
# ------- UNTUK MENGHAPUS TEKS --------
def hapus_teks():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass
# ------- LOGO --------
def henceut():
    hapus_teks()
    prints(Panel(f"""{bir} __  __        __  ______  ____{hps}
{bir} \ \/ / ____  /  |/  / _ )/ __/ ® {hps}|| Created By YayanXD
{bir}  \  / /___/ / /|_/ / _  / _/     {hps}|| Github.com/Yayan-XD
{bir}  /_/       /_/  /_/____/_/ v3.0  {hps}|| Facebook.com/KM39453"""))
