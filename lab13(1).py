#1
class Car:
    def __init__(self,marka,model,przebieg,color,spalanie,przyspiszenie):
         self.marka = marka
         self.model = model
         self.przebieg = przebieg
         self.color = color
         self.spalanie = spalanie
         self.przyspiszenie = przyspiszenie
    def jedzprosto (self):
           print (self.przyspiszenie + " " + "Jade")
    def hamuj (self):
           print (self.spalanie + " " + "Hamuje")
    def driftuj (self):
            print ("Driftuję")
    def crash (self):
             print ("Crashuje")
    def przyspiesz (self):
             print ("Przyspiesza")
ferrari = Car("ferrari","kabriolet","2000","czerwony","11.4","350 km/h")
mersedec = Car("mersedec","gle amg 63","4000","biały","15.3","292 km/h")
bmw = Car("bmw","e34","10000","szary","10.5","192 km/h")
tesla = Car("tesla","y","23000","czarny","elektro","330 km/h")

tesla.jedzprosto()
mersedec.hamuj()
bmw.driftuj()

#2
class Book:
    def __init__(self,nazwa,autor,liczba_stron,rok_wydania):
        self.nazwa = nazwa
        self.autor = autor
        self.liczba_stron = liczba_stron
        self.rok_wydania = rok_wydania
    def czytaj (self):
        print(self.nazwa + self.liczba_stron + " " + "czytam")
    def zamknij (self):
        print("zamkykam")
    def przegladaj (self):
        print(self.nazwa + self.autor + " " + "przegladam")
    def oceniac (self):
        print("oceniam")

To = Book("To","stephen_king","1138","1986")
Harry_Potter = Book("Harry_Potter","Joanna Rouling","328","1997")

To.czytaj()
Harry_Potter.przegladaj()

#3
class Smartfon:
    def __init__(self, marka, model, rok_produkcji, cena):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.cena = cena
        self.wlaczony = False
        self.bateria_poziom = 100

    def wlacz(self):
        self.wlaczony = True
        print(f"Smartfon {self.marka} {self.model} został włączony.")

    def wylacz(self):
        self.wlaczony = False
        print(f"Smartfon {self.marka} {self.model} został wyłączony.")

    def sprawdz_baterie(self):
        print(f"Aktualny poziom baterii: {self.bateria_poziom}%")

    def ladowanie(self, poziom):
        if self.wlaczony:
            print("Nie można ładować smartfona podczas używania.")
        else:
            self.bateria_poziom += poziom
            if self.bateria_poziom > 100:
                self.bateria_poziom = 100
            print(f"Smartfon {self.marka} {self.model} został naładowany.")

    def wyswietl_informacje(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Rok produkcji: {self.rok_produkcji}")
        print(f"Cena: {self.cena} zł")
        print(f"Stan: {'Włączony' if self.wlaczony else 'Wyłączony'}")
        print(f"Poziom baterii: {self.bateria_poziom}%")


smartfon1 = Smartfon("Apple", "iPhone 12", 2020, 4500)
smartfon2 = Smartfon("Samsung", "Galaxy S21", 2021, 4000)


smartfon1.wlacz()
smartfon1.sprawdz_baterie()
smartfon1.ladowanie(20)
smartfon1.sprawdz_baterie()
smartfon1.wylacz()

smartfon2.wlacz()
smartfon2.wyswietl_informacje()

#4
class Student:
    def __init__(self, imie, nazwisko, numer_indeksu, rok_studiow):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.rok_studiow = rok_studiow
        self.oceny = []

    def dodaj_ocene(self, przedmiot, ocena):
        self.oceny.append((przedmiot, ocena))
        print(f"Dodano ocenę {ocena} z przedmiotu {przedmiot} dla studenta {self.imie} {self.nazwisko}.")

    def srednia_ocen(self):
        if len(self.oceny) == 0:
            return 0.0
        suma_ocen = sum(ocena for _, ocena in self.oceny)
        srednia = suma_ocen / len(self.oceny)
        return srednia

    def informacje(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Numer indeksu: {self.numer_indeksu}")
        print(f"Rok studiów: {self.rok_studiow}")
        print("Oceny:")
        for przedmiot, ocena in self.oceny:
            print(f"- {przedmiot}: {ocena}")

    def sprawdz_warunki(self):
        if self.rok_studiow < 3:
            print("Student nie spełnia warunków do przystąpienia do egzaminów końcowych.")
        else:
            print("Student spełnia warunki do przystąpienia do egzaminów końcowych.")

    def zloz_podanie_o_stypendium(self):
        if self.srednia_ocen() >= 4.5:
            print(f"Student {self.imie} {self.nazwisko} spełnia warunki do złożenia podania o stypendium.")
        else:
            print(f"Student {self.imie} {self.nazwisko} nie spełnia warunków do złożenia podania o stypendium.")


student1 = Student("Jan", "Kowalski", "123456", 3)
student2 = Student("Anna", "Nowak", "654321", 2)


student1.dodaj_ocene("Matematyka", 4.5)
student1.dodaj_ocene("Fizyka", 3.0)
student1.dodaj_ocene("Chemia", 5.0)

student2.dodaj_ocene("Historia", 4.0)
student2.dodaj_ocene("Język angielski", 4.5)
student2.dodaj_ocene("Informatyka")
