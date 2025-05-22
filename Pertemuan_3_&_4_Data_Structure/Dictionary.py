siswas = {
    "kelas" : 12,
    "jurusan" : ["ipa","ips",{
            "Teknik" : ["mesin","elektro"]
        }],
    "nama_ketua" : "udin",
}

#read all
print(f"isi semua data dictionary : {siswas}")

#read spesifik
print(f"Siswa sekarang berada di kelas : {siswas["kelas"]}")
print(f"Gimana caranya kalau saya mau ambil jurusan ips : {siswas['jurusan'][1]}")
print(f"Gimana caranya kalau saya mau ambil jurusan elektro : {siswas['jurusan'][2]["Teknik"][1]}")

# update
siswas["nama_ketua"] = "toni"
print(f"isi semua data dictionary : {siswas}")



# Delete
del siswas["jurusan"][2]
print(f"isi semua data dictionary : {siswas}")

# add value
siswas["teknik"] = ["mesin","elektro"]
siswas["teknik"] = 2
print(f"isi semua data dictionary : {siswas}")

# ambil semua key
print(f"Ambil semua key dictionary : {siswas.keys()}")