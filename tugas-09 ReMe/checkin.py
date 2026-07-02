from data import load_data, save_data

def daily_checkin():

    data = load_data()

    jawab = input("Apakah hari ini berhasil menahan diri?: ")

    if jawab.lower() == "iya":

        data["streak"] += 1

        if data["streak"] > data["best_streak"]:
            data["best_streak"] = data["streak"]

        save_data(data)

        print("Hebat! Kamu berhasil hari ini.")
        print(f"Streak sekarang: {data['streak']} hari")

    else:
        print("Tetap semangat dan coba lagi besok.")