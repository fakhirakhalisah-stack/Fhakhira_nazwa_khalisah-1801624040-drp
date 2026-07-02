from data import load_data

def lihat_progress():

    data = load_data()

    print("=== Progress Counter ===")
    print(f"Kebiasaan: {data['habit']}")
    print(f"Progress saat ini: {data['streak']} hari")

    if data["streak"] < 7:
        milestone = 7
    elif data["streak"] < 30:
        milestone = 30
    elif data["streak"] < 60:
        milestone = 60
    elif data["streak"] < 100:
        milestone = 100
    else:
        milestone = "Semua achievement terbuka"

    print(f"Milestone berikutnya: {milestone}")