from Employe import Employe
from Manager import Manager


def main():
    data_pegawai = [
        {
            "nama" : "Alfadjri Dwi Fadhilah",
            "umur" : 24,
            "pekerjaan" : "IT Trainer",
            "gaji" : 8000000,
            "jumlah_tim" : 0,
        },
        {
            "nama" : "Marsela",
            "umur" : 30,
            "pekerjaan" : "IT Trainer",
            "gaji" : 8000000,
            "jumlah_tim" : 10
        },
        {
            "nama" : "Budi",
            "umur" : 24,
            "pekerjaan" : "Desinger",
            "gaji" : 8000000,
            "jumlah_tim" : 0,
        },
    ]
    print("======= Data User======")
    for value in data_pegawai:
        if value["jumlah_tim"] > 0:
            Person = Manager(value["nama"],value["umur"],value["pekerjaan"],value["gaji"],value['jumlah_tim'])
        if value["jumlah_tim"] <= 0:
            Person = Employe(value["nama"],value["umur"],value["pekerjaan"],value["gaji"]) 
        
        print(Person.get_detail())
        print("======= Work ==========")
        print(Person.work())
        print()

if __name__ == "__main__":
    main()