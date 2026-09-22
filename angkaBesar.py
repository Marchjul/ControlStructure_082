angka1 = int(input("Masukan Angka Pertama : "))
angka2 = int(input("Masukan Angka Kedua : "))
angka3 = int(input("Masukan Angka Ketiga : "))

if angka1 > angka2 and angka1 > angka3:
    terbesar = angka1
    print("Angka Terbesar adalah : ", terbesar)
elif angka2 > angka1 and angka2 > angka3:
    terbesar = angka2
    print("Angka Terbesar adalah : ", terbesar)
elif angka3 > angka1 and angka3 > angka2:
    terbesar = angka3
    print("Angka Terbesar adalah : ", terbesar)
else:
    print("Tidak ada angka terbesar")