sayi = int(input("Sayı giriniz: "))
if sayi == 0:
    sonuc = 0
else:
    if sayi > 0:
        sonuc = "pozitif"
    else:
        sonuc = "negatif"
print(sonuc)
