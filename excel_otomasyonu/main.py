import openpyxl

dosya = "satislar.xlsx"

kitap = openpyxl.Workbook()
sayfa = kitap.active
sayfa.title = "Satışlar"

sayfa["A1"] = "Ürün"
sayfa["B1"] = "Adet"
sayfa["C1"] = "Birim Fiyat"
sayfa["D1"] = "Toplam"

veriler = [
    ["Kalem", 10, 15],
    ["Defter", 5, 40],
    ["Çanta", 2, 250],
    ["Silgi", 20, 5]
]

for satir in veriler:
    urun = satir[0]
    adet = satir[1]
    fiyat = satir[2]
    toplam = adet * fiyat

    sayfa.append([urun, adet, fiyat, toplam])

kitap.save(dosya)

print("Excel raporu oluşturuldu!")
toplam_gelir = 0

for satir in veriler:
    toplam_gelir += satir[1] * satir[2]

print("Toplam gelir:", toplam_gelir, "TL")