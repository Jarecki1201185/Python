import sys

def palindrom(text: str) -> bool:
    tekst1 = ''.join(text.lower().split())

    return tekst1 == tekst1[::-1]

def main():
    if len(sys.argv) != 2:
        return 1

    text = sys.argv[1]

    if palindrom(text):
        print("jest palindromem.")
        return 0
    else:
        print("nie jest palindromem.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
