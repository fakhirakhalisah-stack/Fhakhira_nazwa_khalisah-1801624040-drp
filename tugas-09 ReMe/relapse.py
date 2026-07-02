from data import load_data, save_data

def reset_progress():

    data = load_data()

    data["streak"] = 0

    save_data(data)

    print("=== Relapse ===")
    print("Progress berhasil direset.")
    print(f"Rekor terbaik: {data['best_streak']} hari")