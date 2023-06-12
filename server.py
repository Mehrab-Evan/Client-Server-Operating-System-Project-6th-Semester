# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# s.bind((socket.gethostname(), 1234))
#
# s.listen(5)
#
# while True :
#     clientsocket, address = s.accept()
#     print(f"Connection {address} Stublished")
#     clientsocket.send(bytes("Welcome to Final_Server", "utf-8"))


import socket
import threading
import sys
import os

HEADER = 64
PORT = 5050
SERVER = "192.168.50.164"
#SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    x = 0
    connected = True
    g = ""
    while connected:
        print(f"Top G {g} is Connected")
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if x == 0:
                g = msg
                conn.send(f"Welcome : {msg}".encode(FORMAT))
                x = 1
                continue

            conn.send(f"You : {msg}".encode(FORMAT))

            if msg == DISCONNECT_MESSAGE:
                connected = False
            if msg == "health_read":
                file = open('health.txt', 'r')
                lines = file.readlines()
                conn.send(f"{lines}\n".encode(FORMAT))
                for line in file:
                    print(line.strip())
                file.close()

            if msg == "OPfacebookMehrab":
                url = "https://www.facebook.com/mehrab.evan"
                os.system(f"start {url}")
            if msg == "OPfacebookTaivan":
                url = "https://www.facebook.com/ddipto10"
                os.system(f"start {url}")
            if msg == "OPfacebookTareq":
                url = "https://www.facebook.com/rajbinrobin"
                os.system(f"start {url}")
            if msg == "OPGC":
                url = "https://classroom.google.com/h"
                os.system(f"start {url}")
            if msg == "OPfacebookGM":
                url = "https://www.facebook.com/shaown.arafat"
                os.system(f"start {url}")
            if msg == "Notepad":
                os.system("start notepad")
            if msg == "Word":
                os.system("start winword")
            if msg == "OSsheet":
                url = "https://drive.google.com/file/d/14N7WdoTmvX_5-wAQAD5SIKAmUnopkJD1/view?usp=sharing"
                os.system(f"start {url}")
            if msg == "Met":
                url = "https://www.accuweather.com/en/bd/chittagong/27822/weather-forecast/27822"
                os.system(f"start {url}")
            if msg == "Shutdown":
                os.system("shutdown /s /t 2")

            if msg == "help":
                print("OSsheet : Will have the Operating system Sheet")
                print("Word : Open MS Word")
                print("Notepad : Open NotePad")
                print("OPGC : Open Google Class Room")
                print("OPfacebookGM : Shawon Sir Facebook")
                print("OPfacebookMehrab : Mehrab Evan Facebook")
                print("OPfacebookTaivan : Taivan Reza Facebook")
                print("OPfacebookTareq : Tareq Robin Facebook")
                print("Shutdown : Shutdown the PC")
                print("Met : Weather")
                print("health_write : TO write about your health")
                print("health_read : TO read about your health")
                conn.send("OSsheet : Will have the Operating system Sheet\n".encode(FORMAT))
                conn.send("Word : Open MS Word\n".encode(FORMAT))
                conn.send("Notepad : Open NotePad\n".encode(FORMAT))
                conn.send("OPGC : Open Google Class Room\n".encode(FORMAT))
                conn.send("OPfacebookGM : Shawon Sir Facebook\n".encode(FORMAT))
                conn.send("OPfacebookMehrab : Mehrab Evan Facebook\n".encode(FORMAT))
                conn.send("OPfacebookTaivan : Taivan Reza Facebook\n".encode(FORMAT))
                conn.send("OPfacebookTareq : Tareq Robin Facebook\n".encode(FORMAT))
                conn.send("Shutdown : Shutdown the PC\n".encode(FORMAT))
                conn.send("Met : Weather\n".encode(FORMAT))
                conn.send("health_write : TO write about your health\n".encode(FORMAT))
                conn.send("health_read : TO read about your health\n".encode(FORMAT))
                # conn.send("Server : ARE YOU SURE? Y/N".encode(FORMAT))
                # url = "https://www.facebook.com/shaown.arafat"
                # msg_length = conn.recv(HEADER).decode(FORMAT)
                # if msg_length:
                #     msg_length = int(msg_length)
                #     msg = conn.recv(msg_length).decode(FORMAT)
                #     if msg == "Y" or msg == "y":
                #         os.system(f"start {url}")
                #     else :
                #         conn.send("GOOD CHOICE".encode(FORMAT))
            else :
                print("Kono Command Detect korte parlam na")
            # if msg == "MEHRAB":
            #     # print("MEHRAAAAAAAAAAAAAB")
            #     # print(f"[{addr}] {msg}")
            #     conn.send("Msg MEHRAB".encode(FORMAT))

            # print(f"[{addr}] {msg}")
            # conn.send("Msg received".encode(FORMAT))
    #         print("WHY MEE")
    # print("WHY")
    conn.close()
    # sys.exit()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()