def BacaCSV(namaFile):
    #Input : nama file dengan tipe, contoh : 'gadgets.csv'
    #Output : Akan mengembalikan array berisi data dari CSV
    f = open(namaFile,'r')
    lineGadget = f.readlines()
    f.close()
    usedLineGadget = [line.replace("\n",'') for line in lineGadget]
    headerGadget = rapidata(usedLineGadget.pop(0))
    datasGadget = []
    for line in usedLineGadget:
        dataAkhirGadget = rapidata(line)
        datasGadget.append(dataAkhirGadget)
    return {'header':headerGadget, 'data':datasGadget}
    #simpan hasil baca file ini ke sebuah variabel misal hasilBaca
    #maka hasilBaca['header'] akan menyimpan nama-nama kolom di file yang dibaca
    # hasilBaca['data'] akan menyimpan data-data berupa array


def convertDatatoString(header,lines):      # mengubah bentuk matriks (array of array) menjadi string yang akan
    stringline = ';'.join(header) + "\n"    # dicatat pada file csv
    for line in lines:
        allLine = [str(kind) for kind in line]
        stringline += ';'.join(allLine)
        stringline += '\n'
    return stringline

def pisah(lines):   # parser csv buatan
    newline = []
    word = ''
    for alpha in lines:
        if alpha == ';':
            newline.append(word)
            word = ''
        else:
            word += alpha
    if word != '':
        newline.append(word)
    return newline

def rapidata(line): # buat menjadikan array yg awalnya misal ['s', ' s', 's '] => ['s','s','s']
    new = pisah(line)
    result = [data.strip() for data in new]
    return result

def SimpanCSV(header, array, namaFile):
    #I.S. Array sudah terdefinisi masih belum bertipe string, file csv belum diperbarui
    #F.S. File CSV sudah diperbarui
    #Isi parameter header dengan nama variabel dimana header disimpan
    #Isi parameter array dengan nama variabel dimana data berupa array disimpan
    #Isi namaFile dengan tempat dimana data ingin disimpan, contoh: 'gadgets.csv'
    data_string = convertDatatoString(header,array)
    f = open(namaFile,'w')
    f.write(data_string)
    f.close()