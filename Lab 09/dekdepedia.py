
class User() :
    def __init__(self, user_name, tipe):
        self.user_name = user_name
        self.tipe = tipe

    def get_name(self) : 
        return self.user_name

    def get_tipe(self) : 
        return self.tipe

class Seller(User) : 
    def __init__(self, user_name, tipe, pemasukan):
        super().__init__(user_name, tipe)
        self.pemasukan = pemasukan
        self.list_barang_jual = []
        pemasukan_seller[user_name] = 0

    def get_pemasukan(self) : 
        return self.pemasukan

    def set_pemasukan(self, y) : 
        self.pemasukan = y

    def tambah_product(self, nama_produk, harga, stock_tersedia):
        if nama_produk not in self.list_barang_jual:
            list_product.append(nama_produk)
            harga_product[nama_produk] = int(harga)                 # memasukan product yang baru ditambah ke dict yang akan digunakan pada saat transaksi
            stock_product[nama_produk] = int(stock_tersedia)
            seller_product[nama_produk] = Seller.get_name(self)
            print()
        else:
            print("Produk sudah pernah terdaftar.\n")

    def lihat_produk_jualan_saya(self) : 
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Produk   |   Harga   | Stok ")
        print("-------------------------------------")

        for product in sorted(list_product) : 
            if seller_product[product] == user_name_login:
                print(" {:<15}| {:<10}| {:<6}".format(product, harga_product[product], stock_product[product]))
        print("-------------------------------------\n")

    def menu(self) :                                            # Menu untuk user seller
        print("Selamat datang {},".format(user_name_login))
        print('berikut menu yang bisa Anda lakukan:')
        print("1. TAMBAHKAN_PRODUK")
        print("2. LIHAT_DAFTAR_PRODUK_SAYA")
        print("3. LOG_OUT")
        print()
        print("Pemasukan anda {},".format(self.get_pemasukan()))
        pilih = input("Apa yang ingin Anda lakukan? ")
        while True:
            if pilih == "1":                                    # Seller bisa menambahkan barang yang mereka jual
                inp = input("Masukkan data produk : ")
                self.tambah_product(inp.split()[0], inp.split()[1], inp.split()[2])
                print("Pemasukan anda {},".format(self.get_pemasukan()))
                pilih = input("Apa yang ingin Anda lakukan? ")
            elif pilih == "2":                                  # Seller bisa melihat apa saja yang mereka jual
                Seller.lihat_produk_jualan_saya(user_name_login)
                print("Pemasukan anda {},".format(self.get_pemasukan()))
                pilih = input("Apa yang ingin Anda lakukan? ")
            elif pilih == "3":                                  # Program akan keluar dari akun dan kembali ke main menu
                print("Anda telah keluar dari akun {}".format(user_name_login))
                main()
            
