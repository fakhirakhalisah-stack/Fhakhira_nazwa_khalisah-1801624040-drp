from database import tambah_habit
from datetime import date

def pilih_kebiasaan():

    print("=== Pilih Kebiasaan ===")
    print("1. Alkohol")
    print("2. Begadang")
    print("3. Berbohong")
    print("4. Berkata Kasar")
    print("5. Doomscrolling")
    print("6. Impulsive Shopping")
    print("7. Junk Food")
    print("8. Merokok")
    print("9. Perjudian")
    print("10. Prokrastinasi")
    print("11. Self-harm")
    print("12. Video Game")
    print("13. Other")

    pilihan = input("Pilih kebiasaan (1-13): ")

    if pilihan == "1":
        habit = "Alkohol"

    elif pilihan == "2":
        habit = "Begadang"

    elif pilihan == "3":
        habit = "Berbohong"

    elif pilihan == "4":
        habit = "Berkata Kasar"

    elif pilihan == "5":
        habit = "Doomscrolling"

    elif pilihan == "6":
        habit = "Impulsive Shopping"

    elif pilihan == "7":
        habit = "Junk Food"

    elif pilihan == "8":
        habit = "Merokok"

    elif pilihan == "9":
        habit = "Perjudian"

    elif pilihan == "10":
        habit = "Prokrastinasi"

    elif pilihan == "11":
        habit = "Self-harm"

    elif pilihan == "12":
        habit = "Video Game"

    elif pilihan == "13":
        habit = input("Masukkan kebiasaan yang ingin diubah: ")

    else:
        print("Pilihan tidak valid.")
        return

    kategori_habit = input("Masukkan kategori habit: ")

    try:
        target_pengguna = int(input("Masukkan target (hari): "))
    except ValueError:
        print("Target harus berupa angka.")
        return

    tanggal_mulai = str(date.today())
    status_habit = "Aktif"
    id_user = 1

    tambah_habit(
        habit,
        kategori_habit,
        tanggal_mulai,
        status_habit,
        target_pengguna,
        id_user
    )

    print(f"Kebiasaan berhasil ditambahkan: {habit}")