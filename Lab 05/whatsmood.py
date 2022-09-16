my_input = input("Masukkan nama file input: ")

happiness = 50
sadness = 50
anger = 50

def smile():                                                # Function smile() ini mengganti kata (smile) dengan emoticon
    global in_file                                          # Menggunakan global untuk mengubah variable di luar function
    for word in in_file.split():
        if word == "(smile)":
            in_file = in_file.replace(word, "\U0001f603")

def sad():                                                  # Function sad() ini mengganti kata (sad) dengan emoticon
    global in_file                                          # Menggunakan global untuk mengubah variable di luar function
    for word in in_file.split():
        if word == "(sad)":
            in_file = in_file.replace(word, "\U0001f622")

def angry():                                                # Function angry() ini mengganti kata (angry) dengan emoticon
    global in_file                                          # Menggunakan global untuk mengubah variable di luar function
    for word in in_file.split():
        if word == "(angry)":
            in_file = in_file.replace(word, "\U0001f621")

def batas(n):                                               # Function batas() ini digunakan untuk membatasi aspek mood
    if n < 0:
        return 0                                            # 0 adalah batas bawah nilai aspek mood
    elif n > 100:
        return 100                                          # 100 adalah batas atas nilai aspek mood
    else:
        return n

def poin():                                                 # Function poin() ini digunakan untuk menghitung poin aspek mood
    global happiness                                        # Menggunakan global untuk mengubah variable di luar function
    global sadness                                          # Menggunakan global untuk mengubah variable di luar function
    global anger                                            # Menggunakan global untuk mengubah variable di luar function
    for line in pc_file:
        if line.startswith("Pak Chanek"):                   # Hanya emoticon yang dikirim Pak Chanek yang akan merubah mood
            for word in line.split():
                if word == "(smile)":
                    happiness += 9
                    sadness -= 6
                elif word == "(sad)":
                    sadness += 10
                    anger -= 8
                elif word == "(angry)":
                    anger += 13
                    happiness -= 5
    print("Mengukur suasana hati....")
    print()
    print("##### Hasil Pengukuran #####")
    print("Happiness = {} | Sadness = {} | Anger = {}".format(batas(happiness), batas(sadness), batas(anger)))

def kesimpulan():                                           # Function kesimpulan() ini digunakan untuk menyimpulkan mood
    print()
    print("##### Kesimpulan #####")
    if happiness > sadness:
        if happiness == anger:
            print("Pak Chanek sedang bahagia atau marah.")
        elif happiness > anger:
            print("Pak Chanek sedang bahagia.")
        elif happiness < anger:
            print("Pak Chanek sedang marah.")
    elif sadness > happiness:
        if sadness == anger:
            print("Pak Chanek sedang sedih atau marah.")
        elif sadness > anger:
            print("Pak Chanek sedang sedih.")
        elif sadness < anger:
            print("Pak Chanek sedang marah.")
    elif sadness == happiness == anger:
        print("Kesimpulan tidak ditemukan.")
    elif sadness == happiness:
        print("Pak Chanek sedang bahagia atau sedih.")

def main():                                                 # Function main() ini sebagai induk function
    global my_input
    try:
        global in_file
        global pc_file
        in_file = open(my_input, "r").read()
        pc_file = open(my_input, "r").readlines()
        if len(in_file.split()) == 0:
            print("File input ada tapi kosong :(")
            input("Program selesai. Tekan enter untuk keluar...")
            exit()
        else:
            smile()
            sad()
            angry()
            print()
            print(in_file)
            poin()
            kesimpulan()

    except FileNotFoundError:                                   # jika file input tidak ditemukan maka program akan berhenti
        print("File input tidak ada :(")
        my_input = input("Masukkan nama file input: ")
        main()

main()