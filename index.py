print("Müberra'nın Kütüphanesine Hoş Geldiniz.")
KullaniciAdi = "Müberra"
Sifre = "1234"
gAdi = input("Kullanıcı Adınızı Giriniz: ")
gSifre = input("Şifrenizi Giriniz: ")

dosya = open("final.txt", "w")
dosya.write("Furuğ Ferruhzad -- İnanalım Soğuk Mevsimin Başlangıcına -- 2018 -- Dünya Şiiri\nFuruğ Ferruhzad -- Bir Başka Doğuş -- 2016 -- Dünya Şiiri\nCem Say -- 50 Soruda Yapay Zeka -- 2018 -- Popüler Bilim\nEmine Naskali -- Cumhuriyet Tarihi Soyadı Hikayeleri -- 2013 -- Cumhuriyet Tarihi\nOrhan Pamuk -- Masumiyet Müzesi -- 2013 -- Türkiye Roman\n")
dosya.close()

#dosya = open("final.txt", "r")
#print(dosya.read())
#dosya.close()

if gAdi == KullaniciAdi and gSifre == Sifre:
    print("Hoş Geldiniz")


    x = input("Yazar Adında Arama Yapmak İçin E Tuşuna Basınız →→→\n"
                "Kitap Adında Arama Yapmak İçin R Tuşuna Basınız →→→\n"
                "Tarih Bilgisine Göre Arama Yapmak İçin T Tuşuna Basınız →→→\n"
                "Konu Adında Arama Yapmak İçin Y Tuşuna Basınız →→→\n")
    if x == "E":
        kullanici = input("Bulmak İstediğiniz Eserin Yazar Adını Yazınız: ").casefold() #yazar adı
        if kullanici == "Furuğ Ferruhzad".casefold():
            print("Furuğ Ferruhzad -- İnanalım Soğuk Mevsimin Başlangıcına -- 2018 -- Dünya Şiiri\nFuruğ Ferruhzad -- Bir Başka Doğuş -- 2016 -- Dünya Şiiri")
        elif kullanici == "Cem Say".casefold():
            print("Cem Say -- 50 Soruda Yapay Zeka -- 2018 -- Popüler Bilim")
        elif kullanici == "Emine Naskali".casefold():
            print("Emine Naskali -- Cumhuriyet Tarihi Soyadı Hikayeleri -- 2013 -- Cumhuriyet Tarihi")
        elif kullanici == "Orhan Pamuk".casefold():
            print("Orhan Pamuk -- Masumiyet Müzesi -- 2013 -- Türkiye Roman")
        else:
            print("Yazar Adı Kataloğumuzda Bulunmamaktadır...")
    if x == "R":
        kullanici = input("Bulmak İstediğiniz Eserin Adını Yazınız: ").casefold() #kitap adı
        if kullanici == "İnanalım Soğuk Mevsimin Başlangıcına".casefold():
            print("Furuğ Ferruhzad -- İnanalım Soğuk Mevsimin Başlangıcına -- 2018 -- Dünya Şiiri")
        elif kullanici =="Bir Başka Doğuş".casefold():
            print("Furuğ Ferruhzad -- Bir Başka Doğuş -- 2016 -- Dünya Şiiri")
        elif kullanici == "50 Soruda Yapay Zeka".casefold():
            print("Cem Say -- 50 Soruda Yapay Zeka -- 2018 -- Popüler Bilim")
        elif kullanici == "Cumhuriyet Tarihi Soyadı Hikayeleri".casefold():
            print("Emine Naskali -- Cumhuriyet Tarihi Soyadı Hikayeleri -- 2013 -- Cumhuriyet Tarihi")
        elif kullanici == "Masumiyet Müzesi".casefold():
            print("Orhan Pamuk -- Masumiyet Müzesi -- 2013 -- Türkiye Roman")
        else:
            print("Kitap Adı Kataloğumuzda Bulunmamaktadır...")
    if x == "T":
        kullanici = input("Bulmak İstediğiniz Eserin Tarihini Yazınız: ") #tarih
        if kullanici == "2013":
            print("Emine Naskali -- Cumhuriyet Tarihi Soyadı Hikayeleri -- 2013 -- Cumhuriyet Tarihi\nOrhan Pamuk -- Masumiyet Müzesi -- 2013 -- Türkiye Roman")
        elif kullanici == "2016":
            print("Furuğ Ferruhzad -- Bir Başka Doğuş -- 2016 -- Dünya Şiiri")
        elif kullanici == "2018":
            print("Furuğ Ferruhzad -- İnanalım Soğuk Mevsimin Başlangıcına -- 2018 -- Dünya Şiiri\nCem Say -- 50 Soruda Yapay Zeka -- 2018 -- Popüler Bilim")
        else:
            print("Belirttiğiniz Tarihle İlişkili Kataloğumuzda Kaynak Bulunmamaktadır...")
    if x == "Y":
        kullanici = input("Bulmak İstediğiniz Eserin Konusunu Yazınız: ").casefold() #konu
        if kullanici =="Dünya Şiiri".casefold():
            print("Furuğ Ferruhzad -- İnanalım Soğuk Mevsimin Başlangıcına -- 2018 -- Dünya Şiiri\nFuruğ Ferruhzad -- Bir Başka Doğuş -- 2016 -- Dünya Şiiri")
        elif kullanici == "Popüler Bilim".casefold():
            print("Cem Say -- 50 Soruda Yapay Zeka -- 2018 -- Popüler Bilim")
        elif kullanici == "Cumhuriyet Tarihi".casefold():
            print("Emine Naskali -- Cumhuriyet Tarihi Soyadı Hikayeleri -- 2013 -- Cumhuriyet Tarihi")
        elif kullanici == "Türkiye Roman".casefold():
            print("Orhan Pamuk -- Masumiyet Müzesi -- 2013 -- Türkiye Roman")
        else:
            print("Belirtiğiniz Konuyla İligili Kataloğumuzda Kaynak Bulunmamaktadır...")


    kullanici = input("Yeni Eser Eklemek İster Misiniz?")
    if kullanici == "Yes":
        Yazar = input("Yazar: ")
        KitapAdi = input("Kitap Adı: ")
        Tarih = input("Tarih: ")
        Yayinevi = input("Yayınevi: ")
        dosya = open("final.txt", "a")

        dosya.write(Yazar + " -- ")
        dosya.write(KitapAdi + " -- ")
        dosya.write(Tarih + " -- ")
        dosya.write(Yayinevi + " ")
        dosya.close()
    elif kullanici == "No":
        print("Programdan Çıkış Yapabilirsiniz.")
else:
    print("Kullanıcı Adınızı veya Şifrenizi Yanlış Girdiniz.\nLütfen Tekrardan Deneyiniz...")





