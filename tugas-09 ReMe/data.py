import sqlite3
import json
import os


def export_data(filename):

    connection = sqlite3.connect("reme.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user")
    user = cursor.fetchall()

    cursor.execute("SELECT * FROM habit")
    habit = cursor.fetchall()

    cursor.execute("SELECT * FROM daily_checkin")
    daily_checkin = cursor.fetchall()

    cursor.execute("SELECT * FROM relapse")
    relapse = cursor.fetchall()

    cursor.execute("SELECT * FROM milestone")
    milestone = cursor.fetchall()

    data = {
        "user": user,
        "habit": habit,
        "daily_checkin": daily_checkin,
        "relapse": relapse,
        "milestone": milestone
    }

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    connection.close()

    print("Data berhasil diexport ke", filename)


def import_data(filename):

    if not os.path.exists(filename):
        print("File tidak ditemukan.")
        return

    with open(filename, "r") as file:
        data = json.load(file)

    connection = sqlite3.connect("reme.db")
    cursor = connection.cursor()

    # Hapus data lama
    cursor.execute("DELETE FROM daily_checkin")
    cursor.execute("DELETE FROM relapse")
    cursor.execute("DELETE FROM milestone")
    cursor.execute("DELETE FROM habit")
    cursor.execute("DELETE FROM user")

    # Import data user
    for row in data["user"]:
        cursor.execute("""
            INSERT INTO user
            VALUES (?, ?, ?, ?, ?)
        """, row)

    # Import data habit
    for row in data["habit"]:
        cursor.execute("""
            INSERT INTO habit
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, row)

    # Import data daily_checkin
    for row in data["daily_checkin"]:
        cursor.execute("""
            INSERT INTO daily_checkin
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, row)

    # Import data relapse
    for row in data["relapse"]:
        cursor.execute("""
            INSERT INTO relapse
            VALUES (?, ?, ?, ?, ?)
        """, row)

    # Import data milestone
    for row in data["milestone"]:
        cursor.execute("""
            INSERT INTO milestone
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, row)

    connection.commit()
    connection.close()

    print("Data berhasil diimport dari", filename)