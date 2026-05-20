from datetime import datetime

print('=== Aplikasi Manajemen Aktivitas ===')

aktivitas = input('Masukkan aktivitas: ')
aktivitas = aktivitas.lower()

# AKTIVITAS SARAPAN
if aktivitas == 'sarapan':

    print('Menu tersedia: sosis, ayam, kentang, roti, cereal')

    menu = input('Masukkan menu sarapan: ')
    menu = menu.lower()

    if menu == 'sosis' or menu == 'ayam' or menu == 'kentang':
        print('Bahan tersedia, silakan dimasak terlebih dahulu')
        print('Disarankan memasak dengan porsi yang cukup')

    elif menu == 'roti' or menu == 'cereal':
        print('Menu dapat langsung disajikan')

    else:
        print('Bahan tidak tersedia, silakan membeli terlebih dahulu')


    if menu == 'ayam':
        print('Pastikan ayam dimasak hingga matang')

    elif menu == 'kentang':
        print('Kentang cocok disajikan dengan saus')

    print('Jangan lupa sarapan agar lebih semangat!')


# AKTIVITAS KERJA
elif aktivitas == 'kerja':

    waktu_sekarang = datetime.now()

    jam = waktu_sekarang.hour
    menit = waktu_sekarang.minute

    print('Waktu sekarang:', jam, ':', menit)

    if jam > 8 or (jam == 8 and menit > 0):
        print('Anda terlambat masuk kerja')

    else:
        print('Anda belum terlambat masuk kerja')


    if jam < 7:
        print('Anda masih memiliki banyak waktu sebelum berangkat')

    elif jam == 7:
        print('Segera bersiap agar tidak terlambat')

    else:
        print('Segera menuju kantor')

    print('Semangat bekerja hari ini!')
