
import tkinter as tk
import tkinter.messagebox as tkmsg


class Product(object):

    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def set_stok(self, jumlah):
        self.__stok -= jumlah


class Buyer(object):

    def __init__(self):
        self.__daftar_beli = {}

    def add_daftar_beli(self, produk, jumlah):
        if produk in self.__daftar_beli:
          self.__daftar_beli[produk] += jumlah
        else :
          self.__daftar_beli[produk] = jumlah

    def get_daftar_beli(self):
        return self.__daftar_beli


class WindowLihatBarang(tk.Toplevel):

    def __init__(self, product_dict, master = None):
        super().__init__(master)
        self.product_dict = product_dict
        self.wm_title("Daftar Barang")
        self.create_widgets()

    def create_widgets(self):
        self.lbl_judul = tk.Label(self, \
                                  text = 'Daftar Barang Yang Tersedia').grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, \
                                 text = 'Nama Produk').grid(row = 1, column = 0)
        self.lbl_harga = tk.Label(self, \
                                  text = 'Harga').grid(row = 1, column = 1)
        self.lbl_stok = tk.Label(self, \
                                 text = 'Stok Produk').grid(row = 1, column = 2)

        i = 2
        for nama, barang in sorted(self.product_dict.items()):
            tk.Label(self, \
                     text = f"{nama}").grid(row = i, column= 0)
            tk.Label(self, \
                     text = f"{barang.get_harga()}").grid(row = i, column= 1)
            tk.Label(self, \
                     text = f"{barang.get_stok()}").grid(row = i, column= 2)
            i += 1

        self.btn_exit = tk.Button(self, text = "EXIT", \
                                  command = self.destroy).grid(row = i, column=1)           # jika button EXIT diclick maka window Daftar Barang akan ditutup


class WindowBeliBarang(tk.Toplevel):

    def __init__(self, buyer, product_dict, master = None):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.wm_title("Beli Barang")
        self.geometry("330x150")
        self.ent_nama_barang = tk.StringVar()
        self.ent_jumlah = tk.IntVar()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_judul = tk.Label(self, text = 'Form Beli Barang').grid(row=0, column=1)
        self.lbl_barang = tk.Label(self, text = 'Nama Barang').grid(row=1, column=0)
        self.lbl_jumlah = tk.Label(self, text = 'Jumlah').grid(row=2, column=0)
        self.inp_nama_barang = tk.Entry(self, textvariable=self.ent_nama_barang).grid(row=1, column=1, padx=1, pady=1)  # value dari input akan disimpan di instance self.ent_nama_barang
        self.inp_jumlah = tk.Entry(self, textvariable=self.ent_jumlah).grid(row=2, column=1, padx=1, pady=1)            # value dari input akan disimpan di instance self.ent_jumlah
        self.btn_count = tk.Button(self, text = "BELI", width = 10, \
                                    command = self.beli_barang).grid(row=3, column=1)
        self.btn_count = tk.Button(self, text = "EXIT", width = 10, \
                                    command = self.destroy).grid(row=4, column=1)   # jika button EXIT diclick maka window Beli Barang akan ditutup

    def beli_barang(self):          # method ini merupakan event handler untuk button BELI
        nama_barang = self.ent_nama_barang.get()
        jumlah = self.ent_jumlah.get()

        if nama_barang == "":
            answer = tkmsg.askretrycancel("BarangNotFound", "Nama barang tidak boleh kosong.")
            if answer == False:
                self.destroy()                              # jika user memilih retry maka mereka bisa melakukan input lagi, jika user memilih cancel maka window Beli Barang akan tertutup
                
        elif nama_barang not in self.product_dict:
            answer = tkmsg.askretrycancel("BarangNotFound",f"Barang dengan nama {nama_barang} tidak ditemukan di dalam BakungLapak.")
            if answer == False:
                self.destroy()

        elif self.product_dict[nama_barang].get_stok() - jumlah < 0:
            answer = tkmsg.showinfo("StokEmpty", "Maaf, stok produk telah habis.")
        
        else :
            barang = self.product_dict[nama_barang]
            buyer.add_daftar_beli(barang, jumlah)
            barang.set_stok(jumlah)
            self.ent_nama_barang.set("")                        # untuk mengosongkan Textfield saya menggunakan set("") karena 'StringVar' object has no attribute 'delete'
            self.ent_jumlah.set("")                             # untuk mengosongkan Textfield saya menggunakan set("") karena 'StringVar' object has no attribute 'delete'
            tkmsg.showinfo("Berhasil!", f"Berhasil membeli {nama_barang}")


