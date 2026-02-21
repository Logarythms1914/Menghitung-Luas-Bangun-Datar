def persegi():
    sisi = int(input('Masukkan nilai sisi: '))
    return sisi**2

nama_bangun_datar = input('Masukkan nama bangun datar: ')
nama_bangun_datar = nama_bangun_datar.lower()

if nama_bangun_datar != 'persegi':
    print(f'Maaf bangun datar yang kamu cari belum ada rumusnya di program ini')
else:
    luas = persegi()
    print(f'Luas persegi adalah {luas}')
