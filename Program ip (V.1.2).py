sem = eval(input('Semester anda : '))
p=0
ipprev=0
sksprev=0
var1=0
ipkum=0
skskum=0
if sem>12 :
    print('Seharusnya anda sudah di DO')
else :
    if sem<=12 :
        while p<sem:
            ipprev=eval(input("Berapa ip anda : "))
            sksprev=eval(input("Berapa sksnya : ")) 
            var1= ipprev*sksprev
            ipkum=ipkum+var1
            skskum=skskum+sksprev
            p=p+1
    skstot = eval(input('Berapa sks yang diambil semester ini : '))
    matkultotal = eval(input('Berapa matkul yang di ambil : '))
    i=0
    a=0
    aprev=0
    sks=0
    skslulus=0
    b=0
    bprev=0
    while i<matkultotal:
        f=eval(input('Masukkan nilai matkul anda : '))
        g=eval(input('Masukkan jumlah sks matkulnya : '))
        if f<40 :
            print('Nilai anda adalah E')
            a= 0*g
            sks=sks+g
            skslulus=skslulus+0
            b=0
        else :
            if f>=40 and f<55 :
                print('Nilai anda adalah D')
                a= 1*g
                sks=sks+g
                skslulus=skslulus+0
                b=0
            else :
                if f>=55 and f<60 :
                    print('Nilai anda adalah C')
                    a= 2*g
                    sks=sks+g
                    skslulus=skslulus+g
                    b= 2*g
                else :
                    if f>=60 and f<65 :
                        print('Nilai anda adalah C+')
                        a= 2.3*g
                        sks=sks+g
                        skslulus=skslulus+g
                        b= 2.3*g
                    else :
                        if f>=65 and f<70 :
                            print('Nilai anda adalah B-')
                            a= 2.7*g
                            sks=sks+g
                            skslulus=skslulus+g
                            b= 2.7*g
                        else :
                            if f>=70 and f<75 :
                                print('Nilai anda adalah B')
                                a= 3*g
                                sks=sks+g
                                skslulus=skslulus+g
                                b= 3*g
                            else :
                                if f>=75 and f<80 :
                                    print('Nilai anda adalah B+')
                                    a= 3.3*g
                                    sks=sks+g
                                    skslulus=skslulus+g
                                    b= 3.3*g
                                else :
                                    if f>=80 and f<85 :
                                        print('Nilai anda adalah A-')
                                        a= 3.7*g
                                        sks=sks+g
                                        skslulus=skslulus+g
                                        b= 3.7*g
                                    else :
                                        if f>=85 :
                                            print('Nilai anda adalah A')
                                            a= 4*g
                                            sks=sks+g
                                            skslulus=skslulus+g
                                            b= 4*g
        aprev=aprev+a
        bprev=bprev+b
        i=i+1
    if sks!=skstot :
        print('sks total salah')
    else :
        ipktotal = bprev/skslulus
        iptotal = aprev/skstot
        print(('ips anda adalah %f dan ipk anda adalah %f')%(iptotal,ipktotal))