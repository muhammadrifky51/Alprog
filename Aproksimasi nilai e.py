print("Nama : Muhammad Rifky Yusdiansyah\nNPM : 1506671423")
p=raw_input("Press enter to continue....")
import math

#Ini Program Utama
x=input("Masukkan nilai x : ")
n=input("Masukkan nilai n : ")
e=float(1)
i=1
f=0
while i<=n:
    a=float((x)**(i))
    d=1
    j=1
    while j <= i:
        d=d*j
        j=j+1
    d=float(d)    
    e=e+(a/d)
    i=i+1
print("nilai e**(%s) dengan n=%s adalah %f")%(x,n,e)
nanya=raw_input("Ingin melihat error dari aproksimasi e**(%s)? (Y/N)\n")
if nanya=='y' or nanya== 'Y':
    print abs(((math.e)**x)-e)
else:
    print "Okay"