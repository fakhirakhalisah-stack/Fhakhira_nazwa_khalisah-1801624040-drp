from data import export_data, import_data

def backup_restore():

    while True:

        print("\n=== Backup & Restore ===")
        print("1. Export Data")
        print("2. Import Data")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":

            filename = input("Masukkan nama file export: ")

            if filename == "":
                filename = "backup_data"

            if not filename.endswith(".json"):
                filename += ".json"

            export_data(filename)

        elif pilihan == "2":

            filename = input("Masukkan nama file import: ")

            if not filename.endswith(".json"):
                filename += ".json"

            import_data(filename)

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid.")