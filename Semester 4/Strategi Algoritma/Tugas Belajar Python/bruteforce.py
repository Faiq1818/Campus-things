class Hewan:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def makan(self):
        print(self.nama, " sedang makan...")


class Kucing(Hewan):
    def __init__(self, nama, usia, heterochromia):
        super().__init__(nama, usia)
        self.heterochromia = heterochromia


bubul = Kucing("bubul", 7, "yes")
print(bubul.nama)


# class Sepeda:
#     def __init__(self):
#         self.roda_gigi_saat_ini = 1
#         self.max_kecepatan = 2
#         self.kecepatan = 0
#     def pindah_roda_gigi(self, roda_gigi):
#         pass
#     def menambah_kecepatan(self):
#         self.kecepatan += 1
#     def menurunkan_kecepatan(self):
#         pass
#
# paragon = Sepeda()
# print(paragon.kecepatan)
# paragon.menambah_kecepatan()
# print(paragon.kecepatan)

# class Mobil:
#     def __init__(self, nama, warna):
#         self.nama = nama
#         self.warna = warna

#     def maju(self):
#         print("mobil" + self.nama + "sedang maju")

# alya = Mobil("Alya", "Putih")
# alya.maju()

# a = "a a a a"
# print(len(a))

# def function(param1, param2, param3):


# sisi = 2
# volume = sisi * sisi * sisi
# # print("volume kubus adalah: " + (volume))


# nama = input("nama kamu: ")
# print("halo, " + nama + "!")

# class Mobil:
#     jumlah_mobil = 0

#     def __ini(self):
#         Mobil.jumlah_mobil += 1


# innova = Mobil()
# print(innova.jumlah_mobil)

# avanza = Mobil()
# print(avanza.jumlah_mobil)

# class Mobil:
#     jumlah_mobil = 0  # Variabel kelas
#
#     def __init__(self):
#         Mobil.jumlah_mobil += 1
#
# innova = Mobil()
# print(Mobil.jumlah_mobil)  # Akses langsung melalui kelas
#
# avanza = Mobil()
# print(Mobil.jumlah_mobil)  # Akses langsung melalui kelas
#
# fortuner = Mobil()
# print(Mobil.jumlah_mobil)  # Akses langsung melalui kelas
