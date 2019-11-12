#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018r

import threading
import socket
import sys
import time
import platform

host = ''
port = 9000
locaddr = (host, port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)
##tello_address = ('127.0.0.1', 6789)
sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\nUscita dal programma . . .\n')
            break


print('\r\n\r\nTello ITC CHIRONI.\r\n')

print('Comandi Tello: takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print('end -- esce dal programma.\r\n')

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True:
    try:
        python_version = str(platform.python_version())
        version_init_num = int(python_version.partition('.')[0])
        # print (version_init_num)
        if version_init_num == 3:
            msg = input("");
        elif version_init_num == 2:
            msg = raw_input("");

        if not msg:
            msg = "battery?"
            break

        if 'end' in msg:
            print('...')
            sock.close()
            break

        # Send data
        print("Eseguo "+msg+"\n")
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print('\n . . .\n')
        sock.close()
        break
