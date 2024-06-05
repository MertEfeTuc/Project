import personel
import doktor

yeniPersonel1 = personel.Personel(1,"Ahmet","Cetin","morg",20000)
yeniPersonel2 = personel.Personel(1,"Sercan","Cosar","Acil",25000)



doktor1 = doktor.doktor(1, "Mehmet", "Yilmaz", "Cardiology", 100000, "Cardiologist", 10, "City Hospital")
print(doktor1.ad_get())  # Output: Mehmet
print(doktor1.soyad_get())  # Output: Yilmaz
print(doktor1.dep_get())  # Output: Cardiology
print(doktor1.maas_get())  # Output: 100000

# Access subclass-specific attributes using getter methods
print(doktor1.uzmanlik_get())  # Output: Cardiologist
print(doktor1.deneyim_get())  # Output: 10
print(doktor1.hastane_get())  # Output: City Hospital

# Increase maas by 10%
doktor1.maas_attir(1.1)
print(doktor1.maas_get())  # Output: 110000