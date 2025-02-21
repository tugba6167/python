faiz = 1.59
vade = 36
krediAdi = "İhtiyaç kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade)+12)
#print(int(krediAdi)
faiz = str(faiz)
print(type(faiz))

vade =36 #input("lütfen istediğiniz vade değerini giriniz")
print(type(vade))
vade = vade + 12

# string interpolation
# seçtiğiniz vade sonucu ortaya çıkan vade:
print("seçtiğinizvade sonucu ortaya çıkan vade: " + str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}" .format(vadeSayisi=vade))
print(f"seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "Halit" #input("isminizi giriniz")
metin = "Merhaba {name}".format(name=123)
print(metin)    


# f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)  


# listeler
# döngüler
# fonksiyonlar

dizi = ["İhtiyaç kredisi", 10,5.2, True]
print(dizi)

krediler = ["ihtiyaç kredisi", "Taşıt kredisi", "Konut kredisi"]

print(type(krediler))

print(krediler[0])
print(len(krediler)) #length
# print(krediler[3]) => hata verir

krediler.append("Özel kredi")
print(krediler)

krediler.append("X kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt kredisi")
print(krediler)


krediler.remove("Taşıt kredisi")
print(krediler)

krediler.extend(["Y kredisi" "Z kredisi"])
print(krediler)

# for
# i=0 i<1

for i in range(10):
    print("xx")
    print(i)

for i in range(0,51,10):
    print(i)


# print("****************"")
# for i in range(0.1,0.5):
#      print(i)

krediler = (["ihtiyaç kredisi", "Taşıt kredisi", "Konut kredisi"])
for kredi in krediler:
    print(kredi)

for i in range(len(krediler)):
    print(krediler[i])




# sonsuz döngü
while 1 < 10:
    print("x")
    i += 1
print("y")



while True:
    print("x")
    break

print("***son döngü*****")


krediler = ["ihtiyaç kredisi", "Taşıt kredisi", "Konut kredisi"]

i = 0
while i < len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "konut kredisi":
        break

#fonksiyonlar

fiyat = 100
indirim = 20    
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)


# sınıflar => classlar
# modules
# paket yönetimi

class human :
    def talk(self,sentence):
        print(f"human:{sentence}")
    def walk(self):
        print("human is walking")


# instance => örnek
human1 = human()
human1.talk("merhaba")
human1.walk()










    



    

    
          











