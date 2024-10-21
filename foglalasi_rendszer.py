from jarat import BelfoldiJarat, NemzetkoziJarat
from legi_tarsasag import LegiTarsasag
from jegy_foglalas import JegyFoglalas
from datetime import datetime

class FoglalasiRendszer:
    def __init__(self):
        self.legi_tarsasag = LegiTarsasag("Python Air")
        self.foglalasok = []
        self.rendszer_inditasa()

    def rendszer_inditasa(self):
        jarat1 = BelfoldiJarat("PA101", "Budapest", "Eger", 5000, [datetime(2024, 12, 1)], datetime(2024, 12, 1, 14, 0), 100, 20)  
        jarat2 = BelfoldiJarat("PA102", "Budapest","Debrecen", 2000, [datetime(2024, 12, 2)], datetime(2024, 12, 2, 10, 0), 80, 20)  
        jarat3 = NemzetkoziJarat("PA201","Budapest", "London", 25000, [datetime(2024, 12, 3)], datetime(2024, 12, 3, 16, 0), 150, 180) 
        self.legi_tarsasag.jarat_hozzaadasa(jarat1)
        self.legi_tarsasag.jarat_hozzaadasa(jarat2)
        self.legi_tarsasag.jarat_hozzaadasa(jarat3)

        self.foglalasok.append(JegyFoglalas("Nagy Anna", jarat1, datetime(2024, 12, 1)))
        self.foglalasok.append(JegyFoglalas("Kiss Béla", jarat2, datetime(2024, 12, 2)))
        self.foglalasok.append(JegyFoglalas("Szabó Csaba", jarat3, datetime(2024, 12, 3)))
        self.foglalasok.append(JegyFoglalas("Tóth Dóra", jarat1, datetime(2024, 12, 5)))
        self.foglalasok.append(JegyFoglalas("Horváth Erik", jarat2, datetime(2024, 12, 6)))
        self.foglalasok.append(JegyFoglalas("Varga Fanni", jarat3, datetime(2024, 12, 7)))

    def foglalas_letrehozasa(self):
        utas_nev = input("Adja meg az utas nevét: ")
        print("Elérhető járatok:")
        self.legi_tarsasag.jaratok_listazasa()

        jaratszam = input("Adja meg a foglalni kívánt járat számát: ")
        jarat = next((j for j in self.legi_tarsasag.jaratok if j.jaratszam == jaratszam), None)
        if not jarat:
            print("Nincs ilyen járat!")
            return

        print("Elérhető dátumok a kiválasztott járaton:")
        for i, datum in enumerate(jarat.elerheto_datumok):
            print(f"{i + 1}. {datum.strftime('%Y-%m-%d')}")

        datum_index = input("Válassza ki a dátum sorszámát: ")
        try:
            datum_index = int(datum_index) - 1
            foglalas_datum = jarat.elerheto_datumok[datum_index]
            if foglalas_datum < datetime.now():
                print("Nem lehet múltbeli dátumra foglalni!")
                return
        except (ValueError, IndexError):
            print("Hibás dátum kiválasztás!")
            return

        try:
            foglalas = JegyFoglalas(utas_nev, jarat, foglalas_datum)
            self.foglalasok.append(foglalas)
            print(f"Foglalás sikeres! Ára: {foglalas.foglalas_ara()} Ft")
            print(f"Foglalás száma: {foglalas.foglalas_szam}")
        except ValueError as e:
            print(e)

    def foglalas_torlese(self):
        if not self.foglalasok:
            print("Nincs törölhető foglalás!")
            return

        print("Elérhető foglalások:")
        for foglalas in self.foglalasok:
            print(f"{foglalas.foglalas_szam}. {foglalas}")

        valasztott_szam = input("Adja meg a törlendő foglalás számát: ")
        try:
            valasztott_szam = int(valasztott_szam)
            torolt_foglalas = next((f for f in self.foglalasok if f.foglalas_szam == valasztott_szam), None)
            
            if torolt_foglalas:
          
                torolt_foglalas.jarat.foglalt_helyek -= 1
                torolt_foglalas.jarat.szabad_helyek += 1

                self.foglalasok.remove(torolt_foglalas)
                print(f"{torolt_foglalas.foglalas_szam} számú foglalás törölve! Foglalt helyek frissítve.")
            else:
                print("Nincs ilyen foglalás!")
        except ValueError:
            print("Hibás foglalás szám formátum!")


    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincs megjeleníthető foglalás!")
            return
        for foglalas in self.foglalasok:
            print(foglalas)

    def menu(self):
        while True:
            print("\n--- Repülőjegy Foglalási Rendszer ---")
            print("1. Jegy foglalása")
            print("2. Foglalás lemondása")
            print("3. Foglalások listázása")
            print("4. Kilépés")
            valasztas = input("Válasszon egy opciót: ")
            if valasztas == "1":
                self.foglalas_letrehozasa()
            elif valasztas == "2":
                self.foglalas_torlese()
            elif valasztas == "3":
                self.foglalasok_listazasa()
            elif valasztas == "4":
                print("Köszönjük, hogy használta a rendszert!")
                break
            else:
                print("Érvénytelen választás! Próbálja újra.")
