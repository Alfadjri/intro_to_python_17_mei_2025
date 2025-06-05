from Employe import Employe

class Manager(Employe):
    def __init__(self, nama, umur, pekerjaan, gaji,jumlah_tim):
        super().__init__(nama, umur, pekerjaan, gaji)
        self._jumlah_tim = jumlah_tim
    
    def get_detail(self):
        return super().get_detail() + f"\nTim\t:\t{self._jumlah_tim}\n"
    
    def work(self):
        return super().work() + f"dengan jumlah tim {self._jumlah_tim}\n"