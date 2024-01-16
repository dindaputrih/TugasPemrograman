class Helm:
    def__init__(self, merk, harga, stok):
        self.merk = merk
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"Merk: {self.merk}, Harga: {self.harga} USD, Stok: {self.stok} unit")

def beli_helm(helm, jumlah):
    if helm.stok >= jumlah:
        total_harga = helm.harga * jumlah
        helm.stok -= jumlah
        return f"Anda telah membeli {jumlah} unit {helm.merk}. Total harga: {total_harga} USD."
    else:
        return f"Maaf, stok {helm.merk} tidak mencukupi untuk pembelian ini."

def main():
    daftar_helm = [
        Helm("KYT", 80, 15),
        Helm("INK", 100, 10),
        Helm("NHK", 120, 8),
        Helm("Gm",300, 15),
        Helm("zeus", 400, 25)
    ]

    while True:
        print("\nMenu:")
        print("1. Tampilkan Helm")
        print("2. Beli Helm")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            print("\nDaftar Helm:")
            for helm in daftar_helm:
                helm.tampilkan_info()
        elif pilihan == "2":
            merk_helm = input("Masukkan merk helm yang ingin dibeli: ")
            helm_terpilih = next((helm for helm in daftar_helm if helm.merk.lower() == merk_helm.lower()), None)

            if helm_terpilih:
                jumlah_pembelian = int(input(f"Masukkan jumlah {helm_terpilih.merk} yang ingin dibeli: "))
                hasil_pembelian = beli_helm(helm_terpilih, jumlah_pembelian)
                print(hasil_pembelian)
            else:
                print("Merk helm tidak ditemukan.")
        elif pilihan == "3":
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name_ == "main_":
    main()
