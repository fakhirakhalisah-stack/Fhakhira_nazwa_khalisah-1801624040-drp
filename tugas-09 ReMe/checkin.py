from database import ambil_habit, tambah_checkin
from datetime import date

def pilih_habit():

    data = ambil_habit()

    if not data:
        print("Belum ada habit. Silakan tambah habit dulu.")
        return None

    print("=== Pilih Habit ===")

    for h in data:
        print(f"{h[0]}. {h[1]}")

    try:
        id_habit = int(input("Pilih ID habit: "))
        return id_habit
    except ValueError:
        print("Input tidak valid.")
        return None


def daily_checkin():

    id_habit = pilih_habit()

    if id_habit is None:
        return

    jawab = input("Apakah hari ini berhasil menahan diri? (iya/tidak): ")

    tanggal = str(date.today())

    if jawab.lower() == "iya":

        mood = input("Mood hari ini: ")
        aktivitas = input("Aktivitas hari ini: ")
        catatan = input("Catatan (opsional): ")

        tambah_checkin(
            tanggal,
            "berhasil",
            mood,
            aktivitas,
            catatan,
            id_habit
        )

        print("Hebat! Check-in berhasil dicatat.")

    else:

        tambah_checkin(
            tanggal,
            "gagal",
            "-",
            "-",
            "-",
            id_habit
        )

        print("Tetap semangat, coba lagi besok.")