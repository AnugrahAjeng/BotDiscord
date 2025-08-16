
from tugas import Tugas

obj = Tugas ()

kondisi = True
while kondisi:
    print("=====Menu=====")
    print("1. Tampil Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Ubah Status")
    print("5. Hapus Data")
    print("6. Keluar")
    pil = input("Pilihan : ")
    if pil == "1":
        obj.TampilData()

    elif pil == "2":
        judul = input("Judul : ")
        deskripsi = input("Deskripsi : ")
        tanggal = input("tanggal : ")
        status = "0"

        obj.TambahData(judul, deskripsi, tanggal, status)

    elif pil == "5":
        judul = input("Judul yang ingin dihapus : ")
        obj.HapusData(judul)

    elif pil == "3":
        judul = input("Judul : ")
        deskripsi = input("Deskripsi : ")
        tanggal = input("tanggal : ")

        obj.UbahData(judul, deskripsi, tanggal)

    elif pil == "4":
        judul = input("Judul : ")
        status = input("status : ")

        obj.UbahStatus(judul, status)

    elif pil == "6":
        kondisi = False



