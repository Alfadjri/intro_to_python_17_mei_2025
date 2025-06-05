#Kartu
import random

class Kartu : 
    __satu_divisi_kartu = 13 
    _jumlah_kartu = 52
    
    divisi_katru = ["❤️","💎","♠️","♣️"] 
    ambil_nomer_kartu = "default"
    
    _is_katru_joker = False # ini di sebutnya encapsulation
    # encapsulation adalah teknik di mana nilai itu di sembunyikan

    def getKartu(self):
        ambil_kartu = self.divisi_katru[random.randint(0,3)]
        if self._is_katru_joker == True:
            self.ambil_nomer_kartu = 14
        else:
            self.ambil_nomer_kartu = random.randint(1,self.__satu_divisi_kartu)
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

    def getJumlahKartu(self):
        if self._is_katru_joker == True:
            self._jumlah_kartu = 56
        
        return self._jumlah_kartu
    def getSatuDivisi(self):
        if self._is_katru_joker == True:
            self.__satu_divisi_kartu += 1
        return self.__satu_divisi_kartu

    def setJoker(self,Joker):
        if Joker == True:
            self._is_katru_joker = True
        else:
            self._is_katru_joker = False
            
    # Teknik Seter (Set) and Geter  (Get)
    # set di gunanakan untuk merubah nilai private 
    # get di gunakan untuk mengambil sesuatu dari kelas
    

# tampat construktor
list_kartu = Kartu()
print("========Tampa Joker ===========")
list_kartu.divisi_katru.append("Baru") #kartan divisikartu property nya public
print(f"List Kartu : {list_kartu.divisi_katru}")
print(f"Jumlah Kartu : {list_kartu.getJumlahKartu()}")
print(f"Satu Divisi Kartu : {list_kartu.getSatuDivisi()}")
print(f"Katru Acak : {list_kartu.getKartu()}")

list_kartu.setJoker(True)
print("========Tampa Dengan ===========")
print(f"Jumlah Kartu : {list_kartu.getJumlahKartu()}")
print(f"Satu Divisi Kartu : {list_kartu.getSatuDivisi()}")
print(f"Katru Acak : {list_kartu.getKartu()}")