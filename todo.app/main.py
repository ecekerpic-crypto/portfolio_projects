import tkinter as tk


def gorev_ekle():
    gorev = giris.get()

    if gorev != "":
        liste.insert(tk.END, gorev)
        giris.delete(0, tk.END)


def gorev_sil():
    secilen = liste.curselection()

    if secilen:
        liste.delete(secilen)


pencere = tk.Tk()
pencere.title("Todo App")
pencere.geometry("400x400")

baslik = tk.Label(pencere, text="Todo App", font=("Arial", 20))
baslik.pack(pady=10)

giris = tk.Entry(pencere, width=35)
giris.pack(pady=10)

ekle_buton = tk.Button(pencere, text="Görev Ekle", command=gorev_ekle)
ekle_buton.pack(pady=5)

liste = tk.Listbox(pencere, width=45, height=12)
liste.pack(pady=10)

sil_buton = tk.Button(pencere, text="Seçili Görevi Sil", command=gorev_sil)
sil_buton.pack(pady=5)

pencere.mainloop()