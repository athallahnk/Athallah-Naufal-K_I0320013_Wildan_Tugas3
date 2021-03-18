#Input data
Identitas= {'Nama':'Athallah Naufal Kuranityo','Hobi':['Catur','Badminton','Berenang'],'Instagram':'athallahnk','Facebook':'Athan Naufal','ID Line':'atha170702',
             'Lagu Favorit':['Melukis Senja','To the Bone','Into Your Arms','Mungkin Hari Ini Esok atau Nanti'], 'Makanan Favorit':['Kebab','Nasi Goreng','Martabak','Bakso']}
#Mengubah salah satu hobi
Identitas['Hobi']= "Catur, Badminton, Game"
#Menambahkan hobi
Identitas['Hobi']= " Catur, Badminton, Game, Bernyanyi"
#Mengubah salah satu media sosial
Identitas['Facebook']= "Naufal Athan"
#Menghapus dua makanan favorit
del Identitas['Makanan Favorit']
Identitas['Makanan Favorit']= "Martabak, Bakso"

print(Identitas)
