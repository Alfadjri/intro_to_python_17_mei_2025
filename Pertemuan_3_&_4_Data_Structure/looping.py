#while
#sifatnya di check terlebih dahulu baru di jalankan
#sifatnya dijalankan tapi gak tau cara untuk berhenti
banyak_kata = 1000
print("==========while========")
while banyak_kata <= 1000:
    print(f"{banyak_kata}.I Love you ❤️")
    banyak_kata += 1
print("===========for========")
print("==========Range========")
# di gunakan saat kamu tau kapan mulai dan kapan berhenti
for i in range(1,2):
    print(f"{i}.I Love you ❤️")
print("==========Tipe data list========")
makanas = ['sayuran', 'ikan', 'ayam', 'Tomat', 'Alpukat']
count = 1
for value in makanas:
    print(f"{count}.{value}")
    count += 1
    
print("==========Continue and break========")
angka = 1
while angka <= 100:
    if angka % 2 == 0 :
        angka+=1
        continue # ini di pakai untuk skip atau melewati 1 putran
    
    print(f"{angka}")
    angka+=1
    
    if angka >= 30:
        break # ini di pakai untuk memaksa looping behenti