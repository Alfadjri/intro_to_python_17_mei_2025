class Ibu:
    panggilan = "Ini ibu ada yang bisa ibu bantu ?"
    
    def memanggil(self):
        print("Iya, Ada apa ?")
    
    def setSifat(self,sifat):
        self.__sifat = sifat
    
    def getSifat(self):
        print(f"{self.__sifat}")


class Anak(Ibu):
    def suruh(self):
        print("nanti dulu ah!!!")
        


# Contoh Memanggil
anak = Anak()
anak.memanggil()
anak.setSifat("Malas")
anak.getSifat()
anak.suruh()

ibu = Ibu()
# ibu.suruh()

#inheritace adalah teknik untuk menurunkan sifat atau class dari Induk