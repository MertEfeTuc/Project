import personel


class hemsire(personel.Personel):
    def __init__(self, calisma_saati, sertifika, hastane):
        super().__init__(personel.personel_no, personel.ad, personel.soyad, personel.departman, personel.maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def __str__(self):
        return f"{self.__calisma_saati},{self.__sertifika},{self.__hastane}"

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
    def maas_attir(self, value):
        self.__maas *= value