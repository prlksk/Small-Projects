print("1-Toplama")
print("2-Çıkarma")
print("3-Bölme")
print("4-Çarpma")
print("5- Kare Al")
print("6- Kök Al")
print("q- Çıkış")
 
while True:
    scanner = input("Lütfen yapmak istediğiniz işlemin numarasını seçiniz ")    
 
    if scanner == "q":
        print("Çıkış")
        break
 
    elif scanner == "1":
        scannerToplama1 = input("Toplamak istediğiniz 1. sayıyı giriniz: ")
        scannerToplama2 = input("Toplamak istediğiniz 2. sayıyı giriniz: ")
        sonuc = int(scannerToplama1) + int(scannerToplama2)
        print(sonuc)
 
    elif scanner == "2":
        scannerCikarma1 = input("Çıkarma yapmak istediğiniz sayıyı giriniz: ")
        scannerCikarma2 = input("Çıkarılacak sayıyı giriniz: ")
        sonuc = int(scannerCikarma1)- int(scannerCikarma2)
        print(sonuc)
 
    elif scanner == "3":
        scannerBolme1 = input("Bölünecek sayıyı giriniz: ")
        scannerBolme2 = input("Bölmek istediğiniz sayıyı giriniz: ")
        sonuc = int(scannerBolme1) / int(scannerBolme2)
        print(sonuc)
 
    elif scanner == "4":
        scannerCarpma1 = input("Çarpmak istediğiniz 1. sayıyı giriniz: ")
        scannerCarpma2 = input("Çarpmak istediğiniz 2. sayıyı giriniz: ")
        sonuc = int(scannerCarpma1) * int(scannerCarpma2)
        print(sonuc)
 
    elif scanner == "5":
        scannerKare = input("Karesin almak istediğiniz sayıyı giriniz: ")
        sonuc = int(scannerKare) ** 2
        print(sonuc)
 
    elif scanner == "6":
        scannerKok = input("Karekökünü almak istediğiniz sayıyı giriniz: ")
        sonuc = int(scannerKok) ** 0.5
        print(sonuc)
 
    else:
        print("Yanlış bir rakam girdiniz lütfen yeniden giriniz.")
