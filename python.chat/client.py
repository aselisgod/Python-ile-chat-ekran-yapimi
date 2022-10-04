import socket
import time

host_adı = "localhost"
port = 7777

internet_soketi = socket.socket()
internet_soketi.connect((host_adı,port))

print("Bağlantı sağlandı!! {}:{}".format(host_adı , port))

mesaj = input("---::")
print("Server Bekleniyor...")

while mesaj !="cikis":
    internet_soketi.send(mesaj.encode())
    gelen_veri = internet_soketi.recv(1024).decode
    
    print("SERVER :"+ gelen_veri)
    
    mesaj = input("---::")
    print("Server Bekleniyor...")
    
internet_soketi.close