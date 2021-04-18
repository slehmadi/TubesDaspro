import utility
def Load(namaFolder):
    #I.S. data belum tersimpan dalam variabel
    #F.S. data tersimpan dalam variabel sesuai nama filenya
    global user, gadget, consumable, consumable_history,gadget_borrow_history, gadget_return_history
    #Asumsikan semua file ada, dan penamaan sesuai aturan
    user = utility.BacaCSV(namaFolder+'/user.csv')
    gadget = utility.BacaCSV(namaFolder+'/gadget.csv')
    consumable = utility.BacaCSV(namaFolder+'/consumable.csv')
    consumable_history = utility.BacaCSV(namaFolder+'/consumable_history.csv')
    gadget_borrow_history = utility.BacaCSV(namaFolder+'/gadget_borrow_history.csv')
    gadget_return_history = utility.BacaCSV(namaFolder+'/gadget_return_history.csv')
