#1
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.name}")
        print(f"Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(flavor)

    def open_restaurant(self):
        print(f"Ice cream stand {self.name} is now open!")


class CoffeeShop(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.coffees = []

    def add_coffee(self, coffee):
        self.coffees.append(coffee)

    def display_coffees(self):
        print("Available coffees:")
        for coffee in self.coffees:
            print(coffee)



ice_cream_stand = IceCreamStand("Sweet Delights", "Ice Cream Shop")
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Chocolate")
ice_cream_stand.add_flavor("Strawberry")
ice_cream_stand.display_flavors()
ice_cream_stand.open_restaurant()


coffee_shop = CoffeeShop("Caffeine Boost", "Coffee Shop")
coffee_shop.add_coffee("Americano")
coffee_shop.add_coffee("Latte")
coffee_shop.display_coffees()
coffee_shop.open_restaurant()

#2
class Beer:
    def __init__(self, name, category, alcohol_content, price):
        self.name = name
        self.category = category
        self.alcohol_content = alcohol_content
        self.price = price
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_average_rating(self):
        if len(self.reviews) == 0:
            return 0
        total_rating = sum(review['rating'] for review in self.reviews)
        return total_rating / len(self.reviews)

    def __str__(self):
        return f"Beer: {self.name}\nCategory: {self.category}\nAlcohol Content: {self.alcohol_content}%\nPrice: {self.price}\n"


class Sklep:
    def __init__(self):
        self.beers = []

    def add_beer(self, beer):
        self.beers.append(beer)

    def sort_by_rating(self):
        self.beers.sort(key=lambda x: x.get_average_rating(), reverse=True)

    def sort_by_name(self):
        self.beers.sort(key=lambda x: x.name)

    def display_beers(self):
        for beer in self.beers:
            print(beer)


beer1 = Beer("IPA", "Ale", 6.5, 3.99)
beer1.add_review({'rating': 4, 'comment': 'Great IPA!'})
beer1.add_review({'rating': 5, 'comment': 'Love the hoppy flavor!'})

beer2 = Beer("Stout", "Porter", 7.2, 4.99)
beer2.add_review({'rating': 3, 'comment': 'Decent stout.'})
beer2.add_review({'rating': 4, 'comment': 'Smooth and rich taste.'})

beer3 = Beer("Wheat Beer", "Hefeweizen", 5.0, 3.49)
beer3.add_review({'rating': 5, 'comment': 'Refreshing and flavorful.'})
beer3.add_review({'rating': 4, 'comment': 'Perfect for summer.'})


sklep = Sklep()
sklep.add_beer(beer1)
sklep.add_beer(beer2)
sklep.add_beer(beer3)


sklep.sort_by_rating()
print("Sorted by rating:")
sklep.display_beers()


sklep.sort_by_name()
print("Sorted by name:")
sklep.display_beers()


#3
class Obywatel:
    def __init__(self):
        self.imię = ""
        self.nazwisko = ""
        self.ulica = ""
        self.nr_domu = ""
        self.kod_pocztowy = ""
        self.miejscowość = ""

    def wczytaj_dane(self):
        self.imię = input("Podaj imię: ")
        self.nazwisko = input("Podaj nazwisko: ")
        self.ulica = input("Podaj ulicę: ")
        self.nr_domu = input("Podaj numer domu: ")
        self.kod_pocztowy = input("Podaj kod pocztowy: ")
        self.miejscowość = input("Podaj miejscowość: ")

    def wizytówka(self):
        return f"""{self.imię} {self.nazwisko}
{self.ulica} {self.nr_domu}
{self.kod_pocztowy} {self.miejscowość}"""

    def drukuj_do_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, "w") as plik:
            plik.write(self.wizytówka())


obywatel = Obywatel()

obywatel.wczytaj_dane()

print(obywatel.wizytówka())

obywatel.drukuj_do_pliku("wizytówka.txt")


#4
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank < other.rank


class Deck:
    def __init__(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def display(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def move_card(self, card, destination):
        self.cards.remove(card)
        destination.add_card(card)


deck = Deck()


print("Deck of cards:")
deck.display()


deck.shuffle()
print("\nShuffled deck:")
deck.display()


deck.sort()
print("\nSorted deck:")
deck.display()


new_card = Card("Ace", "Spades")
deck.add_card(new_card)
print("\nDeck after adding a card:")
deck.display()


card_to_remove = Card("2", "Hearts")
deck.remove_card(card_to_remove)
print("\nDeck after removing a card:")
deck.display()


second_deck = Deck()

card_to_move = Card("3", "Diamonds")
deck.move_card(card_to_move, second_deck)
print("\nFirst deck after moving a card:")
deck.display()
print("\nSecond deck after moving a card:")
second_deck.display()
