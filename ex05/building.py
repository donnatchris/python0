import sys
import string

ARGS_COUNT_ERROR = "more than one argument is provided"


def caracter_count(text: str) -> str:
    """
    Count the number of upper case letters, lower case letters,
    punctuation marks, spaces and digits in a given text.

    Args:
        text (str): The text to count.

    Returns:
        str: A string containing the counts of each character type.
    """
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
        elif char in string.punctuation:
            punctuation += 1

    return f"""The text contains {len(text)} characters:
{upper} upper letters
{lower} lower letters
{punctuation} punctuation marks
{spaces} spaces
{digits} digits"""


def main() -> None:
    """
    Handle command-line arguments and count text characters.

    Print an error message if too many arguments are provided.
    """
    try:
        args_cont = len(sys.argv)
        text = ""
        if args_cont == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]
        assert args_cont < 3, ARGS_COUNT_ERROR
        print(caracter_count(text))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
