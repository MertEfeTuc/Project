import personel

class doktor(personel.Personel):
    def __init__(self,personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str},{self.__uzmanlik},{self.__deneyim_yili},{self.__hastane}"
    #Getter methods
    def uzmanlik_get(self):
        return self.__uzmanlik
    def deneyim_get(self):
        return self.__deneyim_yili
    def hastane_get(self):
        return self.__hastane

    # Setter methods
    def uzmanlik_set(self,uz):
        self.__uzmanlik =  uz
    def deneyim_set(self,de):
        self.__deneyim_yili = de
    def hastane_set(self,ha):
        self.__hastane = ha

    # Method for raises in maas value
    def maas_arttir(self, value):
        current_maas = self.maas_get()
        new_maas = current_maas * value
        self.maas_set(new_maas)
