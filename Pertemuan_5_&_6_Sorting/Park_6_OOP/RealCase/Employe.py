from Person import Person


class Employe(Person):
    def __init__(self, nama, umur,pekerjaan,gaji):
        super().__init__(nama, umur)
        self._pekerjaan = pekerjaan
        self.__gaji = gaji
        
    def get_detail(self):
        return f"Nama\t:\t{self._nama}\nUmur\t:\t{self.get_umur()}\nJob\t:\t{self._pekerjaan}\nGaji\t:\t{self.__gaji}"
    
    def work(self):
        return f"{self._nama} dia bekerja sebagai {self._pekerjaan}"