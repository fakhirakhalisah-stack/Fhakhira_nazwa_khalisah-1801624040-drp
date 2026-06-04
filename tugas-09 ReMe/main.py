from tools import display_menu, select_menu

if __name__ == '__main__':
    while True:
        display_menu()

        menu = input("Masukkan menu yang dipilih: ")

        is_done = select_menu(menu)

        if is_done:
            break