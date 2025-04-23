# Nama: Faiq Ghozy Erlangga
# Nim: 123140139
# Kelas: PBO RB
# Tugas: 4

# di kode saya ini, saya menggunakan access modifier public, karena menggunakan access modifier yang lain tidak terlalu diperlukan

class Lagu:
    def __init__(self, penyanyi: str, judul: str, tahun: int):
        self.penyanyi = penyanyi
        self.judul = judul
        self.tahun = tahun

class Playlist:
    def __init__(self):
        self.daftar_lagu = [  #bersifat public
            Lagu("My Chemical Romance", "I Don't Love You", 2006),
            Lagu("ShibayanRecords", "Fall In the Dark", 2012),
            Lagu("Hindia", "Nabi Palsu", 2023)
        ]
        self.lagu_yang_dimainkan_saat_ini = 0 #bersifat public
    
    def putar_lagu_pertama (self):
        self.lagu_yang_dimainkan_saat_ini = 0
        print(f"Memutar lagu {self.daftar_lagu[self.lagu_yang_dimainkan_saat_ini].judul}")
    
    def putar_lagu_terakhir(self):
        self.lagu_yang_dimainkan_saat_ini = len(self.daftar_lagu) - 1
        print(f"Memutar lagu {self.daftar_lagu[self.lagu_yang_dimainkan_saat_ini].judul}")

    def putar(self):
        print(f"Memutar lagu {self.daftar_lagu[self.lagu_yang_dimainkan_saat_ini].judul}")

    def putar_lagu_selanjutnya(self):
        if(len(self.daftar_lagu) > self.lagu_yang_dimainkan_saat_ini + 1):
            self.lagu_yang_dimainkan_saat_ini += 1
            print(f"Memutar lagu {self.daftar_lagu[self.lagu_yang_dimainkan_saat_ini].judul}")
        else:
            print("Tidak ada lagi lagu selanjutnya")

    def putar_lagu_sebelumnya(self):
        if(self.lagu_yang_dimainkan_saat_ini - 1 >= 0):
            self.lagu_yang_dimainkan_saat_ini -= 1
            print(f"Memutar lagu {self.daftar_lagu[self.lagu_yang_dimainkan_saat_ini].judul}")
        else:
            print("Tidak ada lagi lagu sebelumnya")
    
    def set_lagu(self, nomor):
        if(nomor < 0):
            print("nomor tidak boleh kurang dari 0!")
        elif(nomor - 1 > len(self.daftar_lagu)):
            print("nomor lagu melebihi jumlah lagu!")
        else:
            self.lagu_yang_dimainkan_saat_ini = nomor - 1
            print(f"Mengset dan memutar lagu {self.daftar_lagu[self.lagu_yang_dimainkan_saat_ini].judul}")

    def mencetak_lagu(self):
        print(f"Informasi lagu sekarang:")
        print(f"Judul: {self.daftar_lagu[self.lagu_yang_dimainkan_saat_ini].judul}")
        print(f"Penyanyi: {self.daftar_lagu[self.lagu_yang_dimainkan_saat_ini].penyanyi}")
        print(f"Tahun rilis: {self.daftar_lagu[self.lagu_yang_dimainkan_saat_ini].tahun}")



lagusaya = Playlist()

lagusaya.putar_lagu_pertama()
print("")
lagusaya.putar_lagu_terakhir()
print("")
lagusaya.putar()
print("")
lagusaya.putar_lagu_sebelumnya()
print("")
lagusaya.putar_lagu_selanjutnya()
print("")
lagusaya.putar_lagu_selanjutnya()
print("")
lagusaya.putar_lagu_selanjutnya()
print("")
lagusaya.putar_lagu_selanjutnya()
print("")
lagusaya.set_lagu(1)
print("")
lagusaya.mencetak_lagu()