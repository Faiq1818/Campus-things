def tambah_data(nim, nama, nilai_mata_kuliah):
    mahasiswa[nim] = {
        "Nama": nama,
        "Nilai Mata Kuliah": nilai_mata_kuliah
    }

def cari_nilai_akhir(nim, nama_mata_kuliah):
    nama = mahasiswa[nim]["Nama"]
    x1 = mahasiswa[nim]["Nilai Mata Kuliah"][nama_mata_kuliah][0]
    x2 = mahasiswa[nim]["Nilai Mata Kuliah"][nama_mata_kuliah][1]
    x3 = mahasiswa[nim]["Nilai Mata Kuliah"][nama_mata_kuliah][2]

    nilai_ratarata = (x1 + x2 + x3) / 3
    nilai_ratarata_bulat = round(nilai_ratarata, 1)

    print("nilai akhir", nama, "untuk mata kuliah", nama_mata_kuliah, ":", nilai_ratarata_bulat)

def tampilkan_mahasiswa_diatas_80(nama_mata_kuliah):
    print("Mahasiswa dengan nilai akhir di atas 80 untuk mata kuliah Algoritma:")
    for nim, data in mahasiswa.items():
        x1 = mahasiswa[nim]["Nilai Mata Kuliah"][nama_mata_kuliah][0]
        x2 = mahasiswa[nim]["Nilai Mata Kuliah"][nama_mata_kuliah][1]
        x3 = mahasiswa[nim]["Nilai Mata Kuliah"][nama_mata_kuliah][2]

        nilai_ratarata = (x1 + x2 + x3) / 3
        nilai_ratarata_bulat = round(nilai_ratarata, 1)
        if nilai_ratarata_bulat > 80:
            print(mahasiswa[nim]["Nama"], ":", nilai_ratarata_bulat)



mahasiswa = {}

tambah_data("1234567890", "John Doe", {"Algoritma": [85, 90, 88], "Struktur Data": [78, 85, 80]})
tambah_data("0987654321", "Doe John", {"Algoritma": [85, 90, 88], "Struktur Data": [78, 85, 80]})
cari_nilai_akhir("1234567890", "Algoritma")
tampilkan_mahasiswa_diatas_80("Algoritma")
