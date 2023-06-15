#1
class Pojazd:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.nr_tablica = ""

    def przypisz_nr_tablica(self, nr_tablica):
        self.nr_tablica = nr_tablica

    def wyswietl_informacje(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Numer tablicy rejestracyjnej: {self.nr_tablica}")

    def __del__(self):
        print(f"Obiekt {self.marka} {self.model} został usunięty z pamięci.")


class Samochod(Pojazd):
    def __init__(self, marka, model, ilosc_drzwi):
        super().__init__(marka, model)
        self.ilosc_drzwi = ilosc_drzwi

    def wyswietl_informacje(self):
        super().wyswietl_informacje()
        print(f"Ilość drzwi: {self.ilosc_drzwi}")


class Motocykl(Pojazd):
    def __init__(self, marka, model, pojemnosc_silnika):
        super().__init__(marka, model)
        self.pojemnosc_silnika = pojemnosc_silnika

    def wyswietl_informacje(self):
        super().wyswietl_informacje()
        print(f"Pojemność silnika: {self.pojemnosc_silnika} ccm")


samochod1 = Samochod("Toyota", "Corolla", 4)
samochod1.przypisz_nr_tablica("ABC123")
samochod1.wyswietl_informacje()

samochod2 = Samochod("Ford", "Focus", 5)
samochod2.przypisz_nr_tablica("XYZ789")
samochod2.wyswietl_informacje()

motocykl1 = Motocykl("Honda", "CBR600RR", 600)
motocykl1.przypisz_nr_tablica("DEF456")
motocykl1.wyswietl_informacje()

motocykl2 = Motocykl("Kawasaki", "Ninja 300", 300)
motocykl2.przypisz_nr_tablica("GHI789")
motocykl2.wyswietl_informacje()

#2
class Zwierzę:
    def __init__(self, gatunek, wiek):
        self.gatunek = gatunek
        self.wiek = wiek

    def daj_głos(self):
        pass

    def informacje(self):
        print(f"Gatunek: {self.gatunek}")
        print(f"Wiek: {self.wiek} lat")


class Kot(Zwierzę):
    def __init__(self, wiek, imię):
        super().__init__("Kot", wiek)
        self.imię = imię

    def daj_głos(self):
        print("Miau!")

    def informacje(self):
        super().informacje()
        print(f"Imię: {self.imię}")


class Pies(Zwierzę):
    def __init__(self, wiek, rasa):
        super().__init__("Pies", wiek)
        self.rasa = rasa

    def daj_głos(self):
        print("Hau hau!")

    def informacje(self):
        super().informacje()
        print(f"Rasa: {self.rasa}")


class Ptak(Zwierzę):
    def __init__(self, wiek, gatunek):
        super().__init__("Ptak", wiek)
        self.gatunek = gatunek

    def daj_głos(self):
        print("Cwir cwir!")

    def informacje(self):
        super().informacje()
        print(f"Gatunek: {self.gatunek}")


class Ryba(Zwierzę):
    def __init__(self, wiek, gatunek):
        super().__init__("Ryba", wiek)
        self.gatunek = gatunek

    def daj_głos(self):
        print("...")

    def informacje(self):
        super().informacje()
        print(f"Gatunek: {self.gatunek}")



kot1 = Kot(3, "Filemon")
kot1.informacje()
kot1.daj_głos()

pies1 = Pies(5, "Labrador")
pies1.informacje()
pies1.daj_głos()

ptak1 = Ptak(1, "Wróbel")
ptak1.informacje()
ptak1.daj_głos()

ryba1 = Ryba(2, "Karp")
ryba1.informacje()
ryba1.daj_głos()


#3
import math

class Figura:
    def oblicz_obwod(self):
        pass

    def oblicz_pole(self):
        pass


class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_obwod(self):
        return 4 * self.bok

    def oblicz_pole(self):
        return self.bok ** 2


class Prostokąt(Figura):
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b

    def oblicz_obwod(self):
        return 2 * (self.bok_a + self.bok_b)

    def oblicz_pole(self):
        return self.bok_a * self.bok_b


class Trójkąt(Figura):
    def __init__(self, podstawa, bok_a, bok_b, bok_c):
        self.podstawa = podstawa
        self.bok_a = bok_a
        self.bok_b = bok_b
        self.bok_c = bok_c

    def oblicz_obwod(self):
        return self.podstawa + self.bok_a + self.bok_b + self.bok_c

    def oblicz_pole(self):
        p = self.oblicz_obwod() / 2
        return math.sqrt(p * (p - self.podstawa) * (p - self.bok_a) * (p - self.bok_b) * (p - self.bok_c))


class Koło(Figura):
    def __init__(self, promień):
        self.promień = promień

    def oblicz_obwod(self):
        return 2 * math.pi * self.promień

    def oblicz_pole(self):
        return math.pi * self.promień ** 2


class Romb(Figura):
    def __init__(self, przekątna_a, przekątna_b):
        self.przekątna_a = przekątna_a
        self.przekątna_b = przekątna_b

    def oblicz_obwod(self):
        return 4 * math.sqrt((self.przekątna_a / 2) ** 2 + (self.przekątna_b / 2) ** 2)

    def oblicz_pole(self):
        return (self.przekątna_a * self.przekątna_b) / 2


class Trapez(Figura):
    def __init__(self, podstawa_a, podstawa_b, bok_a, bok_b):
        self.podstawa_a = podstawa_a
        self.podstawa_b = podstawa_b
        self.bok_a = bok_a
        self.bok_b = bok_b

    def oblicz_obwod
