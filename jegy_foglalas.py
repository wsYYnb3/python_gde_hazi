class JegyFoglalas:
    foglalas_counter = 1  

    def __init__(self, utas_nev, jarat, foglalas_datum):
        self.foglalas_szam = JegyFoglalas.foglalas_counter 
        JegyFoglalas.foglalas_counter += 1
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.foglalas_datum = foglalas_datum

   
        self.jegyFoglalas()

    def jegyFoglalas(self):
        """Foglaljon jegyet."""
        if self.jarat.szabad_helyek > 0:
            self.jarat.foglalt_helyek += 1
            self.jarat.szabad_helyek -= 1
        else:
            raise ValueError("Nincs szabad hely a járaton!")

    def __str__(self):
        return f"Foglalás szám: {self.foglalas_szam} - {self.utas_nev} - {self.jarat.jaratszam} - {self.foglalas_datum.strftime('%Y-%m-%d')}"

    def foglalas_ara(self):
        return self.jarat.jegyar