#Kartu
import random

class Kartu : #Kartu di sebut nama class 
    #class adalah cetak biru dari object
    __satu_divisi_kartu = 13 # _ _ ini disebut property protected berarti nilainya hanya bisa di gunakan di class tersebut
    _jumlah_kartu = 52 # _ ini siftanya property private bisa di ubah tapi tidak sembarangan
    
    divisi_katru = ["❤️","💎","♠️","♣️"] # ini di sebut object
    ambil_nomer_kartu = "default"
    
    
    def __init__(self,joker = None): #konstruktor itu gunanya untuk syarat dalam memanggil kelas
        if joker != None:
            self.__satu_divisi_kartu += 1
            self.ambil_nomer_kartu = 14
        else:
            self.ambil_nomer_kartu = random.randint(1,self.__satu_divisi_kartu)
    
    def getKartu(self): #metode
        ambil_kartu = self.divisi_katru[random.randint(0,3)]
        match(self.ambil_nomer_kartu):
            case 1 :
                self.ambil_nomer_kartu = "A"
            case 11:
                self.ambil_nomer_kartu =  "J"
            case 12:
                self.ambil_nomer_kartu =  "Q"
            case 13:
                self.ambil_nomer_kartu = "K"
            case 14:
                self.ambil_nomer_kartu = "Joker"
            
        return str(self.ambil_nomer_kartu) +" "+ str(ambil_kartu)
    

# tampat construktor
list_kartu = Kartu()
print(f"list divisi kartu : {list_kartu.divisi_katru}")
print(f"Katru yang kita ambil adalah : {list_kartu.getKartu()}")

list_kartu = Kartu(True)
print(f"Katru yang kita ambil adalah : {list_kartu.getKartu()}")