import math

#Ini Program Utama
x=input("Masukkan nilai x : ")
n=input("Masukkan nilai n : ")
i=1
f=0
x=x*math.pi/180
while i<=n:
    a=(-1)**(i+1)
    b=x**((2*i)-1)
    d=1
    for j in range(1,((2*i)-1)):
        d=d*j
    e=a*b/d
    f=f+e
    i=i+1
g=math.sin(x)-f
h=abs(g)
print("nilai aproksimisi dari sin(%.2f) dengan n = %d adalah %.2f dengan galat %e")%(x,n,f,h)
print("\n")

#Ini menggunakan n=5
print("Gunakan x=330 derajat dan n=5")
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
print("nilai aproksimisi dari sin(%.2f) dengan n = %d adalah %.2f dengan galat %e")%(x,n,f,h)
print("\n")

#Ini menggunakan n=10
print("Gunakan x=330 derajat dan n=10")
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
print("nilai aproksimisi dari sin(%.2f) dengan n = %d adalah %e dengan galat %e")%(x,n,f,h)
print("\n")

#Ini menggunakan n=15
print("Gunakan x=330 derajat dan n=15")
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
print("nilai aproksimisi dari sin(%.2f) dengan n = %d adalah %E dengan galat %e")%(x,n,f,h)
print("\n")

#Ini menggunakan n=5
print("Gunakan x=330 derajat dan n=20")
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
print("nilai aproksimisi dari sin(%.2f) dengan n = %d adalah %E dengan galat %e")%(x,n,f,h)
print("\n")
print("Kesimpulan :\n\"Semakin besar n, maka semakin kecil galat yag di peroleh\"")