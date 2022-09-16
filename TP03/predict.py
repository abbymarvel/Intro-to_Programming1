# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# lengkapi fungsi berikut
def load_ndsi(ndsi_filename):
    """
    Parameters
    ----------
    ndsi_filename : string
        sebuah nama file dimana daftar kata dan nilai NDSI-nya
        disimpan.

    Returns
    -------
    word_ndsi : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah NDSI score (float) dari kata tersebut.
    """
    word_ndsi = {}
    for line in open(ndsi_filename, "r").readlines():               # Membuka file NDSI
        line = line.strip("\n")                                     # .strip("\n") digunakan agar tidak ada "\n" di belakang string
        line = line.split(" ")                                      # split(" ")  digunakan karena pada file NDSI kata dan nilai NDSI hanya dipisahkan oleh spasi
        word_ndsi[line[0]] = line[1]                                # Memasukan kata sebagai keys dan nilai NDSI sebagai values di dict word_ndsi
    return word_ndsi

# lengkapi fungsi berikut
def compute_score(filename, word_ndsi):
    """
    Parameters
    ----------
    filename : string
        nama file dari kumpulan kalimat-kalimat yang ingin diprediksi
        labelnya apakah berorientasi sentiment positif atau negatif.
        Di soal, nama default-nya adalah sent-unknown-label.txt
    word_ndsi : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah NDSI score (float) dari kata tersebut.

    Returns
    -------
    pos_neg_scores : list
        list of pairs, dimana pair merupakan pasangan nilai
        positif dan negatif dari sebuah kalimat. Elemen pertama
        pada pair adalah nilai positif dan yang kedua adalah nilai
        negatif.

        Nilai positif dari sebuah kalimat didapatkan dengan cara
        menjumlahkan semua kata-kata pada kalimat tersebut yang
        mempunyai nilai NDSI > 0

        Nilai negatif dari sebuah kalimat didapatkan dengan cara
        menjumlahkan semua kata-kata pada kalimat tersebut yang
        mempunyai nilai NDSI < 0. Namun, nilai negatif harus dibuat
        absolut (bisa gunakan fungsi abs())

    Contoh
    ------
    Seandainya word_ndsi = {'bad':-0.67, 'worst':-1., 'good':0.90, 'nice':1.}

    dan sent-unknown-label.txt terdiri dari 2 kalimat:
        bad movie, worst scenario, but good actors
        good movie with nice plot

    Fungsi akan mengembalikan:
        [(0.90, 1.67), (1.90, 0.)]

    0.90 adalah dari kata good (0.90)
    1.67 adalah hasil dari 0.67 (bad) + 1 (worst)
    1.90 adalah dari 0.90 (good) + 1.0 (nice)
    0 adalah karena kalimat kedua tidak mengandung kata ber-NDSI negatif

    Notes
    -----
    Untuk nilai negatif, tanda (-) diabaikan

    """
    pos_neg_scores = []
    for line in open(filename, "r", encoding="utf-16-le").readlines():          
        pos = 0.00                                                  # set variable positif ke 0 kembali saat memproses kalimat baru
        neg = 0.00                                                  # set variable negatif ke 0 kembali saat memproses kalimat baru
        for word in line.split():
            if word in word_ndsi.keys():                            # Jika kata ada di dict word_ndsi maka program akan menghitung skor positif dan negatif dari setiap kalimat
                if float(word_ndsi[word]) > 0:
                    pos += float(word_ndsi[word])                   # Jika skor NDSI kata positif maka akan masuk ke skor positif
                elif float(word_ndsi[word]) < 0:
                    neg += abs(float(word_ndsi[word]))              # Jika skor NDSI kata negatif maka akan masuk ke skor negatif
        pos_neg_scores.append((pos, neg))                           # Menambahkan skor positif dan negatif ke dalam dict pos_neg_scores dengan format (positif, negatif)
    return pos_neg_scores

# Fungsi sudah diberikan; tinggal digunakan saja
def show_scatter_plot(pos_neg_scores):
    """
    Parameters
    ----------
    pos_neg_scores : list
        list of pairs, dimana pair merupakan pasangan nilai
        positif dan negatif dari sebuah kalimat. Elemen pertama
        pada pair adalah nilai positif dan yang kedua adalah nilai
        negatif.

    Returns
    -------
    None.

    Scatter plot dari semua nilai positif dan negatif dari
    kalimat yang belum diberi label (yang ada di sent-unknown-label.txt)

    Kalimat yang netral (nilai positif = nilai negatif) tidak diikutsertakan.

    """
    plt.clf()

    predicted_as_pos = [(pos_score, neg_score) for (pos_score, neg_score) \
                        in pos_neg_scores if pos_score > neg_score]
    predicted_as_neg = [(pos_score, neg_score) for (pos_score, neg_score) \
                        in pos_neg_scores if pos_score < neg_score]

    x_pos_1 = [pos_score for (pos_score, _) in predicted_as_pos]
    y_pos_1 = [neg_score for (_, neg_score) in predicted_as_pos]
    x_pos_2 = [pos_score for (pos_score, _) in predicted_as_neg]
    y_pos_2 = [neg_score for (_, neg_score) in predicted_as_neg]

    plt.scatter(x_pos_1, y_pos_1, color = 'blue', s = 5)
    plt.scatter(x_pos_2, y_pos_2, color = 'hotpink', s = 5)

    plt.xlabel("Positive Score")
    plt.ylabel("Negative Score")
    plt.xlim(-0.1, 8)
    plt.ylim(-0.1, 8)
    plt.savefig("senti-plot.pdf")



if __name__ == "__main__":

    # memuat dictionary berisi kata dan nilai NDSI-nya
    word_ndsi = load_ndsi("ndsi.txt")

    # hitung nilai
    pos_neg_scores = compute_score("sent-unknown-label-utf-16-le.txt", word_ndsi)

    # scatter plot yang menampilkan nilai positif dan negatif dari
    # kalimat-kalimat yang ada di sent-unknown-label.txt;
    # dokumen yang netral tidak diiukutsertakan.
    show_scatter_plot(pos_neg_scores)

    # untuk setiap kalimat (setiap baris di sent-unknown-label.txt),
    # jika nilai positif > nilai negatif --> predicted label: positif
    # jika nilai positif < nilai negatif --> predicted label: negatif
    # else --> predicted label: netral (hampir tidak ada sepertinya)
    for i, (pos_score, neg_score) in enumerate(pos_neg_scores):
        predicted_label = "neutral"
        if pos_score > neg_score:
            predicted_label = "pos"
        elif neg_score > pos_score:
            predicted_label = "neg"
        print(f"sentence {i+1} -- pos:{pos_score:6.3f}  neg:{neg_score:6.3f}  prediction:{predicted_label}")
