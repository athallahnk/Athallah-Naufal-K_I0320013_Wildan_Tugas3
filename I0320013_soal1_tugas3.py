#Mengisi list
list_teman= ["Naufal", "Ahmed", "Raka", "Wisnu", "Wastu", "Vito", "Salma", "Sabiq", "Dimas", "Momo"]
#Menampilkan isi list indeks nomor 4,6,7.
print("list_teman[4]:", list_teman[4])
print("list_teman[6]:", list_teman[6])
print("list_teman[7]:", list_teman[7])
#Mengganti nama teman di list 3,5,9
list_teman[3]= "Fawwaz"
list_teman[5]= "Athan"
list_teman[9]= "Tenz"
print(list_teman)
#Menambahkan teman
list_teman.append("Dani")
list_teman.append("Fahri")
print(list_teman)
#Menaampilkan semua teman dengan perulangan
for a in list_teman:
    print(a)
#Menampilkan panjang list
panjang_list = len(list_teman)
print(panjang_list)