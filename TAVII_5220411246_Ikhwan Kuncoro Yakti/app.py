class RumahSakit:
    def __init__(self, nama, umur):
        self._nama = nama
        self.__umur = umur

    def get_nama(self):
        return self._nama

    def set_nama(self, nama):
        self._nama = nama

    def get_umur(self):
        return self.__umur

    def set_umur(self, umur):
        self.__umur = umur

    def info_kesehatan(self):
        return f"|| Nama : {self._nama} \n|| Umur : {self.__umur}"


class Dokter(RumahSakit):
    def __init__(self, nama, umur, spesialisasi):
        super().__init__(nama, umur)
        self._spesialisasi = spesialisasi

    def get_spesialisasi(self):
        return self._spesialisasi

    def set_spesialisasi(self, spesialisasi):
        self._spesialisasi = spesialisasi

    def info_kesehatan(self):
        return super().info_kesehatan() + f"\n|| Spesialisasi : {self._spesialisasi}"


class Pasien(RumahSakit):
    def __init__(self, nama, umur, penyakit):
        super().__init__(nama, umur)
        self._penyakit = penyakit

    def get_penyakit(self):
        return self._penyakit

    def set_penyakit(self, penyakit):
        self._penyakit = penyakit

    def info_kesehatan(self):
        return super().info_kesehatan() + f"\n|| Penyakit : {self._penyakit}"


class PasienAnak(Pasien):
    def __init__(self, nama, umur, penyakit):
        super().__init__(nama, umur, penyakit)
        self._dokter = None

    def set_dokter(self, dokter):
        self._dokter = dokter

    def get_dokter(self):
        return self._dokter

    def info_kesehatan(self):
        dokter_info = "Belum ada informasi dokter." if self._dokter is None else self._dokter.info_kesehatan()
        kategori_usia = "Anak" if self.get_umur() < 15 else "Dewasa" if self.get_umur() < 50 else "Lansia"
        return super().info_kesehatan() + f"\n|| Pasien : {kategori_usia}\n||==========================||\n|| Dokter yang merawat :\n||==========================||\n{dokter_info}\n||==========================||"


class PasienDewasa(Pasien):
    def __init__(self, nama, umur, penyakit):
        super().__init__(nama, umur, penyakit)
        self._dokter = None

    def set_dokter(self, dokter):
        self._dokter = dokter

    def get_dokter(self):
        return self._dokter

    def info_kesehatan(self):
        dokter_info = "Belum ada informasi dokter." if self._dokter is None else self._dokter.info_kesehatan()
        kategori_usia = "Anak" if self.get_umur() < 15 else "Dewasa" if self.get_umur() < 50 else "Lansia"
        return super().info_kesehatan() + f"\n|| Pasien : {kategori_usia}\n||==========================||\n|| Dokter yang merawat :\n||==========================||\n{dokter_info}\n||==========================||"


class PasienLansia(Pasien):
    def __init__(self, nama, umur, penyakit):
        super().__init__(nama, umur, penyakit)
        self._dokter = None

    def set_dokter(self, dokter):
        self._dokter = dokter

    def get_dokter(self):
        return self._dokter

    def info_kesehatan(self):
        dokter_info = "Belum ada informasi dokter." if self._dokter is None else self._dokter.info_kesehatan()
        kategori_usia = "Anak" if self.get_umur() < 15 else "Dewasa" if self.get_umur() < 50 else "Lansia"
        return super().info_kesehatan() + f"\n|| Pasien : {kategori_usia}\n||==========================||\n|| Dokter yang merawat :\n||==========================||\n{dokter_info}\n||==========================||"


def display_data(data):
    if not data:
        print("Belum ada data pasien.\n")
    else:
        print("\n||====== Data Pasien =======||")
        for i, pasien in enumerate(data, start=1):
            print("\n||==========================||")
            print(f"|| Data Pasien ke-{i} :")
            print("||==========================||")
            print(pasien.info_kesehatan())


