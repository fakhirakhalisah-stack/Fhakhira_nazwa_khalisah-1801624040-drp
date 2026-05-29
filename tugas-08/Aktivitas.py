# =========================
# SISTEM CATUR + AKTIVITAS 🐾
# =========================

# 1. INPUT NAMA USER
user = input("Siapa nama Anda? 🐶 ")

# 2. HEADER PROGRAM
print("\n" + "=" * 55)
print(f"   🐱 SISTEM CATUR & AKTIVITAS LUCU - {user} 🐱")
print("=" * 55 + "\n")


# =========================
# 3. PAPAN CATUR
# =========================
print("1. PAPAN CATUR 🐾\n")

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")
    print()

print("\n" + "-" * 55 + "\n")


# =========================
# 4. INPUT AKTIVITAS
# =========================
print("2. INPUT AKTIVITAS LUCU 🐰\n")

aktivitas_list = []

# DATA CONTOH DENGAN EMOJI HEWAN 🐶🐱🐼
aktivitas_list.append({
    "aktivitas": "belajar 📚🐱",
    "detail": "belajar Psikologi sambil ditemani kucing",
    "waktu": "pagi 🌤️",
    "mood": "fokus 🦉"
})

aktivitas_list.append({
    "aktivitas": "kerja kelompok 🐼🤝",
    "detail": "diskusi tugas bareng teman",
    "waktu": "siang ☀️",
    "mood": "aktif 🐵"
})

aktivitas_list.append({
    "aktivitas": "nonton 🎬🐶",
    "detail": "nonton film sambil rebahan",
    "waktu": "malam 🌙",
    "mood": "santai 🦊"
})

print("🐾 Data aktivitas lucu berhasil ditambahkan!\n")


# =========================
# 5. OUTPUT AKTIVITAS
# =========================
print("\n3. DAFTAR AKTIVITAS TERDATA 🐾\n")

if len(aktivitas_list) == 0:
    print("😿 Belum ada aktivitas yang dimasukkan.")
else:
    for i, item in enumerate(aktivitas_list, start=1):
        print(f"{i}. {item['aktivitas']}")
        print(f"   📌 Detail : {item['detail']}")
        print(f"   ⏰ Waktu  : {item['waktu']}")
        print(f"   🎭 Mood   : {item['mood']}")
        print("-" * 45)


# =========================
# 6. PENUTUP
# =========================
print("\n" + "=" * 55)
print(f"🐾 Terima kasih {user} 🐶")
print("🐱 Program selesai dengan gemas!")
print("=" * 55)