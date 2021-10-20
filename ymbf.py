import os, sys, time

O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

def donasi():
    os.system("clear")
    print("""%s
    ___  ____ _  _ ____ ____ _    
    |  \ |  | |\ | |__| [__  |    
    |__/ |__| | \| |  | ___] |    """%(O))
    jalan("\n%s Yo hallo penggunaan setia script ymbf"%(K));time.sleep(2)
    jalan(" Ikan hiu makan bapaknya cecep");time.sleep(3)
    jalan(" Cakep...");time.sleep(2)
    jalan(" Bantu donasi dong cep:)");time.sleep(2)
    jalan(" Dengan membelikan secangkir kopi untuk menemani coding di malam hari 🗿\n")
    raw_input(' %s[%s Tekan enter%s ] '%(N,H,N));os.system('xdg-open https://saweria.co/YayanXD')
    os.system("clear")
    jalan("\n Mohon maaf script tidak bisa di jalankan sekarang")
    jalan("\n Tunggu beberapa hari untuk mendapatkan update terbaru")


if __name__ == '__main__':
    os.system('git pull')
    donasi()
