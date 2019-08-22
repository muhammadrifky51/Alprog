print("Nama : Muhammad Rifky Yusdiansyah\nNPM : 1506671423")

loop1=0
loop2=1
while loop1<loop2 :
    soal=input("ingin menjalankan program untuk nomor berapa?\npilihan :\n1 untuk soal nomor 1 (program aproksimasi nilai sin(x))\n2 untuk soal nomor 2 (program yang bintang-bintang)\n3 untuk soal nomor 3 (program untuk menghitung rata-rata)\n4 untuk soal nomor 4 (program menentukan bilangan palindrome atau bukan)\npilih : ")
    if soal ==1:
        
        #SOAL NOMOR 1
        
        import math
        print("\nIni adalah program untuk soal nomor 1")
        #Ini menggunakan n=5
        print("Dengan menggunakan x=330 derajat dan n=5")
        x=330
        n=5
        i=1
        f=0
        x=x*math.pi/180
        while i<=n:
            a=(-1)**(i+1)
            b=x**((2*i)-1)
            d=1
            for j in range(1,((2*i))):
                d=d*j
            e=a*b/d
            f=f+e
            i=i+1
        g=math.sin(x)-f
        h=abs(g)
        print("nilai aproksimasi dari sin(%.2f) dengan n = %d adalah %f dengan galat %e")%(x,n,f,h)
        print("\n")
        
        #Ini menggunakan n=10
        print("Dengan menggunakan x=330 derajat dan n=10")
        x=330
        n=10
        i=1
        f=0
        x=x*math.pi/180
        while i<=n:
            a=(-1)**(i+1)
            b=x**((2*i)-1)
            d=1
            for j in range(1,((2*i))):
                d=d*j
            e=a*b/d
            f=f+e
            i=i+1
        g=math.sin(x)-f
        h=abs(g)
        print("nilai aproksimasi dari sin(%.2f) dengan n = %d adalah %f dengan galat %e")%(x,n,f,h)
        print("\n")
        
        #Ini menggunakan n=15
        print("Dengan menggunakan x=330 derajat dan n=15")
        x=330
        n=15
        i=1
        f=0
        x=x*math.pi/180
        while i<=n:
            a=(-1)**(i+1)
            b=x**((2*i)-1)
            d=1
            for j in range(1,((2*i))):
                d=d*j
            e=a*b/d
            f=f+e
            i=i+1
        g=math.sin(x)-f
        h=abs(g)
        print("nilai aproksimasi dari sin(%.2f) dengan n = %d adalah %f dengan galat %e")%(x,n,f,h)
        print("\n")
        
        #Ini menggunakan n=20
        print("Dengan menggunakan x=330 derajat dan n=20")
        x=330
        n=20
        i=1
        f=0
        x=x*math.pi/180
        while i<=n:
            a=(-1)**(i+1)
            b=x**((2*i)-1)
            d=1
            for j in range(1,((2*i))):
                d=d*j
            e=a*b/d
            f=f+e
            i=i+1
        g=math.sin(x)-f
        h=abs(g)
        print("nilai aproksimasi dari sin(%.2f) dengan n = %d adalah %f dengan galat %e")%(x,n,f,h)
        print("\n")
        print("Kesimpulan :\n\"Semakin besar n, maka semakin kecil galat yag di peroleh\"")
    else:
        if soal==2:
            
            #SOAL NOMOR 2
            
            print("\nIni adalah program untuk soal nomor 2")
            a=input("Bentuk apa yang diinginkan? \n1 untuk belah ketupat \n2 untuk segitiga siku-siku \n3 untuk pohon natal \nPilihan anda : ")
            b=input("Berapa input yang ingin dimasukkan : ")
            i=1
            c="*"
            e=" "
            print("\n")
            if a==1:
                #Belah ketupat
                while i<b :
                    d= (b-i)*e + (2*i-1)*c
                    i=i+1
                    print(d)
                while i!=-1:
                    d= (b-i)*e + (2*i-1)*c
                    i=i-1
                    print(d)
            else:
                if a==2:
                    #Segitiga Sikusiku
                    while i<b :
                        d=5*e + c + i*c
                        i=i+1
                        print(d)
                else:
                    if a==3:
                        #Pohon Natal
                        while i<b :
                            d= (b-i)*e + c + (2*i)*c
                            i=i+1
                            print(d)
                    else:
                        print("input salah")
        else:
            if soal==3:
                
                #SOAL NOMOR 3
                
                print("\nIni adalah program untuk soal nomor 3")
                banyakdata=input("Ada berapa data yang ingin di input?\n")
                i=1
                cek=0
                jumlah=0
                while i<=banyakdata:
                    data=input("Berapa nilai yang ingin di input?\n")
                    banyak=input("Ada berapa data yang bernilai "+str(data)+"?\n")
                    hasilkali=data*banyak
                    jumlah=jumlah+hasilkali
                    i=i+banyak
                    cek=cek+banyak
                if cek>banyakdata:
                    print("Banyaknya data salah")
                else:
                    mean=jumlah/banyakdata
                    print("Rata-rata dari %d data yang diinput adalah\n%.2f")%(banyakdata,mean)
            else:
                if soal==4:
                    
                    #SOAL NOMOR 4
                    
                    print("\nIni adalah program untuk soal nomor 4")
                    angka1=100
                    angka2=100
                    num1=0
                    while angka2<1000:
                        angka3=angka1*angka2
                        angka3=str(angka3)
                        cekangka=reversed(angka3)
                        if list(angka3)==list(cekangka):
                            angka3=int(angka3)
                            if num1<angka3:
                                angka4=angka1
                                angka5=angka2
                                num1=0
                                num1=num1+angka3
                            else:pass
                        else:pass
                        if angka2<=999 and angka1!=999:
                            angka1=angka1+1
                        else:
                            if angka2!=999 and angka1==999:
                                angka1=100
                                angka2=angka2+1
                            else:
                                if angka1==999 and angka2==999:
                                    break
                    print("Bilangan palindrome terbesar dari rentang 100x100 sampai 999x999 adalah %s*%s=%s")%(angka4,angka5,num1)
                else:
                    print("Input Salah")
    nanya=input("Ingin mencoba nomor lain apa ingin keluar dari program?\n1 untuk mencoba nomor lain\n0 untuk keluar dari program\nMasukkan angka : ")
    if nanya==1:
        loop1=loop1+1
        loop2=loop2+1
    else:
        if nanya==0:
            loop2=0
            print("\nProgram keluar")
        else:
            print("\nInput salah, program akan keluar secara otomatis")
            loop2=0
print("\nTerima kasih sudah menjalankan program ini!")