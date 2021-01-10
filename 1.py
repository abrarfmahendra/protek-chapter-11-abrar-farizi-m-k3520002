from datetime import *


def diffDate(x) :
    tanggal = x.split("-")
    dateList = []

    for i in tanggal :
        dateList.append(int(i))
    yesterday = date(dateList[0], dateList[1], dateList[2])
    today = datetime.date(datetime.now())
    delta = yesterday - today
    result = delta.days
    return result

try :
    tgl = input("Masukkan tanggal dengan format (yyyy-mm-dd) : ")
    hasil = diffDate(tgl)
    print("Selisih tanggal {0} dengan hari ini : {1} hari".format(tgl, hasil))
except ValueError :
    print("Masukkan tanggal yang valid")
