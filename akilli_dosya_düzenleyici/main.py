import os
import shutil

# Düzenlenecek klasör yolu
klasor = r"C:\Users\eceke\OneDrive\Desktop\portfolio_projects"

# Dosya türleri
dosya_turleri = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mov"],
    "Documents": [".pdf", ".txt", ".docx"]
}

# Klasördeki dosyaları kontrol et
for dosya in os.listdir(klasor):

    dosya_yolu = os.path.join(klasor, dosya)

    # Dosya mı kontrol et
    if os.path.isfile(dosya_yolu):

        # Uzantıyı al
        uzanti = os.path.splitext(dosya)[1].lower()

        # Türleri kontrol et
        for klasor_adi, uzantilar in dosya_turleri.items():

            if uzanti in uzantilar:

                hedef_klasor = os.path.join(klasor, klasor_adi)

                # Klasör yoksa oluştur
                os.makedirs(hedef_klasor, exist_ok=True)

                # Dosyayı taşı
                shutil.move(dosya_yolu, os.path.join(hedef_klasor, dosya))

                print(f"{dosya} -> {klasor_adi} klasörüne taşındı")