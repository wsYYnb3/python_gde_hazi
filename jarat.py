from abc import ABC, abstractmethod
from datetime import datetime

class Jarat(ABC):
    def __init__(self, jaratszam,kiindulas, celallomas, jegyar, elerheto_datumok, jarat_ido, szabad_helyek,  menetido):
        self.jaratszam = jaratszam
        self.kiindulas = kiindulas
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.elerheto_datumok = elerheto_datumok
        self.jarat_ido = jarat_ido  
        self.foglalt_helyek = 0 
        self.szabad_helyek = szabad_helyek 
        self.menetido = menetido
    @abstractmethod
    def jarat_tipus(self):
        pass


class BelfoldiJarat(Jarat):
    def jarat_tipus(self):
        return "Belföldi"

    def __str__(self):
        return (f"Belföldi Járat - {self.jaratszam} - {self.kiindulas} - {self.celallomas} - {self.jegyar} Ft - "
                f"Járat ideje: {self.jarat_ido.strftime('%Y-%m-%d %H:%M')} - "
                f"Menetidő: {self.menetido} perc - "
                f"Foglalt helyek: {self.foglalt_helyek} - Szabad helyek: {self.szabad_helyek}")


class NemzetkoziJarat(Jarat):
    def jarat_tipus(self):
        return "Nemzetközi"

    def __str__(self):
        return (f"Nemzetközi Járat - {self.jaratszam} - {self.kiindulas} - {self.celallomas} - {self.jegyar} Ft - "
                f"Járat ideje: {self.jarat_ido.strftime('%Y-%m-%d %H:%M')} - "
                f"Menetidő: {self.menetido} perc - "
                f"Foglalt helyek: {self.foglalt_helyek} - Szabad helyek: {self.szabad_helyek}")
