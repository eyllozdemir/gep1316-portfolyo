
# Tarih modülünden datetime sınıfını içe aktarıyoruz.
from datetime import datetime

# Kullanıcıdan adını girmesini istiyoruz.
ad = input("Merhaba! Adınız nedir? ")

# Kullanıcıdan doğum yılını alıp tam sayıya dönüştürüyoruz.
dogum_yili = int(input("Doğum yılınız nedir? "))

# Bilgisayarın tarihinden güncel yılı öğreniyoruz.
guncel_yil = datetime.now().year

# Güncel yıldan doğum yılını çıkararak yaklaşık yaşı hesaplıyoruz.
yas = guncel_yil - dogum_yili

# Kullanıcıya kişisel bir karşılama mesajı gösteriyoruz.
print(f"Merhaba {ad}! Hoş geldiniz.")
print(f"Doğum yılınıza göre bu yıl {yas} yaşına giriyorsunuz.")
