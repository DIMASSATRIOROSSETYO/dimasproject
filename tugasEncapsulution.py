import os
os.system('CLS')

class Sekolah:
    def __init__(self, nama, akreditasi, jurusan):
        self.__nama = nama
        self.__akreditasi = akreditasi
        self.__jurusan = jurusan

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_akreditasi(self):
        return self.__akreditasi

    def set_akreditasi(self, akreditasi):
        self.__akreditasi = akreditasi

    def get_jurusan(self):
        return self.__jurusan

    def set_jurusan(self, jurusan):
        self.__jurusan = jurusan


sekolah1 = Sekolah('SMA 1 SURAKARTA', 'A', 'IPA & IPS')
print(sekolah1.get_nama())
print(sekolah1.get_akreditasi())
print(sekolah1.get_jurusan())

sekolah1.set_nama('SMK MUHAMMADIYAH 2 KLATEN')
sekolah1.set_akreditasi('A')
sekolah1.set_jurusan('Multimedia')

print(sekolah1.get_nama())
print(sekolah1.get_akreditasi())
print(sekolah1.get_jurusan())