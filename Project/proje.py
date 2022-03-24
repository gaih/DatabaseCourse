from rehber import *

print("""***********************************

Global AI Hub Telefon Rehberine Hoşgeldiniz.

İşlemler;

1. Rehberi Göster

2. Kişi Sorgulama

3. Kişi Ekle

4. Kişi Sil 

5. Arama Sayisi

Çıkmak için 'q' ya basın.
***********************************""")

rehber = Rehber()

while True:
    işlem = input("Yapacağınız İşlem:")
    if (işlem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (işlem == "1"):
        rehber.show_rehber()

    elif (işlem == "2"):
        isim = input("Hangi kişiyi görmek istiyorsunuz? ")
        print("Kişi sorgulanıyor...")
        rehber.search_person(isim)

    elif (işlem == "3"):
        isim = input("İsim:")
        soyisim = input("Soyisim:")
        telefon_numarasi = input("Telefon Numarası:")
        yas = int(input("Yaş:"))
        arama_sayisi = 0 # yeni kayıt olması nedeniyle 0 olarak girildi 

        yeni_kisi = rehber_kaydi(isim, soyisim, telefon_numarasi, yas, arama_sayisi)

        print("Kisi ekleniyor....")
        

        rehber.kisi_ekle(yeni_kisi)
        print("Kisi Eklendi....")


    elif (işlem == "4"):
        isim = input("Hangi kisiyi silmek istiyorsunuz ?")

        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Kisi Siliniyor...")

            rehber.kisi_sil(isim)
            print("Kisi silindi....")


    elif (işlem == "5"):
        isim = input("Kimi aramak istiyorsunuz?")
        rehber.arama_sayisi_artma(isim)
    else:
        print("Geçersiz İşlem...")
     

