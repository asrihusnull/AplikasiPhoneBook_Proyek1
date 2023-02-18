"""Program Phone Book"""

kontak = {}

import json

def buatKontak(nama, nomor):
    kontak[nama] = nomor
    file = open("bukuKontak.txt", "a")
    file.write(nama)
    file.write(" : ")
    file.write(nomor)
    file.write("\n")

def perbaruiKontak():
    nama = input("Nama: ")
    if nama not in kontak:
        print("Kontak tidak ada.")
        return
    nomor = input("Nomor Telepon: ")
    kontak[nama] = nomor
    with open("bukuKontak.txt", "r") as file:
        lines = file.readlines()
    with open("bukuKontak.txt", "w") as file:
        for line in lines:
            if line.startswith(nama):
                line = f"{nama} : {nomor}\n"
            file.write(line)
    print("Kontak berhasil diperbarui!")


def hapusKontak(nama):
    file = open("bukuKontak.txt", "r")
    save = {}
    i = 0
    data = file.readline()
    datanama = data.split(" : ")
    while data:
        if datanama[0] == nama:
            del (data)
        else:
            save[i] = data
            i = i + 1
        data = file.readline()
        datanama = data.split(" : ")
    file.close
    file = open("bukuKontak.txt", "w")
    for x in save:
        file.write(save[x])
    file.close

def lihatKontak():
    file = open("bukuKontak.txt")
    file.seek(0)
    lines = file.readlines()
    for line in lines:
        print(line)

def cariKontak(nama):
    file = open("bukuKontak.txt", "r")
    data = file.readline()
    datanama = data.split(" : ")
    ketemu = False
    while data and ketemu == False:
        if datanama[0] == nama:
            print(data)
            ketemu = True
        else:
            data = file.readline()
            datanama = data.split(" : ")
    if(ketemu == False):
        print("Kontak tidak ada.")
    file.close
    
with open("bukuKontak.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            nama, nomor = line.split(" : ")
            kontak[nama] = nomor

            
"""Main Program"""

while True:
    print("\n- MENU PHONE BOOK -")
    print("1. Buat Kontak Baru")
    print("2. Perbarui Kontak")
    print("3. Hapus Kontak")
    print("4. Lihat Semua Kontak")
    print("5. Cari Kontak")
    print("6. Keluar")

    pilih = int(input("\nMasukkan pilihan : "))

    if pilih == 1:
        nama = input("Nama : ")
        nomor = input("Nomor telepon : ")
        buatKontak(nama, nomor)

    elif pilih == 2:
        perbaruiKontak()

    elif pilih == 3:
        nama = input("Nama : ")
        hapusKontak(nama)

    elif pilih == 4:
        lihatKontak()

    elif pilih == 5:
        nama = input("Nama : ")
        cariKontak(nama)

    elif pilih == 6:
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")

print("Selesai!")
