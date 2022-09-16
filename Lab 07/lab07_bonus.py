def menu():                 # func ini untuk menentukan perintah apa yang akan dikerjakan
    global main
    main = input("\nMasukkan perintah: ")
    if main == "INFO_TUJUAN":
        info_tujuan()
    elif main.startswith("TUJUAN_KELAS_TERMURAH"):
        tujuan_kelas_termurah()
    elif main.startswith("TUJUAN_KELAS"):
        tujuan_kelas()
    elif main.startswith("TUJUAN_JAM_TERMURAH"):
        tujuan_jam_termurah()
    elif main.startswith("TUJUAN_JAM"):
        tujuan_jam()
    elif main == "EXIT":
        print("Terima kasih sudah menggunakan program ini!")
        exit()
    else:
        print("Perintah yang dimasukkan tidak valid.")
        menu()


def info_tujuan():          # func ini untuk melihat tujuan akhir KA yang tersedia di stasiun ini
    for i in jadwal:
        if i.split()[1] not in tujuan_akhir:
            tujuan_akhir.append(i.split()[1])
        else:
            continue
    print("KA di stasiun ini memiliki tujuan akhir:")
    for i in tujuan_akhir:
        print(i)
    menu()


def tujuan_kelas():         # func ini untuk melihat KA dengan tujuan akhir dan kelas tertentu
    if len(main.split()) != 3:
        print("Perintah yang dimasukkan tidak valid.")
        menu()
    count = set() # set digunakan untuk melihat apakah ada KA yang sesuai perintah atau tidak ada sama sekali
    req = {} # dict digunakan untuk menyimpan perintah
    req["tujuan"] = main.split()[1]
    req["kelas"] = main.split()[2]
    for i in jadwal:
        if req["tujuan"].lower() == i.split()[1].lower():
            if req["kelas"].lower() == "eksekutif" and i.split()[0].startswith("1"):
                print(f"KA {i.split()[0]} berangkat pukul {i.split()[2]} dengan harga tiket {i.split()[3]}")
                count.add(i.split()[0])
            elif req["kelas"].lower() == "bisnis" and i.split()[0].startswith("2"):
                print(f"KA {i.split()[0]} berangkat pukul {i.split()[2]} dengan harga tiket {i.split()[3]}")
                count.add(i.split()[0])
            elif req["kelas"].lower() == "ekonomi" and i.split()[3].startswith("3"):
                print(f"KA {i.split()[0]} berangkat pukul {i.split()[2]} dengan harga tiket {i.split()[3]}")
                count.add(i.split()[0])
    if len(count) == 0:
        print("Tidak ada jadwal KA yang sesuai.")
    menu()


def tujuan_kelas_termurah():    # func ini untuk melihat KA dengan tujuan akhir dan kelas tertentu dengan harga termurah
    if len(main.split()) != 3:
        print("Perintah yang dimasukkan tidak valid.")
        menu()
    count = set() # set digunakan untuk melihat apakah ada KA yang sesuai perintah atau tidak ada sama sekali
    harga = []
    req = {} # dict digunakan untuk menyimpan perintah
    req["tujuan"] = main.split()[1]
    req["kelas"] = main.split()[2]
    for i in jadwal:
        if req["tujuan"].lower() == i.split()[1].lower():
            if req["kelas"].lower() == "eksekutif" and i.split()[0].startswith("1"):
                for x in jadwal:
                    if x.split()[0].startswith("1"):
                        harga.append(x.split()[3])
                if i.split()[3] == min(harga):
                    print(f"KA {i.split()[0]} berangkat pukul {i.split()[2]} dengan harga tiket {i.split()[3]}")
                    count.add(i.split()[0])
            elif req["kelas"].lower() == "bisnis" and i.split()[0].startswith("2"):
                for x in jadwal:
                    if x.split()[0].startswith("2"):
                        harga.append(x.split()[3])
                if i.split()[3] == min(harga):
                    print(f"KA {i.split()[0]} berangkat pukul {i.split()[2]} dengan harga tiket {i.split()[3]}")
                    count.add(i.split()[0])
            elif req["kelas"].lower() == "ekonomi" and i.split()[0].startswith("3"):
                for x in jadwal:
                    if x.split()[0].startswith("3"):
                        harga.append(x.split()[3])
                if i.split()[3] == min(harga):
                    print(f"KA {i.split()[0]} berangkat pukul {i.split()[2]} dengan harga tiket {i.split()[3]}")
                    count.add(i.split()[0])
    if len(count) == 0:
        print("Tidak ada jadwal KA yang sesuai.")
    menu()


def tujuan_jam():   # func ini untuk melihat KA dengan tujuan akhir dan jam keberangkatan tertentu
    if len(main.split()) != 3:
        print("Perintah yang dimasukkan tidak valid.")
        menu()
    count = set() # set digunakan untuk melihat apakah ada KA yang sesuai perintah atau tidak ada sama sekali
    req = {} # dict digunakan untuk menyimpan perintah
    req["tujuan"] = main.split()[1]
    req["jam"] = main.split()[2]
    for i in jadwal:
        if req["tujuan"].lower() == i.split()[1].lower() and int(req["jam"]) >= int(i.split()[2]):
            print(f"KA {i.split()[0]} berangkat pukul {i.split()[2]} dengan harga tiket {i.split()[3]}")
            count.add(i.split()[0])
    if len(count) == 0:
        print("Tidak ada jadwal KA yang sesuai.")
    menu()


def tujuan_jam_termurah():
    # func ini untuk melihat KA dengan tujuan akhir dan jam keberangkatan tertentu dengan harga termurah
    if len(main.split()) != 3:
        print("Perintah yang dimasukkan tidak valid.")
        menu()
    count = set() # set digunakan untuk melihat apakah ada KA yang sesuai perintah atau tidak ada sama sekali
    harga = []
    req = {} # dict digunakan untuk menyimpan perintah
    req["tujuan"] = main.split()[1]
    req["jam"] = main.split()[2]
    for i in jadwal:
        if req["tujuan"].lower() == i.split()[1].lower():
            for x in jadwal:
                if req["tujuan"].lower() == x.split()[1].lower() and int(req["jam"]) >= int(x.split()[2]):
                    harga.append(int(x.split()[3]))
            if int(i.split()[3]) == min(harga):
                print(f"KA {i.split()[0]} berangkat pukul {i.split()[2]} dengan harga tiket {i.split()[3]}")
                count.add(i.split()[0])
    if len(count) == 0:
        print("Tidak ada jadwal KA yang sesuai.")
    menu()


jadwal = []         # list untuk menyimpan semua jadwal KA yang tersedia
tujuan_akhir = []   # list untuk menyimpan semua tujuan_akhir KA yang tersedia


print("Selamat datang! Silakan masukkan jadwal KA:")
input_ka = input()
while input_ka.lower() != "selesai":
    jadwal.append(input_ka)
    input_ka = input()
print("\nPerintah yang tersedia:\n1. INFO_TUJUAN\n2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>")
print("3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>\n4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>")
print("5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>\n6. EXIT")

menu()