class Buyer(User) : 
    def __init__(self, user_name, tipe, saldo):
        super().__init__(user_name, tipe)
        self.saldo = saldo
    
    def get_saldo(self) : 
        return self.saldo
    
    def set_saldo(self, x):
        self.saldo = x
    
    def riwayat_pembelian(self) : 
        print("\nBerikut merupakan barang yang saya beli")
        print("-------------------------------------")
        print("  Nama Produk  |   Harga   | Penjual ")
        print("-------------------------------------")

        for product in sorted(riwayat_pembelian) : 
            print(" {:<15}| {:<10}| {:<6}".format(product, harga_product[product], seller_product[product]))
        print("-------------------------------------\n")
    
    def menu(self):                                                             # Menu untuk user buyer
        print("Selamat datang {},".format(user_name_login))
        print('berikut menu yang bisa Anda lakukan: ')
        print("1. LIHAT_SEMUA_PRODUK")
        print("2. BELI_PRODUK")
        print("3. RIWAYAT_PEMBELIAN_SAYA")
        print("4. LOG_OUT")
        print()
        print("Saldo anda {},".format(self.get_saldo()))
        pilih = input("Apa yang ingin Anda lakukan? ")
        while True:
            if pilih == "1":                                                    # Jika user memilih menu "1. LIHAT_SEMUA_PRODUK" maka program akan mencetak semua barang yang dijual
                print("Berikut merupakan daftar produk di Dekdepedia")
                print("------------------------------------------------")
                print("  Nama Produk  |   Harga    | Stock |  Penjual")
                print("------------------------------------------------")
                for product in sorted(list_product) :
                    print("{:<15}|{:<12}|{:<7}|{:<9}".format(product, harga_product[product], stock_product[product], seller_product[product]))
                print("------------------------------------------------\n")
                print("Saldo anda {},".format(self.get_saldo()))
                pilih = input("Apa yang ingin Anda lakukan? ")
            elif pilih == "2":                                                  # Jika user memilih menu "2. BELI_PRODUK" maka program akan memproses transaksi yang ingin dilakukan buyer
                inp = input("Masukkan barang yang ingin dibeli : ")
                if inp in harga_product.keys():                                 # Jika produk yang ingin dibeli ada di Dedekpedia, maka program akan memproses transaksi lebih jauh lagi
                    if stock_product[inp] == 0:                                 # Memastikan apakah produk tersedia atau habis
                        print("Maaf, stok produk telah habis.\n") 
                    elif int(self.get_saldo()) < harga_product[inp]:            # Memastikan apakah saldo buyer mencukupi atau kurang
                        print("Maaf, saldo Anda tidak cukup untuk membeli {}.\n".format(inp))
                    else:
                        Buyer.set_saldo(self, (int(self.get_saldo()) - harga_product[inp]))     # Jika semua sudah aman, maka transaksi akan berlangsung
                        stock_product[inp] -= 1
                        riwayat_pembelian.append(inp)
                        pemasukan_seller[seller_product[inp]] += harga_product[inp]
                        print("Berhasil membeli {} dari {}\n".format(inp, seller_product[inp]))
                    print("Saldo anda {},".format(self.get_saldo()))
                    pilih = input("Apa yang ingin Anda lakukan? ")
                elif inp not in harga_product.keys():                           # Jika produk  yang ingin dibeli tidak ada di Dedekpia, maka program akan meminta perintah kembali
                    print("Barang dengan nama {} tidak ditemukan dalam Dekdepedia.\n".format(inp))
                    print("Saldo anda {},".format(self.get_saldo()))
                    pilih = input("Apa yang ingin Anda lakukan? ")
            elif pilih == "3":                                                  # Jika user memilih menu "3. RIWAYAT_PEMBELIAN_SAYA", maka program akan mencetak transaksi yang sudah buyer lakukan
                Buyer.riwayat_pembelian(self)
                print("Saldo anda {},".format(self.get_saldo()))
                pilih = input("Apa yang ingin Anda lakukan? ")
            elif pilih == "4":                                                  # Jika user memilih menu "4. LOG_OUT", maka program akan keluar dari akun dan kembali ke main menu
                print("Anda telah keluar dari akun {}".format(user_name_login))
                main()

class Product() : 
    def __init__(self, product, harga, stock, seller):
        self.nama = product
        self.harga = harga
        self.stock = stock
        self.seller = seller
    
    def get_name(self) : 
        return self.nama
    
    def get_harga(self) : 
        return self.harga

    def get_stock(self) : 
        return self.stock

    def get_seller(self) : 
        return self.seller

def get_user(name, list_user):
    for user in list_user:
        if user.get_name() == name:
            return user
    return None

def get_product(name):
    for product in list_product:
        if product.get_name() == name:
            return product
    return None

list_user = []
list_product = []
pemasukan_seller = {}                   # Saya menambah lumayan banyak dict untuk memudahkan saya mengelola data saat transaksi berlangsung
harga_product = {}
stock_product = {}
seller_product = {}
riwayat_pembelian = []

