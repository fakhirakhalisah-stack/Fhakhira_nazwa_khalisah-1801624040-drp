from database import ambil_habit
import sqlite3
from datetime import date

def pilih_habit():

    data = ambil_habit()

    if not data:
        print("Belum ada habit.")
        return None

    print("=== Pilih Habit ===")

    for h in data:
        print(f"{h[0]}. {h[1]}")

    try:
        return int(input("Pilih ID habit: "))
    except ValueError:
        print("Input tidak valid.")
        return None


def relapse():

    id_habit = pilih_habit()

    if id_habit is None:
        return

    alasan = input("Alasan relapse: ")
    pemicu = input("Pemicu relapse: ")
    tanggal = str(date.today())

    connection = sqlite3.connect("reme.db")

    connection.execute("""
        INSERT INTO relapse
        (alasan, pemicu, tanggal_relapse, id_habit)
        VALUES (?, ?, ?, ?)
    """, (alasan, pemicu, tanggal, id_habit))

    connection.commit()
    connection.close()

    print("=== RELAPSE RECORDED ===")
    print("Relapse berhasil dicatat, tetap semangat!")