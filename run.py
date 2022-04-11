import os
from src import cok as x

if __name__ == "__main__":
    os.system("git pull");os.system("rm -rf results/OK/...");os.system("rm -rf results/CP/...")
    x.cek_server()
