


class hasta:
    def __init__(self,hasta_no,ad,soyad,dogum_tarihi,hastalik,tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = doğum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi
    def __str__(self):
        return f"{self.__hasta_no},{self.__ad},{self.__soyad},{self.__dogum_tarihi},{self.__hastalik},{self.__tedavi}"

    def no_set(self,no):
        self.__hasta_no = no
    def ad_set(self,ad):
        self.__ad = ad
    def soyad_set(self,soyad):
        self.__soyad = soyad
    def dog_set(self,dt):
        self.__dogum_tarihi = dt
    def hastalik_set(self,has):
        self.__hastalik = has
    def tedavi_set(self,no):
        self.__tedavi = no

    def no_get(self):
        return self.__hasta_no
    def ad_get(self):
        return self.__ad
    def soyad_get(self):
        return self.__soyad
    def dog_get(self):
        return self.__dogum_tarihi
    def hastalik_get(self):
        return self.__hastalik
    def tedavi_get(self):
        return self.__tedavi

