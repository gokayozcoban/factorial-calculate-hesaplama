sayi = int(input("Faktoriyeli hesaplanacak sayıyı girin: "))
sonuc = 1
i = 1
while (i <= sayi) :
    sonuc *= i
    i += 1
print ("%d sayisinin faktoriyeli = %d" %(sayi, sonuc))
