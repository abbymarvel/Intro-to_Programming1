import string
import random

print("Program untuk membuat word cloud dari text file\n---------------------------------------------")
print("hasilnya disimpan sebagai file html, \nyang bisa ditampilkan di browser.\n")


def start():  # Function start() adalah function utama dari program ini
    global input_file  # (global_input) digunakan agar input_file bisa digunakan di luar func
    input_file = input("Silakan masukan nama file: ")
    try:  # try digunakan untuk memastikan file input ada dan tidak kosong
        text = open(input_file, "r").read().split()
        stop_words = open("stopwords.txt", "r").read().split()
        stop_words.append("")
        if len(text) == 0:
            print("\n File input ada tapi kosong :(")
            input("Program selesai. Tekan enter untuk keluar...")
            exit()
        else:
            global hasil
            global counter
            global highest
            global lowest
            counter = {}  # dict counter digunakan untuk menghitung kata
            for word in text:
                word = word.lower()
                word = word.strip(string.punctuation)   # strip untuk membersihkan text dari punctuation
                if word in stop_words:
                    continue                            # jika ada stop words di text maka tidak terhitung di counter
                elif word not in counter:
                    counter[word] = 0
                counter[word] += 1
            hasil = {k: v for k, v in sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)[:56]}
            hasil = dict(sorted(hasil.items(), key=lambda x: x[0])) # mengurutkan 56 kata paling atas dari a-z
            highest = max(hasil.values())
            lowest = min(hasil.values())
            printing()
            main()
            input("\nTekan Enter untuk keluar …")

    except FileNotFoundError:  # except untuk handle filenotfounderror
        print("File input tidak ada :(\n")
        start()


def printing():  # function printing untuk ngeprint dengan output format yang ditentukan
    print("\n56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan\n(jumlah:kata) \n")
    words = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56]
    for word in words:
        for key in {k: v for k, v in sorted(counter.items(), key=lambda item: (item[1], item[0]),
                                            reverse=True)[(word - 4):word]}:
            print("{:>2d}:{:<13s}".format({k: v for k, v in sorted(counter.items(), key=lambda item: (item[1], item[0]),
                                                                   reverse=True)[word - 4: word]}[key], key), end="\t")
        print()


def make_HTML_word(word, cnt, high, low):
    '''
    Make a word with a font size and a random color.
    Font size is scaled between html_big and html_little (to be user set).
    high and low represent the high and low counts in the document.
    cnt is the count of the word.
    Required -- word (string) to be formatted
             -- cnt (int) count of occurrences of word
             -- high (int) highest word count in the document
             -- low (int) lowest word count in the document
    Return -- a string formatted for HTML that is scaled with respect to cnt
    '''
    html_big = 96
    html_little = 14
    if high != low:
        ratio = (cnt - low) / float(high - low)
    else:
        ratio = 0
    font_size = html_big * ratio + (1 - ratio) * html_little
    font_size = int(font_size)
    rgb = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    word_str = '<span style=\"color: rgb{}; font-size:{:s}px;\">{:s}</span>'
    return word_str.format(rgb, str(font_size), word)


def make_HTML_box(body):
    '''
    Take one long string of words and put them in an HTML box.
    If desired, width, background color & border can be changed in the function
    This function stuffs the "body" string into the the HTML formatting string.

    Required -- body (string), a string of words
    Return -- a string that specifies an HTML box containing the body
    '''
    box_str = """<div style=\"
    width: 560px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center\" >{:s}</div>
    """
    return box_str.format(body)


def print_HTML_file(body, title):
    '''
    Create a standard html page (file) with titles, header etc.
    and add the body (an html box) to that page. File created is title+'.html'
    Required -- body (string), a string that specifies an HTML box
    Return -- nothing
    '''
    fd = open(title + '.html', 'w')
    the_str = """
    <html> <head>
    <title>""" + title + """</title>
    </head>

    <body>
    <h1>""" + 'A Word Cloud of ' + title + '</h1>' + '\n' + body + '\n' + """<hr>
    </body> </html>
    """
    fd.write(the_str)
    fd.close()


def main():
    pairs = hasil.items()
    high_count = highest
    low_count = lowest
    body = ''
    for word, cnt in pairs:
        body = body + " " + make_HTML_word(word, cnt, high_count, low_count)
    box = make_HTML_box(body)  # creates HTML in a box
    # writes HTML to file name 'testFile.html'
    print_HTML_file(box, input_file)


start()
