def display_menu():
    print("\n=== Re:Me ===")
    print("1. Progress Counter")
    print("2. Daily Check-in")
    print("3. Relapse")
    print("4. Visual Habit Growth")
    print("0. Keluar")

def select_menu(menu):
    if menu == "0":
        print("Terima kasih telah menggunakan Re:Me!")
        return True

    print("Menu belum tersedia.")
    return False