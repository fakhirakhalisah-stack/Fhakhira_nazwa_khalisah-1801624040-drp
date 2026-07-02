from data import load_data

def tampil_visual():

    data = load_data()

    streak = data["streak"]

    print("\n=== Visual Habit Growth ===\n")

    print("🎮 Habit Quest\n")

    achievements = [
        ("🌱 Rookie Survivor", 1),
        ("🌿 Consistent Explorer", 7),
        ("🌳 Habit Guardian", 30),
        ("🌲 Master of Control", 60),
        ("🏆 Re:Me Legend", 100)
    ]

    for nama, target in achievements:
        if streak >= target:
            status = "✅"
        else:
            status = "🔒"

        print(f"{status} {nama} - {target} Hari")

    print(f"\nStreak saat ini : {streak} hari")
    print(f"Rekor terbaik   : {data['best_streak']} hari")