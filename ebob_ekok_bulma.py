sayi1 = int(input("1.Sayı:"))
sayi2 = int(input("2.Sayı:"))
if sayi1<sayi2 :
    kucukSayi = sayi1
else:
    kucukSayi = sayi2
for i in range(1, kucukSayi+1):
    if sayi1%i==0 and sayi2&i==0:
        ebob = i
ekok = (sayi1*sayi2)//ebob 
print("EBOB:",ebob)
print("EKOK:",ekok)
