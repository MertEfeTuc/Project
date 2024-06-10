
class Personel:
    def __init__(self ,personel_no ,ad ,soyad ,departman ,maas):
        self.__personal_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas
    # STR method
    def __str__(self):
        return f"{self.__personal_no},{self.__ad},{self.__soyad},{self.__departman},{self.__maas}"

    # Setter methods
    def no_set(self ,no):
        self.__personal_no = no
    def ad_set(self ,ad):
        self.__ad = ad
    def soyad_set(self ,soyad):
        self.__soyad = soyad
    def dep_set(self ,depart):
        self.__departman = depart
    def maas_set(self ,maas):
        self.__maas = maas

    # Getter methods
    def no_get(self):
        return self.__personal_no
    def ad_get(self):
        return self.__ad
    def soyad_get(self):
        return self.__soyad
    def dep_get(self):
        return self.__departman
    def maas_get(self):
        return self.__maas








