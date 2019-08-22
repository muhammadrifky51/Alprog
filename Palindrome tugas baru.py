x=input("Program ini untuk mengecek apakah kalimat yang anda masukkan adalah palindrome atau bukan.\nPress enter to continue...")

kalimat=input("Masukkan sebuah kalimat: ")
cek=reversed(kalimat)
if list(kalimat)==list(cek):
    print(("%s adalah palindrome")%(kalimat))
else:
    print(("%s bukan palindrome")%(kalimat))