from database import ambil_habit, hitung_persentase_keberhasilan
import sqlite3

def hitung_streak(id_habit):

    connection = sqlite3.connect("reme.db")

    cursor = connection.execute("""
        SELECT COUNT(*)
        FROM daily_checkin
        WHERE status = 'berhasil'
        AND id_habit = ?
    """, (id_habit,))

    streak = cursor.fetchone()[0]

    connection.close()

    return streak


def lihat_progress():

    data = ambil_habit()

    print("=== Progress Counter ===")

    if not data:
        print("Belum ada habit yang ditambahkan.")
        return

    for habit in data:

        id_habit = habit[0]
        nama_habit = habit[1]
        kategori = habit[2]
        tanggal_mulai = habit[3]
        status = habit[4]
        target = habit[5]

        streak = hitung_streak(id_habit) 

        persentase = hitung_persentase_keberhasilan(id_habit) 

        if streak < 7:
            milestone = 7
        elif streak < 30:
            milestone = 30
        elif streak < 60:
            milestone = 60
        elif streak < 100:
            milestone = 100
        else:
            milestone = "Semua achievement terbuka"

        print(f"Kebiasaan          : {nama_habit}")
        print(f"Kategori           : {kategori}")
        print(f"Tanggal Mulai      : {tanggal_mulai}")
        print(f"Status             : {status}")
        print(f"Target             : {target} hari")
        print(f"Progress (streak)  : {streak} hari")
        print(f"Persentase Keberhasilan: {persentase:.2f}%")
        print(f"Milestone berikutnya: {milestone}")
        print("-" * 35)