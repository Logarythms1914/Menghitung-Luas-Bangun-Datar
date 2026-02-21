from math import pi

def persegi_panjang():
    panjang = float(input('Masukkan nilai panjang: '))
    lebar = float(input('Masukkan nilai lebar: '))
    return panjang * lebar


def lingkaran():
    jari_jari = float(input('Masukkan nilai jari-jari: '))
    return pi * jari_jari ** 2

def segitiga():
    alas = float(input('Masukkan nilai alas: '))
    tinggi = float(input('Masukkan nilai tinggi: '))
    return 0.5 * alas * tinggi
    
nama_bangun_datar = input('Masukkan nama bangun datar: ')
nama_bangun_datar = nama_bangun_datar.lower()

if nama_bangun_datar not in ('persegi','lingkaran','persegi panjang','segitiga'):
    print(f'Maaf bangun datar yang kamu cari belum ada rumusnya di program ini')
else:
    if nama_bangun_datar == 'persegi' or nama_bangun_datar == 'persegi panjang':
        luas = persegi_panjang()
        print(f'Luas bangun datarnya adalah {luas}')
    elif nama_bangun_datar == 'lingkaran':
        luas = lingkaran()
        print(f'Luas lingkarannya adalah {luas}')
    elif nama_bangun_datar == 'segitiga':
        luas = segitiga()
        print(f'Luas segitiganya adalah {luas}')
