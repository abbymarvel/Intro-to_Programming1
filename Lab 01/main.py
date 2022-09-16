#Menghitung Luas Cat Logo Pak Chanek
#Abby Marvel Immanuel Parasian Pribadi
#NPM: 2106751796
import math

#assign input
r = float(input("Masukkan radius lingkaran: "))
tinggi_segitiga = r
alas_segitiga = r * 2
sisi_persegi = r * 2


#Menghitung luas segitiga berwarna ungu
luas_cat_ungu = (tinggi_segitiga * alas_segitiga) / 2

#Menghitung luas ingkaran berwarna kuning
luas_cat_kuning = (math.pi * r**2) - luas_cat_ungu

#Menghitung luas kotak berwarna merah
luas_cat_merah = (sisi_persegi ** 2) - (luas_cat_kuning + luas_cat_ungu)

#saya memakai "{:.2f}".format(float) agar hanya dua angka setelah desimal yang tercetak
print("Luas daerah cat merah: " "{:.2f}".format(luas_cat_merah))
print("Luas daerah cat merah: " "{:.2f}".format(luas_cat_kuning))
print("Luas daerah cat merah: " "{:.2f}".format(luas_cat_ungu))

