data_mahasiswa = ("1234567890", "John Doe", (80, 75, 85))

nilai_akhir = round(data_mahasiswa[2][0] * 0.3) + (data_mahasiswa[2][1] * 0.3) + (data_mahasiswa[2][2] * 0.4)

print(f"NIM: {data_mahasiswa[0]}")
print(f"Nama: {data_mahasiswa[1]}")
print(f"Nilai Tugas: {data_mahasiswa[2][0]}, Nilai UTS: {data_mahasiswa[2][1]}, Nilai UAS: {data_mahasiswa[2][2]}")
print(f"Nilai Akhir: {nilai_akhir}")

if nilai_akhir >= 70:
    print("Status: Lulus")
else:
    print("Status: Tidak Lulus")