import socket
import time

host_adı = "localhost"
port = 7777

internet_soketi = socket.socket()
internet_soketi.bind((host_adı,port))
internet_soketi.listen(1)

baglanti , adres = internet_soketi.accept()

print(str(adres)+"Bağlantı Oluşturuldu")

while True:
    while True:
        try:
            gelen_veri = str(baglanti.recv(1024).decode())
            print("client şu mesajı yolladı :"+ gelen_veri)
            break
        except ConnectionResetError:
            time.sleep(2)
            baglanti , adres = internet_soketi.accept()
            print(str(adres)+"Bağlantı Sağlandı")
        if gelen_veri == "cikis":
            break
        else:
            mesaj= input("---::")
            print("Clint bekleniyor...")
            baglanti.send(mesaj.encode())
baglanti.close()