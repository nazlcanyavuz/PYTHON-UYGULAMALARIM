vize = float(input("Vize Notu:"))
proje = float(input("Proje Notu:"))
final = float(input("Final Notu:"))
ortalama = (vize*0.30) + (proje*0.30) + (final*0.40)
if ortalama>=50:
    sonuc = "GEÇTİ"
else:
    sonuc = "KALDI"
print(sonuc)
