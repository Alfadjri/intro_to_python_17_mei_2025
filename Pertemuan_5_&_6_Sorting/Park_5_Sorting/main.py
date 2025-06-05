import random


def generate_random_value(value):
    list_data = []
    for i in range(0,value+1):
        random_value = random.randint(1,100)
        list_data.append(random_value)
    return list_data

def bubble_sort(data):
    jumlah_data = len(data)
    for i in range(jumlah_data):
        for j in range(0,jumlah_data-i-1):
            if data[j] > data[j+1]:
                # temp = data[j]
                # data[j] = data[j+1]
                # data[j+1] = temp
                data[j] , data[j+1] = data[j+1] , data[j]
def selection_sorting(data):
    jumlah_data = len(data)
    for i in range(jumlah_data):
        min_index = i
        for j in range(i+1,jumlah_data):
            if data[j] < data[min_index]:
                min_index = j
        data[i] , data[min_index] = data[min_index] , data[i]       

def main():
    banyak_angka = int(input("Banyak Angka yang akan di ambil : "))
    list_data = generate_random_value(banyak_angka)
    print("List data yang akan di acak")
    print(list_data)
    input("Tekan enter untuk melanjutkan tahapan ......")
    # bubble_sort(list_data)
    selection_sorting(list_data)
    print("List data setelah di sorting")
    print(list_data)

if __name__ == "__main__":
    main()