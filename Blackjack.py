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
    enter=input("Press enter to Continue (H for Help)")
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
        print(("Total Score yang dipegang = %d")%(sum(angkaasli)))
        break
    else:
        if sum(angkaasli)==21:
            print("\n")
            print(pemain)
            print(("Total Score yang dipegang = %d")%(sum(angkaasli)))
            break
        else:pass
    print(pemain)
    print(("Total Score yang dipegang = %d")%(sum(angkaasli)))
    nanya=input("ingin mengambil kartu (Y/N)? ")
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
        nanya1=input("Ingin mengambil kartu lagi (Y/N)? ")
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
    print(("Kartu Dealer = %s")%(dealer))
    print("Permainan seri")
else:
    if sum(angkaasliD)>21:
        print("Pemain menang, kartu dealer lebih dari 21")
##############################################
#NGITUNG SCORE
    else:
        if sum(angkaasli)>21 or sum(angkaasli)<sum(angkaasliD):
            print("\nAnda Kalah")
            print(("Angka Dealer adalah %d")%(sum(angkaasliD)))
            print(("Jumlah kartu player adalah %d")%(sum(angkaasli)))
        else:
            if sum(angkaasli)==sum(angkaasliD):
                print(("\nPermainan Seri dengan score %s untuk dealer dan %s untuk pemain")%(sum(angkaasliD),sum(angkaasli)))
            else:
                print("\nAnda Menang") 
                print(("Angka Dealer adalah %d")%(sum(angkaasliD)))