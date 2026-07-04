from checkin import daily_checkin
from progress import lihat_progress
from relapse import relapse
from visual import tampil_visual
from habit import pilih_kebiasaan
from database import hapus_habit
from backup import backup_restore


def display_menu():
    print("\n=== Re:Me ===")
    print("1. Progress Counter")
    print("2. Daily Check-in")
    print("3. Relapse")
    print("4. Visual Habit Growth")
    print("5. Atur Kebiasaan")
    print("6. Hapus Habit")
    print("7. Backup & Restore")
    print("0. Keluar")


def select_menu(menu):

    if menu == "1":
        lihat_progress()

    elif menu == "2":
        daily_checkin()

    elif menu == "3":
        relapse()

    elif menu == "4":
        tampil_visual()

    elif menu == "5":
        pilih_kebiasaan()

    elif menu == "6":
        id_habit = int(input("Masukkan ID habit yang ingin dihapus: "))
        hapus_habit(id_habit)
        print("Habit berhasil dihapus.")

    elif menu == "7":
        backup_restore()

    elif menu == "0":
        print("Terima kasih telah menggunakan Re:Me!")
        return True

    else:
        print("Menu belum tersedia.")

    return False