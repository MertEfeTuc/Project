import personel

class doktor(personel.Personel):
    def __init__(self,personel,uzmanlik,deneyim_yili,hastane):
        super().__init__(personel.personel_no, personel.ad, personel.soyad, personel.departman, personel.maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane
    def uzmanlik_get(self):
        return self.__uzmanlik
    def deneyim_get(self):
        return self.__deneyim_yili
    def hastane_get(self):
        return self.__hastane
    def uzmanlik_set(self,uz):
        self.__uzmanlik =  uz
    def deneyim_set(self,de):
        self.__deneyim_yili = de
    def hastane_set(self,ha):
        self.__hastane = ha