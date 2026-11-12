import sys


ARG_ERROR = "the arguments are bad"


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def text_to_morse(text: str) -> str:
    """
    Convert a given text to Morse code.

    Args:
        text (str): The text to convert.

    Returns:
        str: The Morse code representation of the text.

    Raises:
        AssertionError:
        If the text contains characters that cannot be converted to Morse code.
    """
    morse: list[str] = []
    for char in text:
        morse_char = NESTED_MORSE.get(char.upper())
        if morse_char is None:
            raise AssertionError(ARG_ERROR)
        morse.append(morse_char)
    return "".join(morse)[:-1]


def main() -> None:
    """
    Convert the first command-line argument to Morse code.

    Print an error message if the arguments are bad.
    """
    try:
        assert len(sys.argv) == 2, ARG_ERROR
        print(text_to_morse(sys.argv[1]))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
