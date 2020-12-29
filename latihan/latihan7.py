namaFile = input('Masukan nama file : ')
angka = int(input('Berapa langkah untuk menggeser ? : '))
file = open(namaFile, 'r')
file2 = file.read()
data = list(file2)
password = []

for i in data:
    asciCode = ord(i)
    if asciCode == 32:
        code = asciCode
    else:
        code = asciCode - angka
        if code < 65 :
            code = code + 26
        elif code < 90 and code > 97:
            code = code + 26
    sandi = chr(code)
    password = password + [sandi]
    if not data:
        break
a = ''.join(password)
hasil = open('d:\hasilSandi.txt', 'w')
hasil.write(a)
hasil.close()
