from tools import display_menu, select_menu
from habit import pilih_kebiasaan
from data import load_data

if __name__ == '__main__':

    data = load_data()

    if data["habit"] == "":
        print("\n=================================")
        print("     Selamat Datang di Re:Me")
        print("=================================")
        print("Silahkan pilih kebiasaan yang ingin dikurangi.\n")

        pilih_kebiasaan()

    while True:
        display_menu()

        menu = input("Masukkan menu yang dipilih: ")

        is_done = select_menu(menu)

        if is_done:
            break