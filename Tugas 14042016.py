print("Program by \nMuhammad Rifky Yusdiansyah (1506671423)\nJeffry Nuari Pakpahan (1506726731)\nRizky Putra Okfradifa (1506741303)")
while True:
    nanyasoal=input("Ingin menjalankan program apa?\n1-Untuk Palindrome\n2-Untuk Blackjack\nSelain 1&2- untuk Kriptografi\nPilihan : ")
    if nanyasoal==1:
        #Palindrome
        x=raw_input("Program ini untuk mengecek apakah kalimat yang anda masukkan adalah palindrome atau bukan.\nPress enter to continue...")

        kalimat=raw_input("Masukkan sebuah kalimat: ")
        cek=reversed(kalimat)
        if list(kalimat)==list(cek):
            print("%s adalah palindrome")%(kalimat)
        else:
            print("%s bukan palindrome")%(kalimat)
    else:
        if nanyasoal==2:
            #Blackjack
            import random
            #INISIATOR
            dealer=[]
            pemain=[]
            kartu=['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K']
            angkaasli=[]
            angkaasliD=[]
            #####################
            #Pembukaan Game
            while True:
                enter=raw_input("Press enter to Continue (H for Help)")
                if enter=="":
                    break
                else:
                    print("Ini adalah permainan Blackjack!!\nAturan Game :\n\t-Diawal permainan Dealer akan diberikan 2 buah kartu tertutup.\n\t-Lalu pemain akan menarik 2 buah kartu.\n\t-Pemain di bebaskan untuk mengambil kartu sebanyak-banyaknya.\n\t-Jika jumlah kartu di tangan melebihi 21, pemain kalah.\n\t-Jika pemain sudah selesai mengambil kartu, Dealer membuka kartunya.\n\t-Jika jumlah kartu Dealer kurang dari 17, dealer wajib mengambil kartu kembali.\n\t-Jika kartu dealer lebih dari 17, dealer dibebaskan untuk mengambil kartu atau mencukupi.\n\t-Jika kartu dealer lebih dari 21, pemain menang.\n\t-Pemenangnya adalah yang memiliki nilai kartu terbanyak.\n\tNilai kartu :\n\t\t-Nilai As bernilai 11.\n\t\t-Nilai kartu angka, bernilai sebesar angka.\n\t\t-Untuk kartu Jack, Queen, King bernilai 10\n\nSELAMAT BERMAIN!!!")
            ######################
            #DEALER TURN
            print("\nDealer Turn!")
            while len(angkaasliD)<2:
                c=random.choice(kartu)
                dealer.append(c)
                if c=='A':
                    d=11
                    angkaasliD.append(d)
                    kartu.remove(c)
                else:
                    if c=='J' or c=='Q'or c=='K':
                        d=10
                        angkaasliD.append(d)
                        kartu.remove(c)
                    else:
                        angkaasliD.append(c)
                        kartu.remove(c)
            ###################################
            #PLAYER TURN
            print("\nPlayer Turn!")
            c=random.choice(kartu)
            pemain.append(c)
            if c=='A':
                d=11
                angkaasli.append(d)
            else:
                if c=='J' or c=='Q'or c=='K':
                    d=10
                    angkaasli.append(d)
                    kartu.remove(c)
                else:
                    angkaasli.append(c)
                    kartu.remove(c)
            while True:
                c=random.choice(kartu)
                pemain.append(c)
                if c=='A':
                    d=11
                    angkaasli.append(d)
                    kartu.remove(c)
                else:
                    if c=='J' or c=='Q'or c=='K':
                        d=10
                        angkaasli.append(d)
                        kartu.remove(c)
                    else:
                        angkaasli.append(c)
                        kartu.remove(c)
                if sum(angkaasli)>21:
                    print("\n")
                    print(pemain)
                    print("Total Score yang dipegang = %d")%(sum(angkaasli))
                    break
                else:
                    if sum(angkaasli)==21:
                        print("\n")
                        print(pemain)
                        print("Total Score yang dipegang = %d")%(sum(angkaasli))
                        break
                    else:pass
                print(pemain)
                print("Total Score yang dipegang = %d")%(sum(angkaasli))
                nanya=raw_input("ingin mengambil kartu (Y/N)? ")
                if nanya=='y' or nanya=='Y':
                    pass
                else:
                    break
            #############################################
            #DEALER TURN LAGI!
            print("DEALER MEMBUKA KARTU")
            print(dealer)
            while True:
                while sum(angkaasliD)<17:
                    c=random.choice(kartu)
                    dealer.append(c)
                    if c=='A':
                        d=11
                        angkaasliD.append(d)
                        kartu.remove(c)
                    else:
                        if c=='J' or c=='Q'or c=='K':
                            d=10
                            angkaasliD.append(d)
                            kartu.remove(c)
                        else:
                            angkaasliD.append(c)
                            kartu.remove(c)
                        print(dealer)
                if sum(angkaasliD)>=21:
                    break
                else:
                    nanya1=raw_input("Ingin mengambil kartu lagi (Y/N)? ")
                    if nanya1=='Y' or nanya1=='y':
                        c=random.choice(kartu)
                        dealer.append(c)
                        if c=='A':
                            d=11
                            angkaasliD.append(d)
                        else:
                            if c=='J' or c=='Q'or c=='K':
                                d=10
                                angkaasliD.append(d)
                            else:
                                angkaasliD.append(c)
                    else:
                        break
            ##########################################
            #NGECEK AJA
            if sum(angkaasliD)>21 and sum(angkaasli)>21:
                print("\n")
                print("Kartu Dealer = %s")%(dealer)
                print("Permainan seri")
            else:
                if sum(angkaasliD)>21:
                    print("Pemain menang, kartu dealer lebih dari 21")
            ##############################################
            #NGITUNG SCORE
                else:
                    if sum(angkaasli)>21 or sum(angkaasli)<sum(angkaasliD):
                        print("\nAnda Kalah")
                        print("Angka Dealer adalah %d")%(sum(angkaasliD))
                        print("Jumlah kartu player adalah %d")%(sum(angkaasli))
                    else:
                        if sum(angkaasli)==sum(angkaasliD):
                            print("\nPermainan Seri dengan score %s untuk dealer dan %s untuk pemain")%(sum(angkaasliD),sum(angkaasli))
                        else:
                            print("\nAnda Menang") 
                            print("Angka Dealer adalah %d")%(sum(angkaasliD))
        else:
            i=0
            kode=[]
            c=""
            d=""
            x=raw_input("Ini Program untuk mengenkripsi sebuah pesan, ketik H untuk bantuan, enter untuk melanjutkan\n")
            if x=="":
                pass
            else:
                print("\nSelamat datang di program enkripsi pesan!!!\nKamu akan diminta untuk memasukkan sebuah angka untuk enkripsi\nAngka tersebut digunakan untuk mengenkripsi pesan kamu\nMisal:\n  Kamu memasukkan angka 2, maka huruf A akan berubah menjadi C dan seterusnya.\n  Kamu memasukkan angka 4, maka huruf A akan menjadi huruf E dan seterusnya.\n\nSELAMAT MENJALANKAN PROGRAM!!!")
            while True:
                n=input("Masukkan sebuah angka untuk enkripsi : ")
                if n<0 :
                    input("Mohon maaf untuk bilangan minus belum bisa dijadikan bilangan enkripsi")
                else:
                    break
            pesan=raw_input("Masukkan sebuah pesan: ")
            a=list(pesan)
            n=n%26
            while i<len(a):
                b=ord(a[0])+n
                kode.append(b)
                if c=="":
                    c=str(b)
                else:
                    c=c+" "+str(b)
                del a[0]
            x=raw_input("Pesan anda akan segera di encrypt, Press enter to continue")
            print c
            x=raw_input("Encrypting...")
            while i<len(kode):
                if kode[0]-n==32:
                    kode[0]=int(kode[0]-n)
                    e=chr(int(kode[0]))
                    if d=="":
                        d=str(e)
                    else:
                        d=d+str(e)
                else:
                    if kode[0]>122:
                        kode[0]=int(kode[0]-26)
                        e=chr(int(kode[0]))
                        if d=="":
                            d=str(e)
                        else:
                            d=d+str(e)
                    else:
                        if kode[0]>90 and kode[0]<ord('a')+n:
                            kode[0]=int(kode[0]-26)
                            e=chr(int(kode[0]))
                            if d=="":
                                d=str(e)
                            else:
                                d=d+str(e)
                        else:
                            e=chr(int(kode[0]))
                            if d=="":
                                d=str(e)
                            else:
                                d=d+str(e)
                    del kode[0]
            print d 
    nanyalagi=raw_input("Ingin menjalankan program kembali? (Y/N)\n")
    if nanyalagi=='y' or nanyalagi=='Y':
        pass
    else:
        break
        
print("Program Keluar")