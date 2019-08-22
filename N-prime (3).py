print("Kelompok 8B\nAnggota:\n\t-Adni Adzkiah\n\t-Laudza Satria Naufal Putra\n\t-Muhammad Rifky Yusdianysah\n\t-Muhammad Usamah\n\t-Tri Puji Marjadi")

#INISIASI PROGRAM
angkacek=2 #Dimulai dari angka 2 karena bilangan prima terkecil adalah 2
n=eval(input("Ingin mencari bilangan prima ke "))
prima = []
if n>0:
    while len(prima)<n:
        if angkacek==2:
            prima.append(angkacek)
            angkacek+=1
        else:
            bilprim="Y"
            for a in range (3,angkacek,2): #Logikanya yang akan dicek adalah bilangan ganjil, artinya kita gaperlu mengecek dengan pembagi genap
                if angkacek%a==0:
                    bilprim="N"
                    break
            if bilprim=="Y":
                prima.append(angkacek)
            angkacek+=2 #angkacek ditambah 2 agar angka yang dicek adalah bilangan ganjil, mengingat angka prima yang genap hanya angka 2              
    print(("\nAngka prima ke %s adalah %s\n")%(n,prima[len(prima)-1]))
    print(("%s bilangan prima pertama adalah\n%s")%(n,prima))
else:
    print("n harus bilangan lebih dari 0")