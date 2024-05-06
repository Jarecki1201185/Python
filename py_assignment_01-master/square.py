import sys

def square(wysokosc: int, grubosc: int, char='*') -> str:
    if wysokosc <= 0 or grubosc <= 0:
        return 0

    if grubosc >= wysokosc // 2:
        return 0


    zewn = char * wysokosc
    wewnt  = char * grubosc + ' ' * (wysokosc - 4) + char * grubosc


    square_str = '\n'.join([zewn if i < grubosc or i >= wysokosc - grubosc else wewnt for i in range(wysokosc)])

    return square_str

def main():

    if len(sys.argv) != 4:
        return 1


    try:
        length = int(sys.argv[1])
        thickness = int(sys.argv[2])
        char = sys.argv[3]
    except ValueError:
        return 1

    result = square(length, thickness, char)

    print(result)

if __name__ == "__main__":
    sys.exit(main())
