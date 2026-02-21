def segitiga1():
    sisi_1 = float(input('Masukkan nilai sisi pertama: '))
    sisi_2 = float(input('Masukkan nilai sisi kedua: '))
    sisi_3 = float(input('Masukkan nilai sisi ketiga: '))
    s = (sisi_1 + sisi_2 + sisi_3)/2  # setengah keliling segitiga
    return (s * (s - sisi_1) * (s - sisi_2) * (s - sisi_3))**0.5

if nama_bangun_datar == 'segitiga':
    luas = segitiga1()
    print(f'Luas segitiganya adalah {luas}')
