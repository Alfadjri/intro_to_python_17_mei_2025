makanans = ["nasi","ikan","ayam"]
# Read all
print(f"isi data list :{makanans}")
# Read spesifik
print(f"isi data dari index ke 2 : {makanans[2]}")
# tantangan
print(f"isi data dari index ke -2 : {makanans[-2]}")

# update
makanans[0] = "sayuran"
print(f"isi data list setelah index ke 0 di update :{makanans}")

# add (append)
makanans.append("nasi")
print(f"isi data list setelah di tambahkan nasi :{makanans}")

# delete
makanans.remove("nasi")
print(f"isi data list setelah di hapus nasi :{makanans}")

# list add list
# makanans = makanans + ["Tomat","Alpukat"]
makanans += ["Tomat","Alpukat"]
print(f"isi data list setelah di tambahkan list Tomat dan Alpukat  :{makanans}")