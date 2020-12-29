myFile = open('d:\dataMhs.txt', 'r')
file = myFile.readlines()

cariNim = input('Masukan NIM yang di cari : ' )

for i in range(len(file)):
    if(cariNim in file[i]):
        data = file[i].split('|')
        print('Data Mahasiswa')
        print('NIM : ' , data[0])
        print('Nama : ' , data[1])
        print('Alamat : ' , data[2])
        break
    else:
        print('Data Mahasiswa Tidak Ditemukan')
        break
    
