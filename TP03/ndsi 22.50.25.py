# -*- coding: utf-8 -*-
import string
import matplotlib.pyplot as plt

# lengkapi fungsi berikut
def load_stop_words(filename):
    """
    Parameters
    ----------
    filename : string
        nama file yang menyimpan daftar stopwords.
        Di soal, nama default-nya adalah stopwords.txt

    Returns
    -------
    stop_words : set
        himpunan stopwords (unik)

    Fungsi menerima nama file yang berisi daftar stopwords,
    kemudian memuat semua stopwords ke dalam struktur data
    set. Perhatikan bahwa semua stopwords yang ada di dalam
    file sudah dalam bentuk huruf kecil semua.
    """
    stop_words = set(open(filename, "r").read().split())                    # Membuka file dan memasukan isi file ke set()
    return stop_words

# lengkapi fungsi berikut
def count_words(filepath, stop_words):
    """
    Parameters
    ----------
    filepath : string
        path atau lokasi dari file yang berisi sekumpulan
        kalimat-kalimat yang memiliki polaritas sentiment,
        yaitu rt-polarity.neg atau rt-polarity.pos

    stop_words : set
        himpunan stopwords

    Returns
    -------
    word_freq : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut.

    Fungsi ini akan scan semua baris (semua kalimat) yang
    ada di file dan kemudian mengakumulasikan frekuensi dari
    setiap kata yang muncul pada file tersebut.

    Contoh
    ------
    Jika isi dari file adalah:

        I just watched a good movie
        wow! a good movie
        a good one

    Fungsi akan mengembalikan dictionary:
        {'i':1, 'just':1, 'watched':1, 'a':3, 'good':3,
         'movie':2, 'wow!':1, 'one':1}

    Notes
    -----
    1. stopwords diabaikan
    2. karakter tanda baca seperti , . / dan sebagainya juga
       diabaikan (gunakan string.punctuation di library string)
    """
    word_freq = {}
    for word in open(filepath, "r", encoding="utf-8").read().split():       # Membuka file
        word = word.lower()
        word = word.strip(string.punctuation)                               # strip(string.punctuation) digunakan untuk membersihkan text dari punctuations
        word = word.strip("‘")                                              # Menggunakan strip("‘") karena simbol tersebut tidak masuk ke dalam string.punctuation
        word = word.strip("…")                                              # Menggunakan strip("…")  karena simbol tersebut tidak masuk ke dalam string.punctuation
        if word in stop_words:                                              # Jika ada stop words di text maka tidak akan dihitung di word_freq
            continue
        elif word in word_freq.keys():
            word_freq[word] += 1                                            # Jika kata sudah pernah dimasukan ke dict maka program hanya akan menambahkan 1 ke valuenya
        elif word not in word_freq.keys():
            word_freq[word] = 1                                             # Jika kata belum pernah dimasukan ke dict maka program akan membuat key baru dengan value bernilai 1
    return word_freq

# lengkapi fungsi berikut
def compute_ndsi(word_freq_pos, word_freq_neg):
    """
    Parameters
    ----------
    word_freq_pos : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.pos
    word_freq_neg : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.neg

    Returns
    -------
    word_ndsi : dictionary
        sebuah dictionary, dimana key merupakan kata (string)
        dan value adalah NDSI score (float)

    Notes
    -----
    NDSI dari sebuah kata dihitung dengan:

              word_freq_pos[word] - word_freq_neg[word]
              -----------------------------------------
              word_freq_pos[word] + word_freq_neg[word]

    Jika kata tidak ditemukan pada salah satu dictionary,
    frekuensi kata tersebut adalah 0.

    Contoh
    ------
    Jika word_freq_neg = {'bad':10, 'worst':5, 'good':1} dan
         word_freq_pos = {'good':20, 'nice':5, 'bad':2},

    maka word_ndsi = {'bad':-0.67, 'worst':-1, 'good':0.90, 'nice':1}

    """
    word_ndsi = {}
    for word in word_freq_pos.keys():
        if word in word_freq_neg.keys():                                    # Jika kata di dict word_freq_pos juga terdapat di dict word_freq_neg
            word_ndsi[word] = (word_freq_pos[word] - word_freq_neg[word]) / (word_freq_pos[word] + word_freq_neg[word]) # Program menghitung NDSI dengan formula normal
        elif word not in word_freq_neg.keys():                              # Jika kata di dict word_freq_pos tidak terdapat di dict word_freq_neg
            word_ndsi[word] = (word_freq_pos[word] - 0) / (word_freq_pos[word] + 0)                                     # Program akan menggantukan  word_freq_neg[word] dengan 0
    for word in word_freq_neg.keys():
        if word not in word_freq_pos.keys():                                # Jika kata di dict word_freq_neg tidak terdapat di dict word_freq_pos
            word_ndsi[word] = (0 - word_freq_neg[word]) / (0 + word_freq_neg[word])                                     # Program akan menggantukan  pos[word] dengan 0
    return word_ndsi

# Fungsi berikut sudah selesai. Anda tidak perlu implementasikan
def show_ndsi_histogram(word_ndsi):
    """
    Parameters
    ----------
    word_ndsi : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah NDSI score (float) dari kata tersebut.

    Returns
    -------
    None.

    Plot histogram dari semua NDSI scores yang dihasilkan

    """
    ndsi_scores = [score for _, score in word_ndsi.items()]
    plt.hist(ndsi_scores, 100, facecolor = 'g', alpha = 0.75)
    plt.yscale("log")
    plt.xlabel('NDSI score')
    plt.ylabel('Frekuensi')
    plt.savefig("ndsi-hist.pdf")




if __name__ == "__main__":

    # memuat stop words ke sebuah set
    stop_words = load_stop_words("stopwords.txt")

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment positif
    word_freq_pos = count_words("./sent-polarity-data/rt-polarity.pos", stop_words)

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment negatif
    word_freq_neg = count_words("./sent-polarity-data/rt-polarity.neg", stop_words)

    # hitung NDSI untuk semua kata-kata pada kedua jenis dictionary berisi
    # word frequency
    word_freq_ndsi = compute_ndsi(word_freq_pos, word_freq_neg)

    # tampilkan histogram dari nilai-nilai NDSI yang dihasilkan
    show_ndsi_histogram(word_freq_ndsi)

    # LENGKAPI BAGIAN INI
    # urutkan pasangan kata dan skor ndsi yang ada
    # di word_freq_ndsi berdasarkan nilai ndsi saja, dari terkecil
    # ke yang terbesar

    # ... your code
    word_ndsi =  sorted(word_freq_ndsi.items(), key=lambda x: (x[1], x[0]))     # Sort dict word_ndsi dari value yang terkecil
    # LENGKAPI BAGIAN INI
    # simpan daftar kata-kata dan nilai ndsi yang sudah diurutkan tadi ke
    # file ndsi.txt

    # ... your code
    ndsi_filename = "ndsi.txt"
    file_output = open(ndsi_filename,"w", encoding="utf-8")
    for elem in word_ndsi:                                                      # Memasukan dict word_ndsi ke file_output
        print(elem[0],elem[1],file = file_output)