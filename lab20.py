#1
def reverse_words_to_palindrome(word):
    reversed_word = word[::-1]
    return word + reversed_word


def is_palindrome(word):
    return word == word[::-1]


def test_reverse_words_to_palindrome():
    assert reverse_words_to_palindrome("hello") == "helloolleh"
    assert reverse_words_to_palindrome("python") == "pythonnohtyp"
    assert reverse_words_to_palindrome("racecar") == "racecarracecar"


def test_is_palindrome():
    assert is_palindrome("hello") == False
    assert is_palindrome("racecar") == True
    assert is_palindrome("python") == False


if __name__ == "__main__":
    word = input("Podaj wyraz: ")

    reversed_word = reverse_words_to_palindrome(word)
    print("Odwrócone wyrazy:", reversed_word)

    if is_palindrome(word):
        print("Podany wyraz jest palindromem.")
    else:
        print("Podany wyraz nie jest palindromem.")

#2
def calculate_bmr(weight, height, age, gender):
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Please choose 'male' or 'female'.")

    return bmr


def test_calculate_bmr():
    assert calculate_bmr(70, 180, 30, "male") == pytest.approx(1864.074, abs=0.001)
    assert calculate_bmr(60, 160, 25, "female") == pytest.approx(1326.989, abs=0.001)
    assert calculate_bmr(80, 170, 35, "male") == pytest.approx(1912.682, abs=0.001)


if __name__ == "__main__":
    weight = float(input("Podaj wagę (w kilogramach): "))
    height = float(input("Podaj wzrost (w centymetrach): "))
    age = int(input("Podaj wiek: "))
    gender = input("Podaj płeć (male/female): ")

    bmr = calculate_bmr(weight, height, age, gender)
    print("Twoje BMR wynosi:", bmr)
