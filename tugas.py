import sqlite3

class Tugas:
    def __init__(self):
        self.__conn = sqlite3.connect("BotDiscord.db")
        self.__cursor = self.__conn.cursor()

    def TampilData(self):
        self.__cursor.execute("SELECT * FROM tugas")
        data = self.__cursor.fetchall()
        print("\n=====Daftar Tugas=====")
        for row in data:

            if row[4] == 0:
                print(row[0], row[1], row[2], row[3],"Belum di kerjakan")

            elif row[4] == 1:
                print(row[0], row[1], row[2], row[3], "Sudah di kerjakan")

    def TambahData(self, judul, deskripsi, tanggal, status):
        self.__cursor.execute("INSERT INTO tugas (judul, deskripsi, tanggal, status) VALUES ('"+ judul +"', '"+ deskripsi +"', '"+ tanggal +"', '"+ status +"')")
        self.__conn.commit()
        print("Data Tersimpan")


    def HapusData(self, judul):
        self.__cursor.execute("DELETE FROM tugas WHERE judul = '" + judul + "'")
        self.__conn.commit()
        print("Data Terhapus")

    def UbahData(self,judul, deskripsi, tanggal):
        self.__cursor.execute("UPDATE tugas SET judul = '" + judul + "', deskripsi = '"+ deskripsi +"', tanggal = '"+ tanggal +"' WHERE judul = '" + judul + "'")
        self.__conn.commit()
        print("Data Di ubah")

    def UbahStatus(self, judul, status):
        self.__cursor.execute(
            "UPDATE tugas SET status = '" + status + "' WHERE judul = '" + judul + "'")
        self.__conn.commit()
        print("Status Di ubah")

