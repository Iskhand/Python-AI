import math


def awal():
    a = float(input('masukkan angka:'))
    b = input("masukkan : ")
    c = float(input('masukkan angka:'))

    if (b == "tambah"):
        h = a + c
        print(h)
    elif (b == "kurang"):
        h = a - c
        print(h)
    elif (b == "bagi"):
        h = a / c
        print(h)
    elif (b == "kali"):
        h = a * c
        print(h)
    else:
        print("mohon masukkan dengan benar")
    return awal()


awal()
