print("Contoh Polymorphims".center(75, "="))


class Mahasiswa1:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def info(self):
        print(
            f"I am a Student. My name is {self.nama}. My NIM is{self.nim}. I am I'm majoring in {self.prodi}")


class Mahasiswa2:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def info(self):
        print(
            f"I am a Student. My name is {self.nama}. My NIM is{self.nim}. I am I'm majoring in {self.prodi}")


mahasiswa1 = Mahasiswa1("Enny Zakiyyah Arisa",
                        "M3119035", "D3 Teknik Informatika")
mahasiswa2 = Mahasiswa2("Gita",
                        "M3119040", "D3 Teknik Informatika")

for person in (mahasiswa1, mahasiswa2):
    person.info()
