# Tarih modülünden datetime sınıfını içe aktarıyoruz.
from datetime import datetime

# Kullanıcıdan adını girmesini istiyoruz.
ad = input("Merhaba! Adınız nedir? ")

# Kullanıcıdan doğum yılını alıp tam sayıya dönüştürüyoruz.
dogum_yili = int(input("Doğum yılınız nedir? "))

# Bilgisayarın tarihinden güncel yılı öğreniyoruz.
guncel_yil = datetime.now().year

# Doğum yılının gelecekte olup olmadığını kontrol ediyoruz.
if dogum_yili > guncel_yil:
    print("Hata: Doğum yılı gelecekte olamaz!")

# Doğum yılı geçerliyse yaş hesaplıyoruz.
else:
    yas = guncel_yil - dogum_yili

    # Kişiye özel karşılama mesajını gösteriyoruz.
    print(f"Merhaba {ad}! Hoş geldiniz.")

    # Kullanıcının bu yıl gireceği yaşı gösteriyoruz.
    print(f"Doğum yılınıza göre bu yıl {yas} yaşına giriyorsunuz.")

