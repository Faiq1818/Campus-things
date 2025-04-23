#Nama : Faiq Ghozy Erlangga
#NIM : 12130149
#Kelas : Praktikum PBO RB
#Tugas : Latihan 4

class Buku:
    def __init__(self, judul, tahun, pengarang): #membuat class buku dengan atributnya
        self.judul = judul
        self.tahun = tahun
        self.pengarang = pengarang

    def __str__(self):
        return f"{self.judul} ({self.tahun}) oleh {self.pengarang}"


class Katalog: #membuat class katalog dengan atribut dan methode seperti menambah buku, mencari buku, dll
    def __init__(self):
        self.books = []

    def tambah_buku(self): #methode untuk menambahkan buku
        try:
            judul = input("Judul: ") #menggunakan error handling
            tahun = int(input("Tahun: "))
            pengarang = input("Pengarang: ")
            self.books.append(Buku(judul, tahun, pengarang))
            print("Buku sudah ditambahkan\n")
        except ValueError: #akan mengembalikan exception jika value input tidak sesuai jenis tipe data
            print("Tahun harus angka\n")

    def tampilkan_buku(self): #methode untuk menampilkan buku
        if not self.books:
            print("Katalog masih kosong\n")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")
            print()

    def cari_buku(self): #methode untuk mencari buku
        query = input("Judul buku yang dicari: ").lower()
        found = False
        for book in self.books:
            if query in book.judul.lower():
                print(book)
                found = True
        if not found:
            print("Buku tidak ada\n")
        else:
            print()

def Logika_perulangan():
    katalog = Katalog() # menu pilihan dengan looping
    while True:
        print("Pilih menu")
        print(" --- 1. Tambah buku --- 2. Tampilkan buku --- 3. Cari buku --- 4. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            katalog.tambah_buku()
        elif pilih == "2":
            katalog.tampilkan_buku()
        elif pilih == "3":
            katalog.cari_buku()
        elif pilih == "4":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid\n")


Logika_perulangan()