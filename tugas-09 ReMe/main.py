from tools import display_menu, select_menu
from habit import pilih_kebiasaan
from database import init_db, ambil_habit

if __name__ == '__main__':

    connection = init_db()

    data = ambil_habit()

    print("\n=================================")
    print("            Re:Me")
    print("=================================")
    print("Saatnya mulai perubahan kecil yang konsisten.")
    print("Pilih kebiasaan yang ingin kamu kurangi.\n")

    if not data:
        pilih_kebiasaan()

    while True:
        display_menu()

        menu = input("Masukkan menu yang dipilih: ")

        is_done = select_menu(menu)

        if is_done:
            break