import mysql.connector
from mysql.connector import IntegrityError

class Universitas:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='5220411246'
        )
        self.cursor = self.db.cursor()

class Mahasiswa(Universitas):
    def create(self, npm, nama, jurusan):
        sql = 'INSERT INTO tb_mhs (npm, nama, jurusan) VALUES (%s, %s, %s)'
        value = (npm, nama, jurusan)

        try:
            self.cursor.execute(sql, value)
            self.db.commit()
            print('Data Mahasiswa berhasil disimpan')
        except IntegrityError as e:
            print(f'Data Mahasiswa dengan NPM {npm} sudah ada dalam database.\n')

    def read(self):
        sql = 'SELECT * FROM tb_mhs'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def update(self, npm, nama, jurusan):
        sql = 'UPDATE tb_mhs SET nama=%s, jurusan=%s WHERE npm=%s'
        value = (nama, jurusan, npm)
        self.cursor.execute(sql, value)
        self.db.commit()
        print('Data Mahasiswa berhasil diubah')

    def delete(self, npm):
        sql = 'DELETE FROM tb_mhs WHERE npm=%s'
        value = (npm,)
        self.cursor.execute(sql, value)
        self.db.commit()
        print('Data Mahasiswa berhasil dihapus')

class Dosen(Universitas):
    def create(self, nidn, nama, mata_kuliah):
        sql = 'INSERT INTO tb_dsn (nidn, nama, mata_kuliah) VALUES (%s, %s, %s)'
        value = (nidn, nama, mata_kuliah)

        try:
            self.cursor.execute(sql, value)
            self.db.commit()
            print('Data Dosen berhasil disimpan')
        except IntegrityError as e:
            print(f'Data Dosen dengan NIDN {nidn} sudah ada dalam database.\n')

    def read(self):
        sql = 'SELECT * FROM tb_dsn'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def update(self, nidn, nama, mata_kuliah):
        sql = 'UPDATE tb_dsn SET nama=%s, mata_kuliah=%s WHERE nidn=%s'
        value = (nama, mata_kuliah, nidn)
        self.cursor.execute(sql, value)
        self.db.commit()
        print('Data Dosen berhasil diubah')

    def delete(self, nidn):
        sql = 'DELETE FROM tb_dsn WHERE nidn=%s'
        value = (nidn,)
        self.cursor.execute(sql, value)
        self.db.commit()
        print('Data Dosen berhasil dihapus')

def menu(universitas):
    mahasiswa = Mahasiswa()
    dosen = Dosen()

    print('\n====== PILIH MENU ======')
    print('1. Kelola Data Mahasiswa')
    print('2. Kelola Data Dosen')
    print('3. Keluar')
    print('========================')

    pilihan = int(input('\nMasukkan Pilihan : '))

    if pilihan == 1:
        mahasiswa_menu(mahasiswa)
    elif pilihan == 2:
        dosen_menu(dosen)
    elif pilihan == 3:
        exit("Berhasil Keluar Dari Program\n")
    else:
        print('Pilihan Tidak Ada')

def mahasiswa_menu(mahasiswa):
    print('\n==== MENU MAHASISWA ====')
    print('1. Tambah Data')
    print('2. Tampil Data')
    print('3. Ubah Data')
    print('4. Hapus Data')
    print('5. Kembali ke Menu Utama')
    print('========================')

    menu = int(input('\nMasukkan Menu : '))

    if menu == 1:
        npm = int(input('Masukkan NPM : '))
        nama = input('Masukkan Nama : ')
        jurusan = input('Masukkan Jurusan : ')
        mahasiswa.create(npm, nama, jurusan)

    elif menu == 2:
        data = mahasiswa.read()
        if not data:
            print('Data tidak ada')
        else:
            for row in data:
                print(row)

    elif menu == 3:
        npm = int(input('Masukkan NPM data yang akan diubah : '))
        nama = input('Masukkan Nama : ')
        jurusan = input('Masukkan Jurusan : ')
        mahasiswa.update(npm, nama, jurusan)

    elif menu == 4:
        npm = int(input('Pilih NPM data yang akan dihapus : '))
        mahasiswa.delete(npm)

    elif menu == 5:
        return
    else:
        print('Menu Tidak Ada')

def dosen_menu(dosen):
    print('\n====== MENU DOSEN ======')
    print('1. Tambah Data')
    print('2. Tampil Data')
    print('3. Ubah Data')
    print('4. Hapus Data')
    print('5. Kembali ke Menu Utama')
    print('========================')

    menu = int(input('\nMasukkan Menu : '))

    if menu == 1:
        nidn = int(input('Masukkan NIDN : '))
        nama = input('Masukkan Nama : ')
        mata_kuliah = input('Masukkan Mata Kuliah : ')
        dosen.create(nidn, nama, mata_kuliah)

    elif menu == 2:
        data = dosen.read()
        if not data:
            print('Data tidak ada')
        else:
            for row in data:
                print(row)

    elif menu == 3:
        nidn = int(input('Masukkan NIDN data yang akan diubah : '))
        nama = input('Masukkan Nama : ')
        mata_kuliah = input('Masukkan Mata Kuliah : ')
        dosen.update(nidn, nama, mata_kuliah)

    elif menu == 4:
        nidn = int(input('Pilih NIDN data yang akan dihapus : '))
        dosen.delete(nidn)

    elif menu == 5:
        return
    else:
        print('Menu Tidak Ada')

if __name__ == '__main__':
    universitas = Universitas()
    while True:
        menu(universitas)
