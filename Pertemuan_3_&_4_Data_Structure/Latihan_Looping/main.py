import os 
import platform

def clearTerminal():
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def errorMessage(pesan = "Value not valid"):
    input(f"{pesan}\nPlease press any key .....")

def persegi():
    try:
        sisi = int(input("Lebar sisi : "))
        if(sisi < 5):
            errorMessage("Lebar sisi harus lebih dari 5")
            return 
    except: #digunakan agar aplikasi tetap berjalan walaupun ada error
        errorMessage("Inputan harus berupa angka!!!")
    print("========Persegi=======")
    for i in range(sisi):
        for j in range(sisi):
            print("*",end=" ")
        print()
    print("Back to Menu utama")
    input("Please press any key .....")
    
def segitiga_siku_kiri_bawah(header, sisi):
    print(f"======={header}========")
    for y in range(1,sisi+1):
        for x in range(y):
            print("*",end=" ")
        print()
    print("Back to Menu utama")
    input("Please press any key .....")
def segitiga_siku_kiri_atas(header, sisi):
    print(f"======={header}========")
    for y in range(sisi,0,-1):
        for x in range(y):
            print("*",end=" ")
        print()
    print("Back to Menu utama")
    input("Please press any key .....")
    
def segitiga_siku_kanan_bawah(header, sisi):
    print(f"======={header}========")
    for y in range(1,sisi+1):
        for x in range(sisi - y):
            print(" ",end=" ")
        for z in range(y):
            print("*",end=" ")
        print()
    print("Back to Menu utama")
    input("Please press any key .....")
    
    

def segitiga_siku_kanan_atas(header, sisi):
    print(f"======={header}========")
    for y in range(sisi,0,-1):
        for x in range(sisi - y):
            print(" ",end=" ")
        for z in range(y):
            print("*",end=" ")
        print()
    print("Back to Menu utama")
    input("Please press any key .....")

    
def menu_segitiga():
    banyak_sisi = 5
    header = "Segitiga Siku-siku"
    print(f"======={header}========")
    print("1.kiri bawah")
    print("2.kanan atas")
    print("3.kanan bawah")
    print("4.kiri atas")
    print("q.back")
    select = input("Select => ")
    match select:
        case "1":
            clearTerminal()
            segitiga_siku_kiri_bawah(header,banyak_sisi)
        case "2":
            clearTerminal()
            segitiga_siku_kanan_atas(header,banyak_sisi)
        case "3":
            clearTerminal()
            segitiga_siku_kanan_bawah(header,banyak_sisi)
        case "4":
            clearTerminal()
            segitiga_siku_kiri_atas(header,banyak_sisi)
        case "q":
            return
        case _ :
            errorMessage()

def menu_fibonaci():
    header = "===========fibonaci======="
    try:
        data = int(input("Berapa banyak langkah "))
        if(data <= 0):
            errorMessage("Angka harus lebih besar dari 0")
            return 
    except: #digunakan agar aplikasi tetap berjalan walaupun ada error
        errorMessage("Inputan harus berupa angka!!!")
    data += 1
    nilai_awal = [0,1]
    for i in range(2,data):
        next_bilangan = nilai_awal[-1] + nilai_awal[-2]
        nilai_awal.append(next_bilangan)
    print()
    print(f"Deret bilangan fibonaci : {nilai_awal}")
    print("Back to Menu utama")
    input("Please press any key .....")
    

def main():
    while True:
        clearTerminal()
        print("========Latihan looping=======")
        print("1.Persegi")
        print("2.Segitiga Siku-siku")
        print("3.Fibonaci")
        print("q.Exit")
        select = input("Select => ")
        match select:
            case "1":
                clearTerminal()
                persegi()
            case "2":
                clearTerminal()
                menu_segitiga()
            case "3":
                clearTerminal()
                menu_fibonaci()
            case "q":
                break
            case _ :
                errorMessage()
if __name__ == "__main__":
    main()