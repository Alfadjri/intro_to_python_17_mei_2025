#function 
#format dasar
#def namaFunction(paramter):
# kegiatan apa yang akan di lakukan 

# paramter itu syarat saat kamu memanggil namaFunction nya 
# Contoh 
# contoh non function
# nama_lengkap = "alfadjri"
# jabat = "cybersecurity"
# print(f"Helo {nama_lengkap},Job : {jabat}") 
# nama_lengkap = "bob"
# jabat = "cybersecurity"
# print(f"Helo {nama_lengkap},Job : {jabat}") 



# Data mentah

profiles = [
    {
        "nama_lengkap" : "Alfadjri",
        "job" : None
    },   
    {
        "nama_lengkap" : "bob",
        "job" : None
    },   
    {
        "nama_lengkap" : "toni",
        "job" : None
    },   
    {
        "nama_lengkap" : "andi",
        "job" : None
    },   
    {
        "nama_lengkap" : "budi",
        "job" : None
    },
    {
        "nama_lengkap" : "siti",
        "job" : "Adminstrator"
    },
    
]


def perkenal(nama_lengkap, jabatan = "cybersecurity") :
    print("=========== Biodata ========")
    print(f"Nama\t: {nama_lengkap}\nJob\t: {jabatan}")
    print() 

for value in profiles:
    if value["job"] == None : # validation 
        perkenal(value['nama_lengkap'])
    else :
        perkenal(value['nama_lengkap'],value["job"])


def pembagian(a,b):
    hasil = a // b
    return float(hasil)


def cetak_nilai(a,b):
    hasil = pembagian(a,b)
    print(f"Hasil dari {a} / {b} = {hasil}")
    
    
cetak_nilai(10,2)
cetak_nilai(11,2)
cetak_nilai(12,2)
cetak_nilai(13,2)
cetak_nilai(14,2)
cetak_nilai(15,2)
cetak_nilai(16,2)
cetak_nilai(17,2)
cetak_nilai(18,2)
cetak_nilai(19,2)
cetak_nilai(20,2)




