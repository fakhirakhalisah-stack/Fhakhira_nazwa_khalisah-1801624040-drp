import sqlite3

def init_tables(connection):

    connection.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        foto_profil TEXT,
        tanggal_daftar TEXT,
        last_login TEXT
    );
    """)

    connection.execute("""
    CREATE TABLE IF NOT EXISTS habit (
        id_habit INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_habit TEXT NOT NULL,
        kategori_habit TEXT,
        tanggal_mulai TEXT,
        status_habit TEXT,
        target_pengguna INTEGER,
        id_user INTEGER,
        FOREIGN KEY(id_user) REFERENCES user(id_user)
    );
    """)

    connection.execute("""
    CREATE TABLE IF NOT EXISTS daily_checkin (
        id_checkin INTEGER PRIMARY KEY AUTOINCREMENT,
        tanggal_checkin TEXT,
        status TEXT,
        mood TEXT,
        aktivitas TEXT,
        catatan TEXT,
        id_habit INTEGER,
        FOREIGN KEY(id_habit) REFERENCES habit(id_habit)
    );
    """)

    connection.execute("""
    CREATE TABLE IF NOT EXISTS relapse (
        id_relapse INTEGER PRIMARY KEY AUTOINCREMENT,
        alasan TEXT,
        pemicu TEXT,
        tanggal_relapse TEXT,
        id_habit INTEGER,
        FOREIGN KEY(id_habit) REFERENCES habit(id_habit)
    );
    """)

    connection.execute("""
    CREATE TABLE IF NOT EXISTS milestone (
        id_milestone INTEGER PRIMARY KEY AUTOINCREMENT,
        target_hari INTEGER,
        milestone_berikutnya TEXT,
        tanggal_tercapai TEXT,
        status_milestone TEXT,
        level_achievement TEXT,
        visual_icon TEXT,
        id_habit INTEGER,
        FOREIGN KEY(id_habit) REFERENCES habit(id_habit)
    );
    """)

    connection.commit()


def init_db():

    connection = sqlite3.connect("reme.db")

    init_tables(connection)

    return connection


def tambah_habit(nama_habit, kategori_habit, tanggal_mulai, status_habit, target_pengguna, id_user):

    connection = sqlite3.connect("reme.db")

    connection.execute("""
        INSERT INTO habit
        (nama_habit, kategori_habit, tanggal_mulai, status_habit, target_pengguna, id_user)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nama_habit, kategori_habit, tanggal_mulai, status_habit, target_pengguna, id_user))

    connection.commit()
    connection.close()


def ambil_habit():

    connection = sqlite3.connect("reme.db")

    cursor = connection.execute("SELECT * FROM habit")

    data = cursor.fetchall()

    connection.close()

    return data

def tambah_checkin(tanggal_checkin, status, mood, aktivitas, catatan, id_habit):

    connection = sqlite3.connect("reme.db")

    connection.execute("""
        INSERT INTO daily_checkin
        (tanggal_checkin, status, mood, aktivitas, catatan, id_habit)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (tanggal_checkin, status, mood, aktivitas, catatan, id_habit))

    connection.commit()
    connection.close()

def update_habit(id_habit, status_habit):

    connection = sqlite3.connect("reme.db")

    connection.execute("""
        UPDATE habit
        SET status_habit = ?
        WHERE id_habit = ?
    """, (status_habit, id_habit))

    connection.commit()
    connection.close()


def hapus_habit(id_habit):

    connection = sqlite3.connect("reme.db")

    connection.execute("""
        DELETE FROM habit
        WHERE id_habit = ?
    """, (id_habit,))

    connection.commit()
    connection.close()


def hitung_persentase_keberhasilan(id_habit):

    connection = sqlite3.connect("reme.db")

    cursor = connection.execute("""
        SELECT COUNT(*)
        FROM daily_checkin
        WHERE id_habit = ?
    """, (id_habit,))
    total_checkin = cursor.fetchone()[0]

    cursor = connection.execute("""
        SELECT COUNT(*)
        FROM daily_checkin
        WHERE id_habit = ?
        AND status = 'berhasil'
    """, (id_habit,))
    jumlah_berhasil = cursor.fetchone()[0]

    connection.close()

    if total_checkin == 0:
        return 0

    return (jumlah_berhasil / total_checkin) * 100