namaFile = open('d:\dataMhs.txt', 'r')
namaFile2 = open('d:\dataMhs.txt', 'a')

while True :
    nim = input('\nMasukan NIM : ')
    nama = input('Masukan Nama Mhs : ')
    almt = input('Masukan Alamat : ')
    namaFile2.write(nim + '|' + nama + '|' + almt + '\n')
    
    tambah = input('\nMau lagi (y/n) : ')
    ('\n')
    if tambah == 'y':
        True
    elif tambah == 'n' :
        break
    else :
        print('Inputan invalid')
        break

namaFile2.close()
