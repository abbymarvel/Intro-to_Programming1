import random
# function digunakan untuk memudahkan saya dalam mengatur flow chart program math bot ini
def main_menu():
    print("Pilih Mode:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Campur")
    print("4. Akhiri program")
    print()
    menu_pilihan = input("Masukkan perintah: ")
    print()
    try:
        menu = int(menu_pilihan)
        if menu == 1:
            print("Baik, pilih mode penjumlahan ya, sekarang pilih jenis kuis apa?")
            kuis_1()
        elif menu == 2:
            print("Baik, pilih mode pengurangan ya, sekarang pilih jenis kuis apa?")
            kuis_2()
        elif menu == 3:
            print("Baik, pilih mode campur ya, sekarang pilih jenis kuis apa?")
            kuis_3()
        elif menu == 4:
            print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
            exit()
        else:
            print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
            print()
            main_menu()
    except ValueError:
        print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
        print()
        main_menu()

def kuis_1():
    print("Pilih kuis:")                    # menurut saya seharusnya hanya satu function kuis yang diperlukan
    print("1. Kuis Lepas")                  # namun saya menemukan beberapa masalah
    print("2. Kuis 5")                      # sehingga saya membuat satu function kuis untuk seiap game mode
    print("3. Ganti mode")                  # function kuis_1() ini untuk menentukan mode kuis penjumlahan
    print("4. Akhiri Program")
    print()
    kuis_pilihan = input("Masukkan jenis kuis: ")
    print()
    try:
        mode = int(kuis_pilihan)
        if mode == 1:
            penjumlahan()
        elif mode == 2:
            penjumlahan_kuis_lima()
        elif mode == 3:
            main_menu()
        elif mode == 4:
            print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
            exit()
        else:
            print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
            print()
            kuis_1()
    except ValueError:
        print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
        print()
        kuis_1()

def kuis_2():
    print("Pilih kuis:")                    # function kuis_2() ini untuk menentukan mode kuis penjumlahan
    print("1. Kuis Lepas")
    print("2. Kuis 5")
    print("3. Ganti mode")
    print("4. Akhiri Program")
    print()
    kuis_pilihan = input("Masukkan jenis kuis: ")
    print()
    try:
        mode = int(kuis_pilihan)
        if mode == 1:
            pengurangan()
        elif mode == 2:
            pengurangan_kuis_lima()
        elif mode == 3:
            main_menu()
        elif mode == 4:
            print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
            exit()
        else:
            print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
            print()
            kuis_2()
    except ValueError:
        print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
        print()
        kuis_2()

def kuis_3():
    print("Pilih kuis:")                    # function kuis_3() ini untuk menentukan mode kuis campur
    print("1. Kuis Lepas")
    print("2. Kuis 5")
    print("3. Ganti mode")
    print("4. Akhiri Program")
    print()
    kuis_pilihan = input("Masukkan jenis kuis: ")
    print()
    try:
        mode = int(kuis_pilihan)
        if mode == 1:
            campur()
        elif mode == 2:
            campur_kuis_lima()
        elif mode == 3:
            main_menu()
        elif mode == 4:
            print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
            exit()
        else:
            print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
            print()
            kuis_3()
    except ValueError:
        print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
        print()
        kuis_3()

def penjumlahan():
    x = random.randrange(0, 11)             # function ini untuk generate soal penjumlahan dengan bilangan bulat acak

    y = random.randrange(0, 11)

    print("berapa", x, "+", y, "?")
    jawaban = input("Jawab: ")

    try:                                    # menentukan apakah jawaban bisa diconvert menjadi int atau tidak
        val = int(jawaban)                  # jika jawaban bisa diconvert, maka jawaban akan lanjut diproses di sini
        if val == (x + y):                  # selanjutnya kita check apakah jawaban benar atau salah
            print("Hore Benar!")            # jika benar maka program akan mencetak "Hore Benar!"
            print()
            penjumlahan()
        else:                               # jika salah maka program akan mencetak jawaban yang benar
            print("Masih kurang tepat, ya. Jawabannya adalah", str(x + y))
            print()
            penjumlahan()
    except ValueError:                      # jika jawaban tidak bisa diconvert di atas, maka akan di proses di sini
        if jawaban == "akhiri kuis":        # saya menggunakan except Value Error ini agar program dapat membedakan:
            print()                         # kapan harus mengakhiri kuis dan kapan jawaban invalid
            kuis_1()
        else:
            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
            print()
            penjumlahan()                   # jika jawaban tidak valid maka program akan berjalan terus, tidak berhenti

