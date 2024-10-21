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
        """Book a seat for the specific date if available."""
        if self.foglalas_datum in self.jarat.helyek_per_datum:
            if self.jarat.helyek_per_datum[self.foglalas_datum]['szabad_helyek'] > 0:
                self.jarat.helyek_per_datum[self.foglalas_datum]['foglalt_helyek'] += 1
                self.jarat.helyek_per_datum[self.foglalas_datum]['szabad_helyek'] -= 1
            else:
                raise ValueError("Nincs szabad hely a kiválasztott dátumon!")
        else:
            raise ValueError("Érvénytelen dátum!")

    def __str__(self):
        return f"Foglalás szám: {self.foglalas_szam} - {self.utas_nev} - {self.jarat.jaratszam} - {self.foglalas_datum.strftime('%Y-%b-%d-%H:%M')}"

    def foglalas_ara(self):
        return self.jarat.jegyar