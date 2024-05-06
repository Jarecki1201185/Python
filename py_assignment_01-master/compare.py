def compare(text1: str, text2: str) -> bool:
    text1_lower = text1.lower()
    text2_lower = text2.lower()

    return text1_lower == text2_lower


def main():
    text1 = input("podaj pierwszy ciag znakow: ")
    text2 = input("podaj drugi ciag znakow: ")

    result = compare(text1, text2)

    if result:
        print("ciagi sa takie same.")
    else:
        print("ciagi się roznia.")

if __name__ == "__main__":
    main()
