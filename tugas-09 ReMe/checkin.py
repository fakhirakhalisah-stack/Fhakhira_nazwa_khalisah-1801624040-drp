import data

def daily_checkin():
    jawab = input("Apakah hari ini berhasil menahan diri?: ")

    if jawab.lower() == "iya":
        data.streak += 1

        if data.streak > data.best_streak:
            data.best_streak = data.streak

        print(f"Hebat! Kamu berhasil hari ini.")
        print(f"Streak sekarang: {data.streak} hari")

    else:
        print("Tetap semangat dan coba lagi besok.")