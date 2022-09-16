import tkinter as tk
import tkinter.messagebox as tkmsg


class MainWindow(tk.Frame):

    def __init__(self, master = None, digit = 0):
        super().__init__(master)
        self.namafile = tk.StringVar()
        self.code = tk.StringVar()
        self.master.geometry('350x380')
        self.digit = digit
        self.list_code = {}     # table encoding EAN-13 di soal saya masukan ke dalam dict agar mudah untuk digunakan 
        self.digit_group = {0: 'LLLLLL', 1: 'LLGLGG', 2: 'LLGGLG', 3: 'LLGGGL', 4: 'LGLLGG', 5: 'LGGLLG', 6: 'LGGGLL', 7: 'LGLGLG', 8: 'LGLGGL', 9: 'LGGLGL'}
        self.encoding_l = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011', 5: '0110001', 6: '0101111', 7: '0111011', 8: '0110111', 9: '0001011'}
        self.encoding_g = {0: '0100111', 1: '0110011', 2: '0011011', 3: '0100001', 4: '0011101', 5: '0111001', 6: '0000101', 7: '0010001', 8: '0001001', 9: '0010111'}
        self.encoding_r = {0: '1110010', 1: '1100110', 2: '1101100', 3: '1000010', 4: '1011100', 5: '1001110', 6: '1010000', 7: '1000100', 8: '1001000', 9: '1110100'}
        self.pack()
        self.create_widgets()
    
    def check_filename(self, event):            # Func ini untuk memastikan input nama file sesuai
        namafile = self.namafile.get()
        if str(namafile).endswith(".eps"):      # Jika input nama file sudah sesuai maka program akan lanjut ke func check digit
            pass
        else:                               # Jika tidak sesuai maka akan muncul messagebox
            self.widgets_name_error("Please enter correct input PS file.") 
    
    def check_digit(self, event):               # Func ini untuk memastikan jumlah input code barcode sesuai
        code = self.code.get()
        checksum = 0
        if len(str(code)) == 12:                # Jika input code barcode sudah sesuai maka program akan lanjut ke func check digit
            for i in range(12):
                if (i+1)%2 == 0:
                    checksum += int(str(code)[i]) * 3
                elif (i+1)%2 == 1:
                    checksum += int(str(code)[i])
                self.list_code[i+1] = int(str(code)[i])
            x = checksum % 10
            if x != 0:
                self.digit = 10-x
            else:
                self.digit = x
            self.encoding = ''
            self.barcode()
        elif len(str(code)) != 12:          # Jika tidak sesuai maka akan muncul messagebox
            self.widgets_name_error("Please enter correct input code.")
    
    def widgets_name_error(self, text):
        tkmsg.showerror(title="Wrong input!", message=text) # Handler jika ada input yang tidak sesuai
    
    def create_widgets(self):                   # Func ini untuk membuat widgets yang ada di window
        self.label_file = tk.Label(self, text = 'Save barcode to PS file [Eg: EAN13.eps]:', font='Helvetica 12 bold')
        self.label_file.grid(row=1)
        self.inp_file = tk.Entry(self, textvariable=self.namafile, font=12)             
        self.inp_file.grid(row=2)
        self.label_code = tk.Label(self, text = 'Enter code (first 12 decimal digits):', font='Helvetica 12 bold')
        self.label_code.grid(row=3)
        self.inp_code = tk.Entry(self, textvariable=self.code, font=12)
        self.inp_code.grid(row=4)
        self.canvas = tk.Canvas(self, width=240, height=280, bg="white")
        self.canvas.grid(row=5)
        self.inp_file.bind('<Return>', self.check_filename) # Jika user menekan enter di widget self.inp_file maka program akan menjalankan func check_filename
        self.inp_code.bind('<Return>', self.check_digit)    # Jika user menekan enter di widget self.inp_code maka program akan menjalankan func check_digit
    
    def create_barcode(self, num, x):       # Func ini untuk mencetak garis barcode dari group L, G, dan R
        if num == '0':
            pass
        elif num == '1':
            self.canvas.create_rectangle(x, 100, x+1, 190, fill='sky blue', outline='sky blue')
    
    def create_barcode_sme(self, num, x):   # Func ini untuk mencetak garis barcode dari group S, M, dan E
        if num == '0':
            pass
        elif num == '1':
            self.canvas.create_rectangle(x, 100, x+1, 200, fill='hot pink', outline='hot pink')

    def barcode(self):
        self.canvas.delete("all")                                       # Agar canvas reset lagi saat user memasukan input code selanjutnya
        first_digit = self.list_code[1]
        group = self.digit_group[first_digit]
        self.encoding+='101'                                            # Encoding version dari code barcode input akan disimpan di list self.encoding
        for i  in range(1,7):
            if group[i-1] == 'L':
                self.encoding += self.encoding_l[self.list_code[i+1]]
            elif group[i-1] == 'G':
                self.encoding += self.encoding_g[self.list_code[i+1]]
        self.encoding += '01010'
        for i in range(7,12):
            self.encoding += self.encoding_r[self.list_code[i+1]]
        self.encoding += self.encoding_r[self.digit]
        self.encoding+='101'
        x = 26
        for num in self.encoding[:3]:                                   # self.encoding harus di slicing dan diproses di beberapa for loop yang berbeda,
            self.create_barcode_sme(num, x)                             # unutk membedakan warna dan panjang barcode line yang berasal dari group S, M, dan E
            x+=2
        for num in self.encoding[3:45]:
            self.create_barcode(num, x)
            x+=2
        for num in self.encoding[45:49]:
            self.create_barcode_sme(num, x)
            x+=2
        for num in self.encoding[49:92]:
            self.create_barcode(num, x)
            x+=2
        for num in self.encoding[92:]:
            self.create_barcode_sme(num, x)
            x+=2
        self.canvas.create_text(120, 80, text="EAN-13 Barcode:", fill="black", font=('Helvetica 12 bold'))
        self.canvas.create_text(18, 205, text=first_digit, fill="black", font=('Helvetica 12 bold'))
        x = 42
        for num in self.code.get()[1:7]:
            self.canvas.create_text(x, 205, text=num, fill="black", font=('Helvetica 12 bold'))
            x +=13
        x = 135
        for num in self.code.get()[7:12]:
            self.canvas.create_text(x, 205, text=num, fill="black", font=('Helvetica 12 bold'))
            x +=13
        self.canvas.create_text(200, 205, text=self.digit, fill="black", font=('Helvetica 12 bold'))
        self.canvas.create_text(120, 235, text=f"Check Digit: {self.digit}", fill="orange red", font=('Helvetica 12 bold'))
        self.canvas.postscript(file = self.namafile.get())              # Gambar barcode disimpan sebagai PostScript file.

def main():
    m = MainWindow()
    m.master.title("EAN-13")
    m.master.mainloop()

if __name__ == "__main__":
    main()