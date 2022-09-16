# set dictionaries untuk menyimpan value dari input agar saya mudah untuk mengolahnya
himpunan_a = []
himpunan_b = []
hasil = []

raw_input_a = input("Masukkan input himpunan A: ")      # menerima input
list_a = raw_input_a.split(",")                         # function split untuk memisahkan string menjadi list
for i in list_a:
    himpunan_a.append(i)                                # memasukan list dari input ke himpunan_a(dictionary)


raw_input_b = input("Masukkan input himpunan B: ")      # menerima input
list_b = raw_input_b.split(",")                         # function split untuk memisahkan string menjadi list
for j in list_b:
    himpunan_b.append(j)                                # memasukan list dari input ke himpunan_b(dictionary)

for i in himpunan_a:
    for j in himpunan_b:
        result = ("(" + i + "," + j + ")")              # menggabungkan setiap elemen di himpunan a dan himpunan b
        hasil.append(result)                            # memasukan hasil dari penggabungan ke hasil(dictionary)

print(*hasil, sep = ", ")                               # print(*value, sep=", ") digunakan untuk mencetak elemen dari list yang dipashkan oleh suatu karakter
                                                        # print(*value, sep=", ") juga saya gunakan agar tidak ada quotations di setiap value yang saya cetak