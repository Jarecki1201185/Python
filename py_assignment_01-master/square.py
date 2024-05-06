import sys

def square(length: int, thickness: int, char='*') -> str:
    # Sprawdzenie poprawności argumentów
    if length <= 0 or thickness <= 0:
        return "Długość boku i grubość ścianek muszą być liczbami dodatnimi."

    if thickness >= length // 2:
        return "Grubość ścianek nie może być większa lub równa połowie długości boku."

    # Utworzenie wierszy zewnętrznych i wewnętrznych
    outer_row = char * length
    inner_row = char * thickness + ' ' * (length - 4) + char * thickness

    # Składanie kwadratu
    square_str = '\n'.join([outer_row if i < thickness or i >= length - thickness else inner_row for i in range(length)])

    return square_str

def main():
    # Sprawdzenie liczby argumentów
    if len(sys.argv) != 4:
        print("Użycie: python square.py <długość_boku> <grubość_ścianek> <znak>")
        return 1

    # Pobranie argumentów
    try:
        length = int(sys.argv[1])
        thickness = int(sys.argv[2])
        char = sys.argv[3]
    except ValueError:
        print("Długość boku i grubość ścianek muszą być liczbami całkowitymi.")
        return 1

    # Rysowanie kwadratu
    result = square(length, thickness, char)

    # Wyświetlenie wyniku
    print(result)

if __name__ == "__main__":
    sys.exit(main())