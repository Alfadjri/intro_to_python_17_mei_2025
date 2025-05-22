

#if
#di pakai kalau kita mau maksa kondisi tertentu
#format

#if kondisi :
#   Apa yang akan di lakukan kalau kondisi terpenuhi
print("===========if=========")
nilai_raport = 40
if nilai_raport >= 70 :
    print("Selamat kamu lulus dalam ujian ini!!!")
    
print("===========if-else=========")
# di pakai kalau kamu mau maksa nilai untuk melakukan sesuatu
if nilai_raport >= 70 :
    print("Selamat kamu lulus dalam ujian ini!!!")
else : 
    print("Kamu tidak lulus !!!!")

print("===========if-elif-else=========")
nilai_raport = 200
if nilai_raport > 100:
    print("nilai tidak boleh lebih dari 100")

#di pakai kalau check kondisinya lebih dari 2 
if nilai_raport >= 70 and nilai_raport < 100:
    print("Selamat kamu lulus dalam ujian ini!!!")
elif nilai_raport >= 50 and nilai_raport <= 60:
    if nilai_raport == 60: #teknik namanya if else bersarang
        print("sedikit lagi kamu lulus dengan nilai sempurna")
    print("Kamu harus melakukan remedial")
else : 
    print("Kamu tidak lulus !!!!")

# switch case
# ini di pakai kalau kamu sudah tau user mau ketikan apa secara akurat
print("=========== Switch Case =========")
print("=========== Menu utama =========")
print("1.Start")
print("2.exit")
select = input("Selection (1/2) => ")
match select:
    case "1":
        print("Start the game")
    case "2":
        print("See you !!!!")
    case _ :
        print("input not valid")
