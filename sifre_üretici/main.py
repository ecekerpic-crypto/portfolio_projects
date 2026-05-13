import random
import string

# Şifre uzunluğu
uzunluk = 12

# Kullanılacak karakterler
karakterler = string.ascii_letters + string.digits + string.punctuation

# Şifre oluştur
sifre = "".join(random.choice(karakterler) for i in range(uzunluk))

print("Oluşturulan şifre:", sifre)