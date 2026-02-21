from math import pi

def persegi():
    sisi = int(input('Masukkan nilai sisi: '))
    return sisi**2


def lingkaran():
    jari_jari = int(input('Masukkan nilai jari-jari: '))
    return pi*jari_jari**2

nama_bangun_datar = input('Masukkan nama bangun datar: ')
nama_bangun_datar = nama_bangun_datar.lower()

if nama_bangun_datar not in ('persegi','lingkaran'):
    print(f'Maaf bangun datar yang kamu cari belum ada rumusnya di program ini')
else:
    if nama_bangun_datar == 'persegi':
        luas = persegi()
        print(f'Luas perseginya adalah {luas}')
    elif nama_bangun_datar == 'lingkaran':
        luas = lingkaran()
        print(f'Luas lingkarannya adalah {round(luas,2)}')
