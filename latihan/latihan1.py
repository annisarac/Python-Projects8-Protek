myFile = open('d:\dataBilangan.txt', 'r')
angka = myFile.readlines()

genap = []
ganjil = []


for i in range(len(angka)):
    if('\n' in angka[i] == True):
        angka[i].replace('\n','')

        if(int(angka[i])%2 == 0):
            genap.append(angka[i])
        else:
            ganjil.append(angka[i])

    else:
        if(int(angka[i])%2 == 0):
            genap.append(angka[i])
        else:
            ganjil.append(angka[i])

print('Banyak bilangan genap : {0}'.format(len(genap)))
print('Banyak bilangan ganjil : {0}'.format(len(ganjil)))
