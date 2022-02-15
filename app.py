#!/usr/bin/env python


def get_value(text: str) -> int:
    """
    Traverses str to get the sum ord values then mod 10
    :param text:
    :return: int
    """
    return sum([ord(x) for x in list(text)]) % 10


def is_alphabet_letters(text: str):
    """
    Test if text is alphabet letters, throws exception if isn't
    :param text:
    """
    if not text.isalpha():
        raise ValueError("Input must be from American alphabet.")


def run():
    print("Enter text: ")
    text = input()
    print(f"Entered text: {text}")
    # Raises an exception if text not in alphabet.
    is_alphabet_letters(text)
    print(f"Answer: {get_value(text)}")


if __name__ == "__main__":
    run()
