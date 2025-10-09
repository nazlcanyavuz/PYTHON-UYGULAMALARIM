kenar1 = float(input("1. Kenar Uzunluğu:"))
kenar2 = float(input("2. Kenar Uzunluğu:"))
kenar3 = float(input("3. Kenar Uzunluğu:"))
if kenar1 == kenar2 and kenar1 == kenar3:
    print("Eşkenar Üçgen")
elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
    print("İkizkenar Üçgen")
else:
    print("Çeşitkenar Üçgen")