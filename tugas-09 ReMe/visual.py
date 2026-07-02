import sqlite3
from database import ambil_habit

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


def tampil_visual():

    data = ambil_habit()

    if not data:
        print("Belum ada habit.")
        return

    print("\n=== Visual Habit Growth ===\n")
    print("🎮 Habit Quest\n")

    achievements = [
        ("🌱 Rookie Survivor", 1),
        ("🌿 Consistent Explorer", 7),
        ("🌳 Habit Guardian", 30),
        ("🌲 Master of Control", 60),
        ("🏆 Re:Me Legend", 100)
    ]

    for habit in data:

        id_habit = habit[0]
        nama_habit = habit[1]

        streak = hitung_streak(id_habit)

        print(f"\n📌 {nama_habit}")
        print(f"Streak saat ini: {streak} hari\n")

        for nama, target in achievements:
            if streak >= target:
                status = "✅"
            else:
                status = "🔒"

            print(f"{status} {nama} - {target} Hari")