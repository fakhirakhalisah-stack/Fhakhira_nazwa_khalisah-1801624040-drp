import data

def lihat_progress():
    print("=== Progress Counter ===")
    print("Kebiasaan: Begadang")
    print(f"Progress saat ini: {data.streak} hari")

    if data.streak < 7:
        milestone = 7
    elif data.streak < 30:
        milestone = 30
    elif data.streak < 60:
        milestone = 60
    elif data.streak < 100:
        milestone = 100
    else:
        milestone = "Semua achievement terbuka"

    print(f"Milestone berikutnya: {milestone}")