import utility
def Save():
    #I.S. variabel user,gadget,gadget_return_history, gadget_borrow_history, consumable, consumable_history sudah terdefinisi
    #F.S. variabel-variabel di atas akan disimpan di file csv yang berkaitan, menimpa data yang lama
    folderDir = input('Masukkan nama folder penyimpanan: ')
    utility.SimpanCSV(user['header'], user['data'], folderDir +'/user.csv')
    utility.SimpanCSV(gadget['header'], gadget['data'], folderDir +'/gadget.csv')
    utility.SimpanCSV(gadget_borrow_history['header'], gadget_borrow_history['data'], folderDir +'/gadget_borrow_history.csv')
    utility.SimpanCSV(gadget_return_history['header'], gadget_return_history['data'], folderDir +'/gadget_return_history.csv')
    utility.SimpanCSV(consumable['header'], consumable['data'], folderDir +'/consumable.csv')
    utility.SimpanCSV(consumable_history['header'], consumable_history['data'], folderDir +'/consumable_history.csv')