def edit_data(data):
    if not data:
        print("Belum ada data pasien untuk diedit.\n")
        return
    display_data(data)

    choice = int(input("\nMasukkan nomor data pasien yang ingin diedit : "))
    if 1 <= choice <= len(data):
        pasien = data[choice - 1]

        if isinstance(pasien, PasienAnak):
            print("\n||========== Menu Update Data Pasien ==========||")
            new_nama = input("  Masukkan nama baru : ")
            new_umur = int(input("  Masukkan umur baru : "))
            new_penyakit = input("  Masukkan penyakit baru : ")

            pasien.set_nama(new_nama)
            pasien.set_umur(new_umur)
            pasien.set_penyakit(new_penyakit)
            kategori_usia = "Anak" if new_umur < 15 else "Dewasa" if new_umur < 50 else "Lansia"

            print(f"  Data pasien {kategori_usia} berhasil diubah.")
            print("||=============================================||\n")

        elif isinstance(pasien, PasienDewasa):
            print("\n||========== Menu Update Data Pasien ==========||")
            new_nama = input("  Masukkan nama baru : ")
            new_umur = int(input("  Masukkan umur baru : "))
            new_penyakit = input("  Masukkan penyakit baru : ")

            pasien.set_nama(new_nama)
            pasien.set_umur(new_umur)
            pasien.set_penyakit(new_penyakit)
            kategori_usia = "Anak" if new_umur < 15 else "Dewasa" if new_umur < 50 else "Lansia"

            print(f"  Data pasien {kategori_usia} berhasil diubah.")
            print("||=============================================||\n")

        elif isinstance(pasien, PasienLansia):
            print("\n||========== Menu Update Data Pasien ==========||")
            new_nama = input("  Masukkan nama baru : ")
            new_umur = int(input("  Masukkan umur baru : "))
            new_penyakit = input("  Masukkan penyakit baru : ")

            pasien.set_nama(new_nama)
            pasien.set_umur(new_umur)
            kategori_usia = "Anak" if new_umur < 15 else "Dewasa" if new_umur < 50 else "Lansia"

            print(f"  Data pasien {kategori_usia} berhasil diubah.")
            print("||=============================================||\n")

    else:
        print("Nomor data tidak valid.")


def delete_data(data):
    if not data:
        print("Belum ada data pasien untuk dihapus.\n")
        return

    display_data(data)

    choice = int(input("\nMasukkan nomor data pasien yang ingin dihapus : "))
    if 1 <= choice <= len(data):
        removed_pasien = data.pop(choice - 1)
        print(f"Data pasien ke-{choice} berhasil dihapus :\n\n||==========================||\n{removed_pasien.info_kesehatan()}\n")
    else:
        print("Nomor data tidak valid.")


def main():
    data_pasien = []

    while True:
        print("\n||========== Menu ==========||")
        print("|| 1. Pasien Anak           ||")
        print("|| 2. Pasien Dewasa         ||")
        print("|| 3. Pasien Lansia         ||")
        print("|| 4. Tampilkan Data Pasien ||")
        print("|| 5. Edit Data Pasien      ||")
        print("|| 6. Hapus Data Pasien     ||")
        print("|| 7. Keluar                ||")
        print("||==========================||")

        choice = input("\nMasukkan pilihan -|1|2|3|4|5|6|7|- : ")

        if choice == "1":
            print("\n||========== Menu Pasien Anak ==========||")
            nama = input("  Masukkan nama anak : ")
            umur = int(input("  Masukkan umur anak : "))
            penyakit = input("  Masukkan penyakit anak : ")

            dokter_nama = input("  Masukkan nama dokter : ")
            dokter_umur = int(input("  Masukkan umur dokter : "))
            dokter_spesialisasi = input("  Masukkan spesialisasi dokter : ")

            dokter = Dokter(dokter_nama, dokter_umur, dokter_spesialisasi)
            pasien_anak = PasienAnak(nama, umur, penyakit)
            pasien_anak.set_dokter(dokter)

            data_pasien.append(pasien_anak)
            print(f"  Data pasien anak berhasil ditambahkan.")
            print("||======================================||")

        elif choice == "2":
            print("\n||========== Menu Pasien Dewasa ==========||")
            nama = input("  Masukkan nama : ")
            umur = int(input("  Masukkan umur : "))
            penyakit = input("  Masukkan penyakit : ")

            dokter_nama = input("  Masukkan nama dokter : ")
            dokter_umur = int(input("  Masukkan umur dokter : "))
            dokter_spesialisasi = input("  Masukkan spesialisasi dokter : ")

            dokter = Dokter(dokter_nama, dokter_umur, dokter_spesialisasi)
            pasien_dewasa = PasienDewasa(nama, umur, penyakit)
            pasien_dewasa.set_dokter(dokter)

            data_pasien.append(pasien_dewasa)
            print("  Data pasien dewasa berhasil ditambahkan.")
            print("||========================================||")

        elif choice == "3":
            print("\n||========== Menu Pasien Lansia ==========||")
            nama = input("  Masukkan nama lansia : ")
            umur = int(input("  Masukkan umur lansia : "))
            penyakit = input("  Masukkan penyakit lansia : ")

            dokter_nama = input("  Masukkan nama dokter : ")
            dokter_umur = int(input("  Masukkan umur dokter : "))
            dokter_spesialisasi = input("  Masukkan spesialisasi dokter : ")

            dokter = Dokter(dokter_nama, dokter_umur, dokter_spesialisasi)
            pasien_lansia = PasienLansia(nama, umur, penyakit)
            pasien_lansia.set_dokter(dokter)

            data_pasien.append(pasien_lansia)
            print("  Data pasien lansia berhasil ditambahkan.")
            print("||========================================||")

        elif choice == "4":
            display_data(data_pasien)

        elif choice == "5":
            edit_data(data_pasien)

        elif choice == "6":
            delete_data(data_pasien)

        elif choice == "7":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")


if __name__ == "__main__":
    main()