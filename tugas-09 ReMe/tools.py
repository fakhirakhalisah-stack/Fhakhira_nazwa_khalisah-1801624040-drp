from checkin import daily_checkin
from progress import lihat_progress
from relapse import reset_progress
from visual import tampil_visual

def display_menu():
    print("\n=== Re:Me ===")
    print("1. Progress Counter")
    print("2. Daily Check-in")
    print("3. Relapse")
    print("4. Visual Habit Growth")
    print("0. Keluar")

def select_menu(menu):

    if menu == "1":
        lihat_progress()

    elif menu == "2":
        daily_checkin()

    elif menu == "3":
        reset_progress()

    elif menu == "4":
        tampil_visual()

    elif menu == "0":
        print("Terima kasih telah menggunakan Re:Me!")
        return True

    else:
        print("Menu belum tersedia.")

    return False