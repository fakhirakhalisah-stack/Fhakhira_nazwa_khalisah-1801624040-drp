import data

def reset_progress():
    data.streak = 0

    print("=== Relapse ===")
    print("Progress berhasil direset.")
    print(f"Rekor terbaik: {data.best_streak} hari")