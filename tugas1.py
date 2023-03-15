import os
os.system('CLS')


class Sekolah:
    def __init__(self, nama, akreditasi, jurusan):
        self.nama = nama
        self.akreditasi = akreditasi
        self.jurusan = jurusan

    def lihat_jadwal(self):
        print(
            f"Jadwal pelajaran untuk {self.nama} dengan akreditasi {self.akreditasi} jurusan {self.jurusan} adalah B.Indonesia")

    def upacara(self):
        print(
            f"Sekolah yang berakreditasi {self.akreditasi} yaitu {self.nama} menugaskan jurusan {self.jurusan} sebagai petugas upacara.")

    def ekstrakulikuler(self):
        print(
            f"Jurusan {self.jurusan} mengikuti lomba ekstrakurikuler di {self.nama} yang berakreditasi {self.akreditasi}.")


nama_sekolah1 = Sekolah('SMAN 1 Bhakti Pertiwi', 'A', 'IPA & IPS')
nama_sekolah2 = Sekolah('SMK 2 MUHAMMADIYAH', 'A', 'Multimedia')

print()
nama_sekolah1.lihat_jadwal()
print()
nama_sekolah2.upacara()
print()
nama_sekolah2.ekstrakulikuler()
