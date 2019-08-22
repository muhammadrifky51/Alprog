print("Nama : Muhammad Rifky Yusdiansyah\nNPM : 1506671423")

from pprint import pprint
from random import randint
sum_penumpang=0
single=0
double=0
triple=0
quart=0
#Pesawat Kecil
PK = [[[0 for k in xrange(3)] for j in xrange(2)] for i in xrange(26)]
while sum_penumpang<156:
    grup=randint(1,4)
    if grup==1:
        single+=1
        sum_penumpang+=1
    elif grup==2:
        if 3*2*26-sum_penumpang==1:
            single+=1
            sum_penumpang+=1
        else:
            double+=1
            sum_penumpang+=2
    elif grup==3:
        if 3*2*26-sum_penumpang==1:
            single+=1
            sum_penumpang+=1
        elif 3*2*26-sum_penumpang==2:
            double+=1
            sum_penumpang+=2
        else:
            triple+=1
            sum_penumpang+=3
    else:
        if 3*2*26-sum_penumpang==1:
            single+=1
            sum_penumpang+=1
        elif 3*2*26-sum_penumpang==2:
            double+=1
            sum_penumpang+=2
        elif 3*2*26-sum_penumpang==3:
            triple+=1
            sum_penumpang+=3
        else:
            quart+=1
            sum_penumpang+=4
            
Singlelist=[["S1" for i in xrange(1)]for k in xrange(single)]
pprint(Singlelist)
print('\n')
Doublelist=[["G2" for i in xrange(2)]for k in xrange(double)]
pprint(Doublelist)
print('\n')
Triplelist=[["G3" for i in xrange(3)]for k in xrange(triple)]
pprint(Triplelist)
print('\n')
Quartlist=[["G4" for i in xrange(4)]for k in xrange(quart)]
pprint(Quartlist)
print('\n')
#Untuk ngisi pesawat kecil, dahulukan double untuk mengisi kiri pesawat
for i in range(0,double):
    for j in range(0,2):
        PK[i][0][j]=Doublelist[i][j]
#Dilanjutkan quart untuk mengisi bagian setelah double
for i in range(0,quart):
    for j in range(0,4):
        if j==3:
            PK[i][0][2]=Quartlist[i][3]
        else:
            PK[i][1][j]=Quartlist[i][j] 
#Dilanjutkan triple untuk mengisi kursi dengan 3 tempat duduk kosong
k=0
for i in range(0,triple):
    while k<26:
        tempat="T"
        l=0
        while l<2:
            if PK[k][l][2] ==0:
                for j in range(0,3):
                        PK[k][l][j]=Triplelist[i][j]
                tempat="F"
                break
            else:
                l+=1
        if tempat=="F":
            break
        else:
            k+=1
#Sisanya adalah memasukkan yang single
k=0
cek="T"
for i in range(0,26):
    for j in range(0,2):
        for m in range(0,3):
            if k==single:
                cek="F"
                break
            if PK[i][j][m]==0:
                PK[i][j][m]=Singlelist[k][0]
                k+=1
        if cek=="F":
            break
    if cek=="F":
        break
pprint(PK)
print('\n')
#Air Bus Buat posisi barisnya 2,4,2 terus 30 kebelakang
AB = [[[0 for k in xrange(2)],[0 for l in xrange(4)],[0 for m in xrange(2)]] for j in xrange(30)]
for i in range(0,4):
    for j in range (13,16):
        AB[j][1][i]=-1 #-1 Karena gaada kursinya
for i in range(24,30):
    AB[i][1][1]=-1 #-1 Karena gaada kursinya
#Sekarang untuk memindahkan orang-orang ke tempat duduk baru di Air bus
#Dimulai dari memindahkan double ke kiri dan ke kanan pesawat
l=0
cek="T"
for i in range(0,30):
    for j in range(0,3,2):#Karena yang j=1 belum ingin diisi
        m=0
        for k in range(0,2):
            if l==double:
                cek="F"
                break
            AB[i][j][k]=Doublelist[l][m]
            m+=1
        if cek=="F":
            break
        l+=1
    if cek=="F":
        break
#Selanjutnya memindahkan yang quart
#Quart akan dipindah ke tempat duduk dengan banyak 4, jika tempat duduk yang seharusnya tempatnya double itu kosong, maka 1 baris dapat di duduki oleh 2 kelompok quart
#Jika doublenya genap
if double%2==0:
    l=0
    m=0
    cek="T"
    for i in range(0,30):
        if i<(double/2):
            for k in range(0,4):
                if l==quart:
                    cek="F"
                    break
                AB[i][1][k]=Quartlist[l][k]
            l+=1
        else:
            if i==13:
                i=16
            for j in range(0,3):
                if j==0 or j==2:
                    for k in range(0,2):
                        if l==quart:
                            cek="F"
                            break
                        AB[i][j][k]=Quartlist[l][m]
                        m+=1
                        if m==4:
                            l+=1
                            m=0
                else:
                    for k in range(0,4):
                        if l==quart:
                            cek="F"
                            break
                        AB[i][j][k]=Quartlist[l][m]
                        m+=1
                        if m==4:
                            l+=1
                            m=0
                if cek=="F":
                    break
        if cek=="F":
            break
#Kalau doublenya ganjil
else:
    l=0
    m=0
    cek="T"
    for i in range(0,30):
        if i<((double+1)/2):
            for k in range(0,4):
                if l==quart:
                    cek="F"
                    break
                AB[i][1][k]=Quartlist[l][k]
            l+=1
        else:
            if i==13:
                i=16
            for j in range(0,3):
                if j==0 or j==2:
                    for k in range(0,2):
                        if l==quart:
                            cek="F"
                            break
                        AB[i][j][k]=Quartlist[l][m]
                        m+=1
                        if m==4:
                            l+=1
                            m=0
                else:
                    for k in range(0,4):
                        if l==quart:
                            cek="F"
                            break
                        AB[i][j][k]=Quartlist[l][m]
                        m+=1
                        if m==4:
                            l+=1
                            m=0
                if cek=="F":
                    break
        if cek=="F":
            break 
#Selanjutnya masukkan triple di belakang quart dan double
p=0
m=0
cek="T"
for x in range(16,30):
    for j in range(0,3):
        if j!=1:
            if j==2 and m==0:
                break
            for k in range(0,2):
                if p==triple:
                    cek="F"
                    break
                AB[x][j][k]=Triplelist[p][m]
                m+=1
                if m==3:
                    p+=1
                    m=0
        else:
            for k in range(0,4):
                if x==13:
                    x=16
                if AB[x][j][k]==-1:
                    break
                if p==triple:
                    cek="F"
                    break
                AB[x][j][k]=Triplelist[p][m]
                m+=1
                if m==3:
                    p+=1
                    m=0
        if cek=="F":
            break
    if cek=="F":
        break
#Memasukan yang single di tempat kosong
l=0
cek="T"
for i in range(0,30):
    for j in range(0,3):
        if j!=1:
            for k in range(0,2):
                if l==single:
                    cek="F"
                    break
                if AB[i][j][k]==0:
                    AB[i][j][k]=Singlelist[l][0]
                    l+=1
        else:
            for k in range(0,4):
                if l==single:
                    cek="F"
                    break
                if AB[i][j][k]==0:
                    AB[i][j][k]=Singlelist[l][0]
                    l+=1 
pprint(AB)