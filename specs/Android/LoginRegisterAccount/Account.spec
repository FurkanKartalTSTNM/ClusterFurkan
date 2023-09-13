Specification Heading
=====================
Created by testinium on 8.06.2023

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Deleting Address and Adding New Address
------------------
tags:Gratis_Android_YeniAdresEklemeVeSilme
* Uygulama baslatilir.
* Login sayfasina gecilir.
* Login olunur.
* Profil'e tiklanir profilim sayfasinin acildigi gorulur.
* Adreslerim'e tiklanir adreslerim sayfasinin acildigi gorulur.
* Adres varsa Silme'ye tıklanır, adres silme pop-up'ın açıldığı görülür ve adres silinir.
* Yeni Adres Ekle'ye tiklanir adres ekleme sayfasinin acildigi gorulur.
//* Android klavye kapatılır
* Adres icin Ad, Soyad, Telefon ve Adres Ismi bilgileri girilir.
* Adres Ekle Sehir ismi secilir.
* Adres Ekle Ilce ismi secilir.
* Adres Ekle Mahalle ismi secilir.
* Adres Ekleme icin Adres Detay ve Posta Kodu bilgileri girilir.
* Kaydet ikonuna tiklanir eklenen adresin adreslerim alanina geldigi gorulur.

Updating Address
----------------
tags:Gratis_Android_AdresGuncelleme
* Uygulama baslatilir.
* Login sayfasina gecilir.
* Login olunur.
* Profil'e tiklanir profilim sayfasinin acildigi gorulur.
* Adreslerim'e tiklanir adreslerim sayfasinin acildigi gorulur.
* Adres güncellemeye tıklanır.
* Adres icin Ad, Soyad, Telefon ve Adres Ismi bilgileri girilir.
* Adres Ekle Sehir ismi secilir.
* Adres Ekle Ilce ismi secilir.
* Adres Ekle Mahalle ismi secilir.
* Adres Ekleme icin Adres Detay ve Posta Kodu bilgileri girilir.
* Kaydet ikonuna tiklanir eklenen adresin adreslerim alanina geldigi gorulur.

Favorite List Name Update
--------------------
tags:Gratis_Android_FavoriAdiListeDuzenleme
* Uygulama baslatilir.
* Login sayfasina gecilir.
* Login olunur.
* Profil'e tiklanir profilim sayfasinin acildigi gorulur.
* Profil sayfasındaki Favori butonuna tiklanir.
* Favori sayfasindaki Liste Adini Duzenle butonuna tiklanir ve yeni isim girilir.

Adding A Product To Favorite List
---------------------------------
tags:Gratis_Android_FavorilereUrunEklemeVeCikarma
* Uygulama baslatilir.
* Login sayfasina gecilir.
* Login olunur.
* En Cok Satanlar alanindan bir urunun favori butonuna tıklanir.
* Urun favorilere eklenir.
* Ana sayfadaki urun favorilerden cikarilir.

Add Select and Delete Favorite List
------------------------------------
tags:Gratis_Android_ListeOlusturmaSecmeVeSilme
* Uygulama baslatilir.
* Login sayfasina gecilir.
* Login olunur.
* En Cok Satanlar alanindan bir urunun favori butonuna tıklanir.
* Yeni favori listesi olusturulur ve secilen urun favori eklenir.
* Profil'e tiklanir profilim sayfasinin acildigi gorulur.
* Profil sayfasındaki Favori butonuna tiklanir.
* Listeden yeni eklenen favori listesi secilir.
* Favori listesi silinir.

Add To Cart From Favorite List
------------------------------
tags:Gratis_Android_FavoriListesindenSepeteEkleme
* Ana sayfa sepet ikonuna tiklanir.
* Sepet ikonu ile login olunur.
* Sepet kontrol edilerek temizlenir.
* Ana sayfa tab'ına tıklanır.
* En Cok Satanlar alanindan bir urunun favori butonuna tıklanir.
* Urun favorilere eklenir.
* Profil'e tiklanir profilim sayfasinin acildigi gorulur.
* Profil sayfasındaki Favori butonuna tiklanir.
* Favorilerden urun detay sayfasına gecilir.
* Favorilerdeki urun sepete eklenir ve alısverise devam edilir.
* Favorilerdeki urun sepete eklenir ve sepete gidilir.
* Sepet kasa arkasi popup'i varsa kapatilir.
* Urunlerin sepete eklendigi kontrol edilir.
* Favori listesi kontrol edilerek temizlenir.

From Favorite List to Home Page
-------------------------------
tags:Gratis_Android_FavorilerdenAnasayfayaYonlendirme
* Uygulama baslatilir.
* Login sayfasina gecilir.
* Login olunur.
* Profil'e tiklanir profilim sayfasinin acildigi gorulur.
* Favori listesi kontrol edilerek temizlenir.
* Favori listesinden ana sayfaya yonlendirme yapilir.

Max Add To Cart in Favorites
----------------------------
tags:Gratis_Android_FavorilerdeMaximumSepeteEkleme
* Uygulama baslatilir.
* Ana sayfa sepet ikonuna tiklanir.
* Sepet ikonu ile login olunur.
* Bir ürün için sepet kontrol edilerek temizlenir.
* Kategoriler sayfasina gecilir.
* "Makyaj" isimli kategori seçilir.
* Alt kategorilerden biri "Dudak Makyajı", "Ruj" seçilir.
* Listeleme alanından bir ürünün favori butonuna tıklanır.
* Urun favorilere eklenir.
* Profil'e tiklanir profilim sayfasinin acildigi gorulur.
* Profil sayfasındaki Favori butonuna tiklanir.
* Favorilerdeki urun sepete eklenir ve alısverise devam edilir.
* Favorilerdeki urun sepete eklenir ve alısverise devam edilir.
* Favorilerdeki urun sepete eklenir ve alısverise devam edilir.
* Favorilerdeki urun sepete eklenir ve alısverise devam edilir.
* Favorilerdeki ürünün sepete ekleme butonuna tıklanır.
* toast message "Sepete bu üründen maksimum 4 adet ekleyebilirsiniz." değerine eşit mi

Scenario Updating Customer Information
------------------------------------------
tags:Gratis_Android_UyeBilgileriGuncelleme
* Uygulama baslatilir.
* Login sayfasina gecilir.
* Login olunur.
* Profil'e tiklanir profilim sayfasinin acildigi gorulur.
* Uye bilgilerim sayfasina gecilir.
* Uye bilgileri basarili sekilde guncellenir.
* Uye bilgileri guncellendiği kontrol edilir.