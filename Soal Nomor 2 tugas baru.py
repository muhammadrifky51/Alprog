a=input("Bentuk apa yang diinginkan? \n1 untuk belah ketupat \n2 untuk segitiga siku-siku \n3 untuk pohon natal \nPilihan anda :")
b=input("Berapa input yang ingin dimasukkan : ")
i=0
c="*"
e=" "
print("\n")
if a==1:
    while i<b :
        d= (b-i)*e + c + (2*i)*c
        i=i+1
        print(d)
    while i!=-1:
        d= (b-i)*e + c + (2*i)*c
        i=i-1
        print(d)
else:
    if a==2:
        while i<b :
            d=5*e + c + i*c
            i=i+1
            print(d)
    else:
        if a==3:
            while i<b :
                d= (b-i)*e + c + (2*i)*c
                i=i+1
                print(d)
        else:
            print("input salah")