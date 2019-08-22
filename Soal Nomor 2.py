n=input("Masukkan n : ")
def a(n):
    if n==1:
        return (n)
    else:
        return(2*a(n-1))
print(a(n))