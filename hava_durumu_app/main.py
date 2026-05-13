import tkinter as tk
import requests


def hava_goster():
    sehir = giris.get()

    if sehir == "":
        sonuc.config(text="Lütfen şehir adı gir.")
        return

    try:
        url = f"https://wttr.in/{sehir}?format=3"
        cevap = requests.get(url)

        if cevap.status_code == 200:
            sonuc.config(text=cevap.text)
        else:
            sonuc.config(text="Hava durumu alınamadı.")

    except:
        sonuc.config(text="İnternet bağlantısı hatası.")


pencere = tk.Tk()
pencere.title("Hava Durumu Uygulaması")
pencere.geometry("450x250")

baslik = tk.Label(pencere, text="Hava Durumu", font=("Arial", 22))
baslik.pack(pady=15)

giris = tk.Entry(pencere, width=30, font=("Arial", 14))
giris.pack(pady=10)

buton = tk.Button(pencere, text="Hava Durumunu Göster", command=hava_goster)
buton.pack(pady=10)

sonuc = tk.Label(pencere, text="Şehir adı giriniz", font=("Arial", 14))
sonuc.pack(pady=15)

pencere.mainloop()