import random
nilaimax = input ("Masukkan nilai minimum yang ingin di input : ")
banyakdata = input ("Masukkan banyaknya data yang diinginkan : ")
i=0
jumlah=0

while i<banyakdata:
    data_n = random.randrange(1,nilaimax,1)
    jumlah=jumlah+data_n
    i=i+1
    print("data ke %s adalah %s")%(i,data_n)
rerata=jumlah/banyakdata
print("\nrerata dari %s data random adalah %s")%(banyakdata,rerata)