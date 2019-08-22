angka1=input("Masukkan bilangan pertama : ")
angka2=input("Masukkan bilangan kedua : ")
hasil=str(angka1*angka2)
cekhasil=reversed(hasil)
print("\n")
if list(hasil)==list(cekhasil):
    print("bilangan %s adalah bilangan palindrome")%(hasil)
else:
    print("bilangan %s bukan bilangan palindrome")%(hasil)