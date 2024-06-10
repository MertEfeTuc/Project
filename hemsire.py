import personel


class hemsire(personel.Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str},{self.__calisma_saati},{self.__sertifika},{self.__hastane}"

    # Getter methods
    def saat_get(self):
        return self.__calisma_saati

    def sertifika_get(self):
        return self.__sertifika

    def hastane_get(self):
        return self.__hastane

    # Setter methods
    def saat_set(self, cs):
        self.__calisma_saati = cs

    def sertifika_set(self, ss):
        self.__sertifika = ss

    def hastane_set(self, ha):
        self.__hastane = ha

    # Method for raises in maas value
    def maas_arttir(self, value):
        current_maas = self.maas_get()
        new_maas = current_maas * value
        self.maas_set(new_maas)