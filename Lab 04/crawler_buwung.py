my_input = input("Masukkan nama file input: ")
try:
    input_files = open(my_input, "r").read()
    if len(input_files.split()) == 0:                           # jika file kosong maka program akan berhenti
        print("File input ada tapi kosong :(")
        input("Program selesai. Tekan enter untuk keluar...")
        exit()
    else:
        my_output = input("Masukkan nama file output: ")        # file output akan terbentuk hanya jika file input valid.
        count_hashtag = 0
        count_mention = 0
        count_url = 0
        for word in input_files.split():
            if word.startswith("#"):
                input_files = input_files.replace(word, "(H)")  # Semua substring yang diawali "#" diganti dengan "(H)"
                count_hashtag += 1
            elif word.startswith("@"):
                input_files = input_files.replace(word, "(M)")  # Semua substring yang diawali "@" diganti dengan "(M)"
                count_mention += 1
            elif word.startswith("www."):
                input_files = input_files.replace(word, "(U)")  # Semua substring yang diawali "www." diganti dengan "(U)"
                count_url += 1
except FileNotFoundError:                                       # jika file input tidak ditemukan maka program akan berhenti
    print("File input tidak ada :(")
    input("Program selesai. Tekan enter untuk keluar...")
    exit()

output_files = open(my_output, "w")
print(input_files, file=output_files)                           # writing hasil dari program ke file output
print("###############", file=output_files)
print("Mention : {:>4d}".format(count_mention), file=output_files)
print("Hashtag : {:>4d}".format(count_hashtag), file=output_files)
print("Url     : {:>4d}".format(count_url), file=output_files)
print("Output berhasil ditulis pada", my_output)
input("Program selesai. Tekan enter untuk keluar...")
