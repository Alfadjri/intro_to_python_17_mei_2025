open_file = open("../Create/Contoh_Text.txt",'r')
# untuk baca semua nilai
# readlines
# print(open_file.read())

# mengambil tulisan ini 
# putar posisi
open_file.seek(0)
# print(open_file.readline(3))

# satu baris
open_file.seek(0)
for line in open_file.readlines():
    print(line.strip(""))