from datetime import *

def getLate(hariKembali) :
    hariIni     = datetime.date(datetime.now())
    hariKembali = datetime.strptime(hariKembali, "%Y-%m-%d").date()
    return int((hariIni - hariKembali).days)

file = open("dataMember.txt", "r")

isiFile = file.readlines()
kode    = input("Masukkan Kode Member      : ")

for i in range(len(isiFile)) :   
    if(kode in isiFile[i]) :
        diSplit = isiFile[i].split('|')
        status  = 'Ada'
        break
    else :
        status = 'Tidak ada'
        continue
if(status == 'Ada') :   
    maksPinjam = diSplit[4].rstrip('\n')
    pinjaman = getLate(maksPinjam)
    if(pinjaman <= 0) :      
        keterlambatan      = "Tidak Terlambat"
        denda         = "Tidak Ada Denda"     
    elif(pinjaman > 0) :   
        keterlambatan      = str(pinjaman) + " hari"
        denda         = "Rp " + str(pinjaman*2000)
    print("\nData Peminjaman Buku")
    print("Kode Member              : ", diSplit[0])
    print("Nama Member              : ", diSplit[1])
    print("Judul Buku               : ", diSplit[2])
    print("Tanggal Mulai Peminjaman : ", diSplit[3])
    print("Tanggal Maks Peminjaman  : ", maksPinjam)
    print("Tanggal Pengembalian     : ", datetime.date(datetime.now()))
    print("Terlambat                : ", keterlambatan)
    print("Denda                    : ", denda)
