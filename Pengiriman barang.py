import csv
import os

CSV_FILE = 'pengiriman.csv'

# Inisialisasi file jika belum ada
def init_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id',  'nama_pengirim',  'nama_penerima',  'alamat_tujuan',  'jenis_barang',  'status'])

# Tambah pengiriman baru
def tambah_pengiriman():
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        id = input("Masukkan ID pengiriman: ")
        nama_pengirim = input("Masukkan nama pengirim: ")
        nama_penerima = input("Masukkan nama penerima: ")
        alamat_tujuan = input("Masukkan alamat tujuan: ")
        jenis_barang = input("Masukkan jenis barang: ")
        status = input("Masukkan status (Dikirim/Diterima): ")
        writer.writerow([id, nama_pengirim, nama_penerima, alamat_tujuan, jenis_barang, status])
        print("✅ Data pengiriman berhasil ditambahkan!")

# Lihat semua pengiriman
def lihat_pengiriman():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print("\n--- Daftar Pengiriman ---")
        for row in reader:
            print(row)

# Cari pengiriman berdasarkan ID
def cari_pengiriman():
    cari_id = input("Masukkan ID pengiriman yang dicari: ")
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        found = False
        for row in reader:
            if row['id'] == cari_id:
                print("✅ Data ditemukan:")
                print(row)
                found = True
                break
        if not found:
            print("❌ Data tidak ditemukan.")

# Hapus data pengiriman berdasarkan ID
def hapus_pengiriman():
    id_hapus = input("Masukkan ID pengiriman yang ingin dihapus: ")
    rows = []
    deleted = False
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] != id_hapus:
                rows.append(row)
            else:
                deleted = True
    if deleted:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nama_pengirim', 'nama_penerima', 'alamat_tujuan', 'jenis_barang', 'status'])
            writer.writeheader()
            writer.writerows(rows)
        print("✅ Data berhasil dihapus.")
    else:
        print("❌ Data dengan ID tersebut tidak ditemukan.")

# Menu utama
def menu():
    init_file()
    while True:
        print("\n=== Aplikasi Pengiriman Barang ===")
        print("1. Tambah Pengiriman")
        print("2. Lihat Semua Pengiriman")
        print("3. Cari Pengiriman berdasarkan ID")
        print("4. Hapus Pengiriman")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_pengiriman()
        elif pilihan == '2':
            lihat_pengiriman()
        elif pilihan == '3':
            cari_pengiriman()
        elif pilihan == '4':
            hapus_pengiriman()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu()