def main():
    print("\nSelamat datang di Dekdepedia!")
    print("Silakan memilih salah satu menu di bawah:")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")

    pilih = input("Pilihan Anda: ")

    if (pilih == "1") : 
        banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))
        print("Data akun: ")
        for i in range (banyak_user) : 
            data_user = input(str(i+1)+". ")
            data_user1 = data_user.split()
            if data_user.startswith('BUYER ') or data_user.startswith('SELLER '):
                if data_user.startswith('BUYER ') and len(data_user1) == 3:
                    if get_user(data_user1[1],list_user) != data_user1[1] :
                        if '-' in data_user1[1]:
                            name = data_user1[1].split('-')
                            if name[0].isalnum() == True and name[1].isalnum() == True:
                                if data_user1[2].isnumeric() == True and int(data_user1[2]) > 0:
                                    data_user1[1] = Buyer(data_user1()[1], data_user1[0], data_user1[2])    # Jika sudah sesuai dengan ketentuan, maka object data buyer akan dibentuk
                                    list_user.append(data_user1[1])
                        elif '_' in data_user1[1]:
                            name = data_user1[1].split('_')
                            if name[0].isalnum() == True and name[1].isalnum() == True:
                                if data_user1[2].isnumeric() == True and int(data_user1[2]) > 0:
                                    data_user1[1] = Buyer(data_user1()[1], data_user1[0], data_user1[2])    # Jika sudah sesuai dengan ketentuan, maka object data buyer akan dibentuk
                                    list_user.append(data_user1[1])
                        elif data_user1[1].isalnum() == True:
                            if data_user1[2].isnumeric() == True and int(data_user1[2]) > 0:
                                    data_user1[1] = Buyer(data_user1[1], data_user1[0], data_user1[2])      # Jika sudah sesuai dengan ketentuan, maka object data buyer akan dibentuk
                                    list_user.append(data_user1[1])
                        else:
                            print('Akun tidak valid')                                                       # Jika input tidak sesuai dengan ketentuan, maka program akan meminta input kembali
                    else:
                        print('Username sudah terdaftar')
                elif data_user.startswith('SELLER') and len(data_user1) == 2:
                    if data_user1[1] not in list_user:
                        if '-' in data_user1[0]:
                            name = data_user1[0].split('-')
                            if name[0].isalnum() == True and name[1].isalnum() == True:
                                data_user1[1] = Seller(data_user1[1], data_user1[0], 0)                     # Jika sudah sesuai dengan ketentuan, maka object data seller akan dibentuk
                                list_user.append(data_user1[1])
                        elif '_' in data_user1[0]:
                            name = data_user1[0].split('_')
                            if name[0].isalnum() == True and name[1].isalnum() == True:
                                data_user1[1] = Seller(data_user1[1], data_user1[0], 0)                     # Jika sudah sesuai dengan ketentuan, maka object data seller akan dibentuk
                                list_user.append(data_user1[1])
                        elif data_user1[1].isalnum() == True:
                            data_user1[1] = Seller(data_user1[1], data_user1[0], 0)                         # Jika sudah sesuai dengan ketentuan, maka object data seller akan dibentuk
                            list_user.append(data_user1[1])
                        else:
                            print('Akun tidak valid')                                                       # Jika input tidak sesuai dengan ketentuan, maka program akan meminta input kembali
                    else:
                        print('Akun tidak valid')
                else:
                    print('Akun tidak valid')
            else:
                print('Akun tidak valid')
        print()
        main()

    elif (pilih == "2") : 
        global user_name_login
        user_name_login = input("user_name : ")
        try:
            user_logged_in = get_user(user_name_login, list_user)
            print("Anda telah masuk dalam akun {} sebagai {}\n".format(user_name_login, user_logged_in.get_tipe()))
            if User.get_tipe(user_logged_in) == "BUYER":
                Buyer.menu(user_logged_in)                                                                  # Jika user seorang buyer maka program akan langsung menuju func menu untuk buyer
            elif User.get_tipe(user_logged_in) == "SELLER":
                Seller.menu(user_logged_in)                                                                 # Jika user seorang seller maka program akan langsung menuju func menu untuk seller
        except AttributeError:
                print("Akun dengan username {} tidak ditemukan".format(user_name_login))                    # Jika user belum terdaftar di program sudah dihandle dan program akan balik ke main menu
                main()

    elif (pilih == "3") : 
        print("Terima kasih telah menggunakan Dekdepedia!")
        exit()

if __name__ == "__main__":
    main()