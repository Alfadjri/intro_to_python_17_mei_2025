import datetime

tanggal = datetime.datetime.now().isoformat()
nama_lengkap = "Alfadjri Dwi Fadhilah"
hal = "Sosialisiasi Persyaratan Digital 4.0"

#posisional 
print("===============Posisional==================")
print("\t\t\t\t{0}\nNama\t: {1}\nHal\t: {2}".format(tanggal,nama_lengkap,hal))
print("===============Keyword==================")
print("\t\t\t\t{tanggal}\nNama\t: {nama}\nHal\t: {hal}".format(hal=hal,tanggal=tanggal,nama=nama_lengkap))
print("===============Cara singkat==================")
print(f"\t\t\t\t{tanggal}\nNama\t: {nama_lengkap}\nHal\t: {hal}")