def penjumlahan_kuis_lima():
    skor = 0
    for i in range(5):                      # menggunakan in range(5) untuk mengenerate 5 soal saja
        x = random.randrange(0, 11)
        y = random.randrange(0, 11)

        print("berapa", x, "+", y, "?")
        jawaban = input("Jawab: ")

        try:
            val = int(jawaban)
            if val == (x + y):
                print("Hore Benar!")
                print()
                skor += 20                  # setiap jawaban benar, maka skor akan bertambah 20
            else:
                print("Masih kurang tepat, ya. Jawabannya adalah", str(x + y))
                print()
        except ValueError:                  # jika ada input yang invalid maka program tidak berhenti
            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
            print()
    print("Score kamu: ", skor)             # jika semua soal sudah keluar, maka program akan mengeluarkan nilai akhir
    print()
    kuis_1()

def pengurangan():
    x = random.randrange(0, 11)
    y = random.randrange(x, 11)

    print("berapa", y, "-", x, "?")
    jawaban = input("Jawab: ")

    try:
        val = int(jawaban)
        if val == (y - x):
            print("Hore Benar!")
            print()
            pengurangan()
        else:
            print("Masih kurang tepat, ya. Jawabannya adalah", str(y - x))
            print()
            pengurangan()
    except ValueError:
        if jawaban == "akhiri kuis":
            print()
            kuis_2()
        else:
            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
            print()
            pengurangan()

def pengurangan_kuis_lima():
    skor = 0
    for i in range(5):
        x = random.randrange(0, 11)
        y = random.randrange(x, 11)

        print("berapa", y, "-", x, "?")
        jawaban = input("Jawab: ")

        try:
            val = int(jawaban)
            if val == (y - x):
                print("Hore Benar!")
                print()
                skor += 20
            else:
                print("Masih kurang tepat, ya. Jawabannya adalah", str(y - x))
                print()
        except ValueError:
            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
            print()
    print("Score kamu: ", skor)
    print()
    kuis_2()

def campur():
    a = random.randrange(1, 3)              # saya menggunakan variable a untuk mengacak soal yang akan keluar:
                                            # antara soal penjumlahan dan pengurangan
    if a == 1:
        x = random.randrange(0, 11)
        y = random.randrange(0, 11)

        print("berapa", x, "+", y, "?")
        jawaban = input("Jawab: ")

        try:
            val = int(jawaban)
            if val == (x + y):
                print("Hore Benar!")
                print()
                campur()
            else:
                print("Masih kurang tepat, ya. Jawabannya adalah", str(x + y))
                print()
                campur()
        except ValueError:
            if jawaban == "akhiri kuis":
                print()
                kuis_3()
            else:
                print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                print()
                campur()

    elif a == 2:
        x = random.randrange(0, 11)
        y = random.randrange(x, 11)

        print("berapa", y, "-", x, "?")
        jawaban = input("Jawab: ")

        try:
            val = int(jawaban)
            if val == (y - x):
                print("Hore Benar!")
                print()
                campur()
            else:
                print("Masih kurang tepat, ya. Jawabannya adalah", str(y - x))
                print()
                campur()
        except ValueError:
            if jawaban == "akhiri kuis":
                print()
                kuis_3()
            else:
                print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                print()
                campur()

def campur_kuis_lima():
    skor = 0
    for x in range(5):
        a = random.randrange(1, 3)
        if a == 1:
            x = random.randrange(0, 11)
            y = random.randrange(0, 11)

            print("berapa", x, "+", y, "?")
            jawaban = input("Jawab: ")

            try:
                val = int(jawaban)
                if val == (x + y):
                    print("Hore Benar!")
                    print()
                    skor += 20
                else:
                    print("Masih kurang tepat, ya. Jawabannya adalah", str(x + y))
                    print()
            except ValueError:
                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                    print()
        elif a == 2:
            x = random.randrange(0, 11)
            y = random.randrange(x, 11)

            print("berapa", y, "-", x, "?")
            jawaban = input("Jawab: ")

            try:
                val = int(jawaban)
                if val == (y - x):
                    print("Hore Benar!")
                    print()
                    skor += 20
                else:
                    print("Masih kurang tepat, ya. Jawabannya adalah", str(y - x))
                    print()
            except ValueError:
                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                    print()
    print("Score kamu: ", skor)
    print()
    kuis_3()

print("Halo, selamat datang di Mathbot")
main_menu()