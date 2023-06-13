import socket
import os
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.50.164"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
# client.connect((socket.gethostname(),1234))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

print("Enter Your Name : ")
client_message = input()
send(client_message)

while True:
    print("Hukum Koren Badshah : ")
    client_message = input()
    if client_message == "Kaaj Shesh":
        break

    if client_message == "ClearClient":
        os.system("cls")
    if client_message == "FeelHacked":
        os.system("Color 0a")

    if client_message == "health_write":
        print("Height : ")
        h = input()
        print("Weight : ")
        w = input()
        print("Speed : ")
        s = input()
        file = open('health.txt', 'w')
        file.write(f"Height {h} "f" Weight {w} "f" Speed {s}")
        file.close()

    send(client_message)

# send("Hello from Mehrab Server OS")
# x = input()
#
# y = input()
# send(y)

send(DISCONNECT_MESSAGE)
