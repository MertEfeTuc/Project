import personel
import doktor
import hemsire
import hasta
import pandas as pd
import tkinter as tk
from tkinter import ttk

yeniPersonel1 = personel.Personel(10,"Ahmet","Cetin","morg",5000)
yeniPersonel2 = personel.Personel(11,"Sercan","Cosar","Acil",25000)


doktor1 = doktor.doktor(1, "Emre", "Albayrak", "Kardiyoloji", 100000, "kardiyolog", 10, "Şehir Hastanesi")
doktor2 = doktor.doktor(2, "Ozan", "Kayalar", "Cerrahi", 200000, "Beyin Cerrahı", 25, "Şehir Hastanesi")
doktor3 = doktor.doktor(3, "Mutlu", "Yaşasın", "Cerrahi", 150000, "Plastik Cerrahı", 5, "Köy Hastanesi")


hemsire1 = hemsire.hemsire(21,"Özeralp","Gökçen","Cerrahi",30000,200,"a","Şehir Hastanesi")
hemsire2 = hemsire.hemsire(22,"Ali","Veli","Kardiyoloji",35000,220,"b","Şehir Hastanesi")
hemsire3 = hemsire.hemsire(21,"Berkay","Turu","Cerrahi",25000,240,"a","Köy Hastanesi")


hasta1 = hasta.hasta(111,"Mert","Tuç","18.08.2005","Soğuk algınlığı","ilaç")
hasta2 = hasta.hasta(112,"Necati","Efe","03.11.1998","Kırık","Alçı")
hasta3 = hasta.hasta(113,"Ayşe","Işıl","24.01.2010","Ateş","Dinlenme")


personel_list = [yeniPersonel1, yeniPersonel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3]
hasta_list = [hasta1, hasta2, hasta3]

personel_data = {
    'personel_no': [p.no_get() for p in personel_list],
    'ad': [p.ad_get() for p in personel_list],
    'soyad': [p.soyad_get() for p in personel_list],
    'departman': [p.dep_get() for p in personel_list],
    'maas': [p.maas_get() for p in personel_list],
    'uzmanlik': [getattr(p, 'uzmanlik_get', lambda: None)() for p in personel_list],
    'deneyim_yili': [getattr(p, 'deneyim_get', lambda: None)() for p in personel_list],
    'hastane': [getattr(p, 'hastane_get', lambda: None)() for p in personel_list],
    'calisma_saati': [getattr(p, 'saat_get', lambda: None)() for p in personel_list],
    'sertifika': [getattr(p, 'sertifika_get', lambda: None)() for p in personel_list],
    'hasta_no': [0] * len(personel_list),
    'dogum_tarihi': [0] * len(personel_list),
    'hastalik': [0] * len(personel_list),
    'tedavi': [0] * len(personel_list)
}

hasta_data = {
    'personel_no': [0] * len(hasta_list),
    'ad': [h.ad_get() for h in hasta_list],
    'soyad': [h.soyad_get() for h in hasta_list],
    'departman': [0] * len(hasta_list),
    'maas': [0] * len(hasta_list),
    'uzmanlik': [0] * len(hasta_list),
    'deneyim_yili': [0] * len(hasta_list),
    'hastane': [0] * len(hasta_list),
    'calisma_saati': [0] * len(hasta_list),
    'sertifika': [0] * len(hasta_list),
    'hasta_no': [h.no_get() for h in hasta_list],
    'dogum_tarihi': [h.dog_get() for h in hasta_list],
    'hastalik': [h.hastalik_get() for h in hasta_list],
    'tedavi': [h.tedavi_get() for h in hasta_list]
}

personel_df = pd.DataFrame(personel_data)
hasta_df = pd.DataFrame(hasta_data)

# Boş olan değişken değerleri için 0 atama
personel_df.fillna(0, inplace=True)
personel_df = personel_df.infer_objects()

# Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama
doktor_gruplari = personel_df[personel_df['uzmanlik'] != 0].groupby('uzmanlik').size()
print("Doktor grupları:\n", doktor_gruplari)

# 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
deneyimli_doktorlar = personel_df[(personel_df['deneyim_yili'] > 5) & (personel_df['deneyim_yili'] != 0)]
print("5 yıldan fazla deneyime sahip doktor sayısı:", deneyimli_doktorlar.shape[0])

# Hasta adına göre DataFrame’i alfabetik olarak sıralama
sorted_hasta_df = hasta_df.sort_values(by='ad')
print("Alfabetik sıraya göre hastalar:\n", sorted_hasta_df)

# Maaşı 7000 TL üzerinde olan personelleri bulma
maasi_yuksek_personeller = personel_df[personel_df['maas'] > 7000]
print("Maaşı 7000 TL üzerinde olan personeller:\n", maasi_yuksek_personeller)

# Doğum tarihi 1990 ve sonrası olan hastaları gösterme
dogum_tarihi_1990_sonrasi = hasta_df[pd.to_datetime(hasta_df['dogum_tarihi'], format='%d.%m.%Y') >= '1990-01-01']
print("Doğum tarihi 1990 ve sonrası olan hastalar:\n", dogum_tarihi_1990_sonrasi)


# Yeni DataFrame oluşturma
yeni_df = pd.concat([personel_df, hasta_df], ignore_index=True)

print("Yeni DataFrame:\n", yeni_df)

yeni_df_filtrelenmis = yeni_df[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']]
print("Yeni DataFrame (filtrelenmiş):\n", yeni_df_filtrelenmis)


root = tk.Tk()
root.title("Veri Görselleştirme")


# DataFrame'i gösterecek olan Treeview bileşeni
tree = ttk.Treeview(root)
tree["columns"] = tuple(yeni_df_filtrelenmis.columns)
tree["show"] = "headings"

# Sütun başlıklarını ayarla
for column in yeni_df_filtrelenmis.columns:
    tree.heading(column, text=column)

# Verileri eklemek için tree'e döngü yapısı
for index, row in yeni_df_filtrelenmis.iterrows():
    tree.insert("", "end", values=tuple(row))

# Scrollbar ekleyerek tree'i yerleştir
tree_scroll = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scroll.set)
tree_scroll.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

root.mainloop()