#Hallo anak anjing:v

if __name__ == "__main__":
   try:
       __import__("cok").cek_server()
   except Exception as e:
       exit(str(e))
