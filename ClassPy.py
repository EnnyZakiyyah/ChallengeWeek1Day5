print("Contoh Class".center(75, "="))


class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi


p1 = Mahasiswa("Enny Zakiyyah Arisa", "M3119035", "D3 Teknik Informatika")

print(p1.nama)
print(p1.nim)
print(p1.prodi)

