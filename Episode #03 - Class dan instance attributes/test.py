class Kucing:
    jumlah_kucing = 0

    def __init__(self, nama):
        self.nama = nama
        Kucing.jumlah_kucing += 1

    @classmethod
    def tampilkan_jumlah(cls):  # class method
        print(f"Total kucing: {cls.jumlah_kucing}")
        
        
k1 = Kucing("Agus")  
k2 = Kucing("Budi")  
k3 = Kucing("Cucur")

print(k1.nama)
k3.tampilkan_jumlah()

