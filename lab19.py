#1
import re

def sprawdz_kod_pocztowy(kod):
    if not re.match(r'^\d{2}-\d{3}$', kod):
        raise ValueError("Nieprawidłowy kod pocztowy")
    return kod


def dodaj_kod_pocztowy_do_pliku(kod):
    with open("kody_pocztowe.txt", "a") as plik:
        plik.write(kod + "\n")


def main():
    kod_pocztowy = input("Podaj kod pocztowy: ")
    try:
        kod_pocztowy = sprawdz_kod_pocztowy(kod_pocztowy)
        dodaj_kod_pocztowy_do_pliku(kod_pocztowy)
        print("Kod pocztowy dodany do pliku.")
    except ValueError as e:
        print("Błąd:", str(e))


if __name__ == "__main__":
    main()

#2
def main():
    file1 = input("Podaj nazwę pierwszego pliku: ")
    file2 = input("Podaj nazwę drugiego pliku: ")

    try:
        with open(file1, "r") as f1, open(file2, "r") as f2, open("wynik.txt", "w") as wynik_file:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            for line1, line2 in zip(lines1, lines2):
                wynik_file.write(line1.strip() + "\n")
                wynik_file.write(line2.strip() + "\n")

            # Jeśli plik 1 ma więcej wierszy
            if len(lines1) > len(lines2):
                for line in lines1[len(lines2):]:
                    wynik_file.write(line.strip() + "\n")
            # Jeśli plik 2 ma więcej wierszy
            elif len(lines1) < len(lines2):
                for line in lines2[len(lines1):]:
                    wynik_file.write(line.strip() + "\n")

        print("Wynik zapisano do pliku wynik.txt.")

    except FileNotFoundError:
        print("Nie można odnaleźć podanego pliku.")
    except IOError:
        print("Wystąpił błąd wejścia/wyjścia.")


if __name__ == "__main__":
    main()
