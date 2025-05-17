# tipe data primitif
# integer
x = 32767
print("ini contoh tipe data integer : {0}".format(x))
# float
y = 3.7
print("ini contoh tipe data float : {0}".format(y))
z = 2 + 3j
print("ini contoh tipe data kopleks : {0}".format(z))

#tipe data char
c = 'A'
print("ini contoh tipe data char(varChar) : {0}".format(c))
#tipe data non primitif
#string (str)
#string => char(255)
nama_depan = "alfadjri dwi fadhilah"
print("ini contoh tipe data string : {0}".format(nama_depan))

#tipe data quence 
#list di gunakan sebisa mungkin tipe datanya sama semua
a = [24,35,35,40]
print("ini contoh tipe data list : {0}".format(a))
#truplet
b = (5,3,10)
print("ini contoh tipe data truplet : {0}".format(b))
#rentang (range)
#format dasar range(start,end,step)
r = range(0,5,+1)
print("ini contoh tipe data range : {0}".format(r))

#tipe data maping
profile = {"nama": "alfadjri dwi fadhilah","age" : 24}
print("ini contoh tipe data dict : {0}".format(profile))

#set
#tipe data yang tidak bisa di ubah kembali atau final
f = {1,2,3}
print("ini contoh tipe data set : {0}".format(f))
f = frozenset({4,5,6})
print("ini contoh tipe data forzenset : {0}".format(f))

#tipe data kondisi
#boolean nilai nya hanya 2 True(1) atau False(0)
kondisi_angka = 1
#conversi
kondisi_angka_conversi = bool(kondisi_angka)
print("ini contoh tipe data bool (simbol) : {0}".format(kondisi_angka))
print("ini contoh tipe data bool (non_simbol): {0}".format(kondisi_angka_conversi))

#binary
i = 0b01000001
# decimal = int(i)
# print("tahap conversi binary : {0}".format(decimal))
# char = chr(decimal)
# print("tahap conversi desimal to char : {0}".format(char))
char = chr(int(i))
print("Character binary : {0}".format(char))
j = bytearray(a)
print("isi dari array list : {0}".format(j))
z = memoryview(j)
print("lokasi dari nilai j : {0}".format(z))
