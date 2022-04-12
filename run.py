#Hallo anak anjing:v

if __name__ == "__main__":
   try:
       __import__("src/cok").cek_server()
   except Exception as e:
       exit(str(e))
