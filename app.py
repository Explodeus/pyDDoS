import sys
import os
import time
import socket
import random

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
port = input("Port      : ")