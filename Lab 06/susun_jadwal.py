MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

MATKUL_TERSEDIA = [
["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] + JAM[9] + 40],
["ddp 1 c", HARI[2] + JAM[8] + 0, HARI[2] + JAM[9] + 40],
["ddp 1 b", HARI[1] + JAM[8] + 0, HARI[1] + JAM[9] + 40],
["manbis", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
["matdis 1 a", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
["matdis 1 b", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
["kalkulus 1 c", HARI[2] + JAM[10] + 0, HARI[2] + JAM[12] + 00]
]
MATKUL_DIAMBIL = []
JADWAL = {}

def menu():                         #function ini untuk mengatur flow dari program
    print("=========== SUSUN JADWAL ===========")
    print("1  Add matkul\n2  Drop matkul\n3  Cek ringkasan\n4  Lihat daftar matkul \n5  Selesai")
    print("====================================\n")
    mode = input("Masukkan pilihan: ")
    if mode == str(1):              #jika memilih mode 1 maka akan menambahkan matkul
        add_matkul()
    elif mode == str(2):            #jika memilih mode 2 maka akan mengurangkan matkul
        drop_matkul()
    elif mode == str(3):            #jika memilih mode 3 maka akan meringkas
        ringkasan()
    elif mode == str(4):            #jika memilih mode 4 maka akan mengeluarkan jadwal
        print_hasil()
    elif mode == str(5):            #jika memilih mode 5 maka akan keluar dari program
        print("Terima kasih!")
        exit()
    else:                           #jika pilihan tidak tersedia maka akan masuk ke menu kembali
        print("Maaf, pilihan tidak tersedia\n")
        menu()

def add_matkul():                       #function ini untuk menambahkan matkul
    matkul = input("Masukkan nama matkul: ")
    for i in MATKUL_TERSEDIA:
        if matkul in i:
            MATKUL_DIAMBIL.append(i)    #menambahkan matkul ke list matkul yang diambil
            print()
            menu()                      #setelah menambahkan matkul baru maka akan kembali ke menu
    print("Matkul tidak ditemukan\n")
    menu()                              #jka matkul yang ingin ditambahkan tidak dapat ditemukann akan kembali ke menu

def drop_matkul():                      #function ini untuk mengurangkan matkul
    matkul = input("Masukkan nama matkul: ")
    for i in MATKUL_DIAMBIL:
        if matkul in i:
            MATKUL_DIAMBIL.remove(i)    #menghilangkan matkul dari list matkul yang diambil
            print()
            menu()                      #setelah mengurangi matkul akan kembali lagi ke menu
    print("Matkul tidak ditemukan\n")
    menu()                              #jika nama matkul tidak terdapat di list matkul diambil akan kembali ke menu

def ringkasan():    #function ini digunakan untuk melihat apakah ada matkul yang bentrok
    bentrok = []
    for i in range(len(MATKUL_DIAMBIL)):
        for j in range(i, len(MATKUL_DIAMBIL)): #untuk membandingkan waktu mulai dan akhir setiap matkul yang dipilih
            if i == j:
                continue
            matkul1 = MATKUL_DIAMBIL[i]
            matkul2 = MATKUL_DIAMBIL[j]
            start1 = matkul1[1]
            start2 = matkul2[1]
            stop1 = matkul1[2]
            stop2 = matkul2[2]
            if start2 <= start1 <= stop2 or start2 <= stop1 <= stop2:
                bentrok.append([matkul1, matkul2])
                print(matkul1[0].upper(), "bentrok dengan", matkul2[0].upper()) #mencetak setiap matkul yang bentrok
    if not bentrok:
        print("Tidak ada matkul yang bermasalah\n")                             #jika tidak bentrok sama sekali
        menu()
    else:
        print()
        menu()

def print_hasil():  #function ini digunakan untuk mencetak jadwal secara keseluruhan
    for i in MATKUL_DIAMBIL:
        if i[1] > 5760:
            jam_start = (i[1]-5760)//60
            menit_start = (i[1]-5760)%60
            start = f'{jam_start:>02}.{menit_start:>02}'
            jam_stop = (i[2]-5760)//60
            menit_stop = (i[2]-5760)%60
            akhir = f'{jam_stop:>02}.{menit_stop:>02}'
            print("{:<15s}{:<8s}{:<5} s/d {:<5}".format(i[0].upper(), "Jumat,", start, akhir))
        elif i[1] > 4320:
            jam_start = (i[1]-4320)//60
            menit_start = (i[1]-4320)%60
            start = f'{jam_start:>02}.{menit_start:>02}'
            jam_stop = (i[2]-4320)//60
            menit_stop = (i[2]-4320)%60
            akhir = f'{jam_stop:>02}.{menit_stop:>02}'
            print("{:<15s}{:<8s}{:<5} s/d {:<5}".format(i[0].upper(), "Kamis,", start, akhir))
        elif i[1] > 2880:
            jam_start = (i[1]-2880)//60
            menit_start = (i[1]-2880)%60
            start = f'{jam_start:>02}.{menit_start:>02}'
            jam_stop = (i[2]-2880)//60
            menit_stop = (i[2]-2880)%60
            akhir = f'{jam_stop:>02}.{menit_stop:>02}'
            print("{:<15s}{:<8s}{:<5} s/d {:<5}".format(i[0].upper(), "Rabu,", start, akhir))
        elif i[1] > 1440:
            jam_start = (i[1]-1440)//60
            menit_start = (i[1]-1440)%60
            start = f'{jam_start:>02}.{menit_start:>02}'
            jam_stop = (i[2]-1440)//60
            menit_stop = (i[2]-1440)%60
            akhir = f'{jam_stop:>02}.{menit_stop:>02}'
            print("{:<15s}{:<8s}{:<5} s/d {:<5}".format(i[0].upper(), "Selasa,", start, akhir))
        else:
            jam_start = i[1]//60
            menit_start = i[1]%60
            start = f'{jam_start:>02}.{menit_start:>02}'
            jam_stop = i[2]//60
            menit_stop = i[2]%60
            akhir = f'{jam_stop:>02}.{menit_stop:>02}'
            print("{:<15s}{:<8s}{:<5} s/d {:<5}".format(i[0].upper(), "Senin,", start, akhir))
    print()
    menu()

menu()