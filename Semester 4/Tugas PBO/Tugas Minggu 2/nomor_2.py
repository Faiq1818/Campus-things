def tambah_transaksi(tanggal, jenis, jumlah):
    transaksi.append([tanggal, jenis, jumlah])

def hitung_total():
    total_pemasukan = 0
    total_pengeluaran = 0
    for x in transaksi:
        if x[1] == "Pemasukan":
            total_pemasukan = total_pemasukan + x[2]
        elif x[1] == "Pengeluaran":
            total_pengeluaran = total_pengeluaran + x[2]

    print("Total pemasukan:", total_pemasukan)
    print("Total pengeluaran:", total_pengeluaran)
    print("")

def tampilkan_transaksi_terbesar_terkecil():
    max_transaksi = transaksi[2]
    min_transaksi = transaksi[2]

    for x in transaksi:
        jumlah = x[2]
        if jumlah > max_transaksi[2]:
            max_transaksi = x
        if jumlah < min_transaksi[2]:
            min_transaksi = x 
    print("Transaksi Terbesar:")
    print("- Tanggal:", max_transaksi[0], "Kategori:", max_transaksi[1], "Jumlah:", max_transaksi[2])
    print("")
    print("Transaksi Terkecil:")
    print("- Tanggal:", min_transaksi[0], "Kategori:", min_transaksi[1], "Jumlah:", min_transaksi[2])

def urutkan_transaksi():
    

transaksi = []

tambah_transaksi("01-10-2023", "Pemasukan", 300000)
tambah_transaksi("02-10-2023", "Pengeluaran", 150000)
tambah_transaksi("03-10-2023", "Pemasukan", 500000)

hitung_total()

tampilkan_transaksi_terbesar_terkecil()