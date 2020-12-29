myFile = open('d:\dataMhs.txt' , 'r')
file = (myFile.readlines())

dictionary = {}
dictionary2 = []

for i in range(len(file)):
    data = file[i].split('|')
    data[2] = data[2].replace('\n' , '')
    
    dictionary = {'nim' : data[0], 'nama' : data[1], 'alamat' : data[2]}

    dictionary2.append(dictionary)
    
print(dictionary2)
