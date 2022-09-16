
def starter():
    input_user = input()
    if input_user == "selesai":
        print("\nList perintah:\n1. RANTAI_PENYEBARAN\n2. CEK_PENULARAN\n3. EXIT")
        menu()
    elif len(input_user.split()) == 1:
        nama[input_user.split()[0]] = ''
        starter()
    else:
        nama_penular = input_user.split()[0]
        if nama_penular not in nama.keys():
            nama[nama_penular] = input_user.split()[1:]
        else:
            nama[nama_penular] += input_user.split()[1:]
        starter()


def menu():
    global output
    global main
    output = []
    main = input("\nMasukkan perintah: ")
    if main.startswith("RANTAI_PENYEBARAN"):
        print(f"Rantai penyebaran {main.split()[1]}:")
        rantai_penyebaran(main.split()[1])
        output.append(main.split()[1])
        for i in output:
            print(f"- {i}")
        menu()
    if main.startswith("CEK_PENULARAN"):
        cek_penularan(main.split()[1], main.split()[2])
    elif main == "EXIT":
        print("Terima kasih sudah menggunakan program ini!")
        exit()
    else:
        print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.")
        menu()


def rantai_penyebaran(penular): #dalan func ini saya menggunakan recursion untuk mengumpulkan semua nama yang tertular oleh penular
    if len(nama[penular]) != 0:
        output.extend(nama[penular])    #saya menggunakan extend agar tidak ada list dalam list
    for i in nama[penular]:
        rantai_penyebaran(i)
    return output


def cek_penularan(tertular, penular):
    values = []
    for i in nama.values():
        for j in i:
            values.append(j)
    if penular not in nama.keys() and tertular not in values:
        print(f"Maaf, nama {tertular} dan {penular} tidak ada dalam rantai penyebaran.")
        menu()
    elif penular not in nama.keys():
        print(f"Maaf, nama {penular} tidak ada dalam rantai penyebaran.")
        menu()
    elif tertular not in values:
        print(f"Maaf, nama {tertular} tidak ada dalam rantai penyebaran.")
        menu()
    elif tertular in nama[penular]:
        print("Ya")
        menu()
    elif nama[tertular] in values:
        print("Ya")
        menu()
    else:
        print("Tidak")
        menu()

nama = {}
print("Masukkan rantai penyebaran:")
starter()
