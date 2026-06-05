import data

def tampil_visual():
    print("\n=== Visual Habit Growth ===")
    print()

    streak = data.streak

    if streak >= 100:
        level = "🏆 Re:Me Legend"
    elif streak >= 60:
        level = "🌲 Master of Control"
    elif streak >= 30:
        level = "🌳 Habit Guardian"
    elif streak >= 7:
        level = "🌿 Consistent Explorer"
    elif streak >= 1:
        level = "🌱 Rookie Survivor"
    else:
        level = "Belum ada achievement"

    print(f"Achievement saat ini: {level}")
    print(f"Streak saat ini: {streak} hari")
    print(f"Rekor terbaik: {data.best_streak} hari")