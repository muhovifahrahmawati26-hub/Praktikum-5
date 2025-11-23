# =======================================
# Program Daftar Nilai Mahasiswa (Dictionary)
# =======================================

mahasiswa = {}  # {nim: {"nama":..., "tugas":..., "uts":..., "uas":..., "akhir":...}}

# --------------------------
# Fungsi Hitung Nilai Akhir
# --------------------------
def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

# --------------------------
# Tambah Data
# --------------------------
def tambah_data():
    print("\nTambah Data")
    nim = input("NIM          : ")
    nama = input("Nama         : ")
    tugas = float(input("Nilai Tugas  : "))
    uts = float(input("Nilai UTS    : "))
    uas = float(input("Nilai UAS    : "))

    akhir = hitung_nilai_akhir(tugas, uts, uas)

    mahasiswa[nim] = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }

    print("\n✔ Data berhasil ditambahkan!\n")

# --------------------------
# Ubah Data (fleksibel)
# --------------------------
def ubah_data():
    nim = input("Masukkan NIM yang akan diubah: ")

    if nim not in mahasiswa:
        print("✘ Data tidak ditemukan!\n")
        return

    data = mahasiswa[nim]
    print(f"Data ditemukan: {nim} - {data['nama']}")

    while True:
        print("\n--- Pilih data yang akan diubah ---")
        print("1. Ubah Nama")
        print("2. Ubah Nilai Tugas")
        print("3. Ubah Nilai UTS")
        print("4. Ubah Nilai UAS")
        print("5. Ubah Semua")
        print("0. Selesai")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            data["nama"] = input("Nama baru: ")

        elif pilihan == '2':
            data["tugas"] = float(input("Nilai Tugas baru: "))

        elif pilihan == '3':
            data["uts"] = float(input("Nilai UTS baru: "))

        elif pilihan == '4':
            data["uas"] = float(input("Nilai UAS baru: "))

        elif pilihan == '5':
            data["nama"] = input("Nama baru: ")
            data["tugas"] = float(input("Nilai Tugas baru: "))
            data["uts"] = float(input("Nilai UTS baru: "))
            data["uas"] = float(input("Nilai UAS baru: "))

        elif pilihan == '0':
            break

        else:
            print("✘ Pilihan tidak valid!")
            continue

        data["akhir"] = hitung_nilai_akhir(data["tugas"], data["uts"], data["uas"])
        print("✔ Data berhasil diperbarui!")

    mahasiswa[nim] = data
    print("✔ Proses ubah data selesai!\n")

# --------------------------
# Hapus Data
# --------------------------
def hapus_data():
    nim = input("Masukkan NIM yang akan dihapus: ")

    if nim in mahasiswa:
        del mahasiswa[nim]
        print("✔ Data berhasil dihapus!\n")
    else:
        print("✘ Data tidak ditemukan!\n")

# --------------------------
# Tampilkan Data (View Final Sesuai Contoh)
# --------------------------
def tampilkan_data():
    print("\nDaftar Nilai")
    print("=======================================================================")
    print("| NO |   NIM   |    NAMA     | TUGAS | UTS | UAS |  AKHIR  |")
    print("=======================================================================")

    if not mahasiswa:
        print("|                         TIDAK ADA DATA                            |")
        print("=======================================================================\n")
        return

    no = 1
    for nim, data in mahasiswa.items():
        print(f"| {no:<2} | {nim:<7} | {data['nama']:<11} | "
              f"{data['tugas']:<5} | {data['uts']:<3} | {data['uas']:<3} | {data['akhir']:<7.2f} |")
        no += 1

    print("=======================================================================\n")

# --------------------------
# Cari Data
# --------------------------
def cari_data():
    key = input("Masukkan NIM atau Nama yang dicari: ")

    found = False
    for nim, data in mahasiswa.items():
        if key.lower() in nim.lower() or key.lower() in data["nama"].lower():
            print("\nData Ditemukan:")
            print(f"NIM          : {nim}")
            print(f"Nama         : {data['nama']}")
            print(f"Nilai Tugas  : {data['tugas']}")
            print(f"Nilai UTS    : {data['uts']}")
            print(f"Nilai UAS    : {data['uas']}")
            print(f"Nilai Akhir  : {data['akhir']:.2f}\n")
            found = True

    if not found:
        print("✘ Data tidak ditemukan!\n")

# Saat Program Dimulai → Langsung Tampilkan Judul & Tabel
print("\nProgram Input Nilai")
print("====================\n")
tampilkan_data()
# Menu Utama
# --------------------------
while True:
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar:")
    pilihan = input("Pilih: ").lower()

    if pilihan == 'l':
        tampilkan_data()
    elif pilihan == 't':
        tambah_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("Program selesai.")
        break
    else:
        print("✘ Pilihan tidak valid!\n")