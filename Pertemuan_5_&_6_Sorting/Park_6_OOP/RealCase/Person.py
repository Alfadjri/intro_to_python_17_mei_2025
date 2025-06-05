from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self,nama,umur):
        self._nama = nama
        self.__umur = umur
    
    @abstractclassmethod
    def get_detail(self):
        pass
    
    def get_umur(self):
        return self.__umur
    
    def set_umur(self,umur):
        if(umur > 0):
            self.__umur = umur
        else:
            raise ValueError("Umur harus bernilai positif")