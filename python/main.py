print("kodlamio")
baslik ="Taşıt kredisi"
print(baslik)
#stirng => metinsel ifade
baslik ="ihtiyaç kredisi"
print(baslik)
#int , integer => tam sayı
vade = 36
ekVade = 6
vade2 = "36"

# float,decimal,double
aylikOdeme = 200.50

# bool, boolen => True veya False
yukselisteMi = False

# matematiksel operatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5-5)
print(vade-12)
print(vade-ekVade)
print(36-6)

# *
print(5*5)
print(vade*2)
print(vade*ekVade)
print(36*6)

# /
print(5/5)
print(vade/2)
print(vade/ekVade)
print(36/6)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatörü
print(10%2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10) 


# mantıksal operatörler 
print(1 == 1)
print(1 == 2) 

# CTRL K + CTRL C
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)


print(1 != 1)
print(1 != 2)

# or and

#or => veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 < 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and  5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 or 3 > 2)  


# karar yapıları
# if else
sayi1 = 15
sayi2 = 15
# sayi1 sayi2 ' den büyükse ekrana sayı 1 daha büyük yazdır
#condition

#indent
if sayi1 <= sayi2:
    print("sayi 1 sayi 2'den küçüktür")
elif sayi1 == sayi2:
    print("iki sayı eşittir")
#eğer if ve else if bloklarında hiç birine girmez ise 
else:
    print("sayi 1 sayi 2'den büyüktür")

print("Burası if bloğunun dışındadır")














