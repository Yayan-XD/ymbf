#Hallo anak anjing:v
import os

if __name__ == "__main__":
   try:
       os.system("git pull");os.system("rm -rf results/CP/...");os.system("rm -rf results/OK/...")
       __import__("c").cek_server()
   except Exception as e:
       exit(str(e))
