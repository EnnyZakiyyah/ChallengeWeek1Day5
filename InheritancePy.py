print("Contoh Inheritance dan Encapsulation".center(75, "="))


class Mahasiswa:
    def __init__(self, fnama, lnim, mprodi):
        self.firstnama = fnama
        self.lastnim = lnim
        self.mahasiswaaprodi = mprodi

    def printmahasiswa(self):
        print(self.firstnama, self.lastnim, self.mahasiswaaprodi)

# Use the Person class to create an object, and then execute the printname method:


x = Mahasiswa("Enny, ", "35, ", "D3 Teknik Informatika")
x.printmahasiswa()
