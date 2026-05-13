import tkinter as tk


def hesapla():
    try:
        sonuc = eval(giris.get())
        sonuc_yazisi.config(text=f"Sonuç: {sonuc}")
    except:
        sonuc_yazisi.config(text="Hatalı işlem!")


pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("350x250")

baslik = tk.Label(pencere, text="Hesap Makinesi", font=("Arial", 20))
baslik.pack(pady=15)

giris = tk.Entry(pencere, width=30, font=("Arial", 14))
giris.pack(pady=10)

buton = tk.Button(pencere, text="Hesapla", command=hesapla)
buton.pack(pady=10)

sonuc_yazisi = tk.Label(pencere, text="Sonuç:", font=("Arial", 14))
sonuc_yazisi.pack(pady=10)

pencere.mainloop()
