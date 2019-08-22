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
rx=raw_input("Pesan anda akan segera di encrypt, Press enter to continue")
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