print("Selamat datang di Kalkulator IPK!")
#saya menggunakan while true untuk memastikan jumlah mata kuliah tidak negatif
while True:
  try:
    jumlah = (input("Masukkan jumlah mata kuliah: "))
    if int(jumlah) > 0:
      break
  except Exception as e:
    print(jumlah)
print()

#saya menggunakan dictionary untuk menyimpan input dari while loop yang saya gunakan di bawah
names = []
credits = []
scores = []
pass_credits = []
qualities = []
pass_qualities= []
weight = []
pass_weight = []

#saya menggunakan number sebagai acuan berapa banyak while loop akan looping
number = 0
while number < int(jumlah) :
    number += 1

    nama = input("Masukkan nama mata kuliah ke-" + str(number) + ": " )
    names.append(nama)

    sks = float(input("Masukkan jumlah SKS " + nama + ": "))
    credits.append(sks)

    while True:
        try:
            nilai = input("Masukkan nilai yang kamu dapatkan: ")
            if float(nilai) > 0:
              break
            else:
              print("Nilai yang kamu masukkan tidak valid")
        except Exception as e:
            print(nilai)
    scores.append(nilai)

    if 0 <= float(nilai) < 40:
        bobot = 0.00
    elif 40 <= float(nilai) < 55:
        bobot = 1.00
    elif 55 <= float(nilai) < 60:
        bobot = 2.00
    elif 60 <= float(nilai) < 65:
        bobot = 2.30
    elif 65 <= float(nilai) < 70:
        bobot = 2.70
    elif 70 <= float(nilai) < 75:
        bobot = 3.00
    elif 75 <= float(nilai) < 80:
        bobot = 3.30
    elif 80 <= float(nilai) < 85:
        bobot = 3.70
    elif 85 <= float(nilai):
        bobot = 4.00
    if bobot > 1:
        pass_credits.append(sks)
    weight.append(bobot)
    if bobot > 1:
        pass_weight.append(bobot)

    mutu = sks * bobot
    qualities.append(mutu)
    if bobot > 1:
        pass_qualities.append(mutu)


    print()
#saya assign value yang akan memudahkan saya saat proses mencetak hasil dari kalkulator_ipk.py
ipk = (sum(pass_qualities) / sum(pass_credits))
ipt = (sum(qualities) / sum(credits))
X = sum(pass_qualities)
y = sum(qualities)

#mencetak hasil dari kalkulator_ipk.py
print("Jumlah SKS lulus : " + str(int(sum(pass_credits))) + " / " + str(int(sum(credits))))
print("Jumlah mutu lulus: " + "{:.2f}".format(X) + " / " + "{:.2f}".format(y))
print("Total IPK kamu adalah " "{:.2f}".format(ipk))
print("Total IPT kamu adalah " "{:.2f}".format(ipt))