class WindowCheckOut(tk.Toplevel):

    def __init__(self, buyer, master = None):
        super().__init__(master)
        self.wm_title("Daftar Barang")
        self.daftar_dibeli = buyer.get_daftar_beli()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_judul = tk.Label(self, \
                            text = 'Keranjangku').grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, \
                                 text = 'Nama Produk').grid(row = 1, column = 0)
        self.lbl_harga = tk.Label(self, \
                                  text = 'Harga Barang').grid(row = 1, column = 1)
        self.lbl_stok = tk.Label(self, \
                                 text = 'Jumlah').grid(row = 1, column = 2)
  
        i = 2
        for nama in sorted(self.daftar_dibeli.keys()):
            print(nama)
            tk.Label(self, \
                    text = f"{nama.get_nama()}").grid(row = i, column= 0)   # get_nama digunakan untuk mendapat nama produk yang telah di beli
            tk.Label(self, \
                    text = f"{nama.get_harga()}").grid(row = i, column= 1)  # get_harga digunakan untuk mendapat harga produk yang telah di beli
            tk.Label(self, \
                    text = f"{self.daftar_dibeli[nama]}").grid(row = i, column= 2)  # jumlah barang yang dibeli disimpan sebagai value di dict self.dafta_dibeli
            i += 1

        if len(self.daftar_dibeli.items()) == 0:                            # jika belum ada barang sama sekali di daftar_dibeli maka akan menampilkan pesan: "Belum ada yang dibeli :("
            tk.Label(self, text= 'Belum ada yang dibeli :(').grid(row = 2, column = 0, columnspan = 3)
            i += 1

        self.btn_exit = tk.Button(self, text = "EXIT", \
                                command = self.destroy).grid(row = i, column=1)         # jika button EXIT diclick maka window Daftar Barang akan ditutup


class MainWindow(tk.Frame):

    def __init__(self, buyer, product_dict, master = None):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, \
                              text = 'Selamat datang di BakungLapak. Silahkan pilih Menu yang tersedia')

        self.btn_lihat_daftar_barang = tk.Button(self, \
                                                 text = "LIHAT DAFTAR BARANG", \
                                                 command = self.popup_lihat_barang)
        self.btn_beli_barang = tk.Button(self, \
                                         text = "BELI BARANG", \
                                         command = self.popup_beli_barang)
        self.btn_check_out = tk.Button(self, \
                                       text = "CHECK OUT", \
                                       command = self.popup_check_out)
        self.btn_exit = tk.Button(self, \
                                  text = "EXIT", \
                                  command = quit) # jika button EXIT diclick maka program akan berhenti

        self.label.pack()
        self.btn_lihat_daftar_barang.pack()
        self.btn_beli_barang.pack()
        self.btn_check_out.pack()
        self.btn_exit.pack()

    def popup_lihat_barang(self):       # method ini merupakan event handler untuk button LIHAT DAFTAR BARANG
        WindowLihatBarang(self.product_dict)

    def popup_beli_barang(self):        # method ini merupakan event handler untuk button BELI BARANG
        WindowBeliBarang(self.buyer, self.product_dict)

    def popup_check_out(self):          # method ini merupakan event handler untuk button CHECK OUT
        WindowCheckOut(self.buyer)


if __name__ == "__main__":

    buyer = Buyer()

    product_dict = {"Kebahagiaan" : Product("Kebahagiaan", 999999, 1),
                    "Kunci TP3 SDA" : Product("Kunci TP3 SDA", 1000000, 660)}

    m = MainWindow(buyer, product_dict)
    m.master.title("BakungLapak")
    m.master.mainloop()
