namaFile = open('d:\dataAngka.txt', 'r')
file = namaFile.readlines()

for i in range(len(file)):
    data1 = file[i].replace('\n','')
    data2 = data1.split('|')
    jumlah = int(data2[0]) + int(data2[1])
    file[i] = jumlah
    
print('hasil ada di file hasilDataAngka.txt')

namaFile.close()
hasil = open('d:\hasilDataAngka.txt', 'w')
for x in range(len(file)):
    hasil.write(str(file[x]) + '\n')
hasil.close()
        
