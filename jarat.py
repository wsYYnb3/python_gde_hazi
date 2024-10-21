from abc import ABC, abstractmethod
from datetime import datetime

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar, elerheto_datumok, jarat_ido, szabad_helyek):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.elerheto_datumok = elerheto_datumok
        self.jarat_ido = jarat_ido  
        self.foglalt_helyek = 0 
        self.szabad_helyek = szabad_helyek 

    @abstractmethod
    def jarat_tipus(self):
        pass


class BelfoldiJarat(Jarat):
    def jarat_tipus(self):
        return "Belföldi"

    def __str__(self):
        return (f"Belföldi Járat - {self.jaratszam} - {self.celallomas} - {self.jegyar} Ft - "
                f"Járat ideje: {self.jarat_ido.strftime('%Y-%m-%d %H:%M')} - "
                f"Foglalt helyek: {self.foglalt_helyek} - Szabad helyek: {self.szabad_helyek}")


class NemzetkoziJarat(Jarat):
    def jarat_tipus(self):
        return "Nemzetközi"

    def __str__(self):
        return (f"Nemzetközi Járat - {self.jaratszam} - {self.celallomas} - {self.jegyar} Ft - "
                f"Járat ideje: {self.jarat_ido.strftime('%Y-%m-%d %H:%M')} - "
                f"Foglalt helyek: {self.foglalt_helyek} - Szabad helyek: {self.szabad_helyek}")
