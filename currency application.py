import requests
url="http://api.fixer.io/latest?base="
birinci=input("Çevirmek istediğiniz birim:")
ikinci=input("Çevireceğiniz birim:")
miktar=float(input("Miktarı giriniz:"))

deger=requests.get(url+birinci)
json_veri=deger.json()

print(float(json_veri["rates"][ikinci])*miktar)
