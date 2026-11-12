import sys


def main() -> None:
    """
    Filter words from a given text based on their length.
    """
    ARG_ERROR = "the arguments are bad"
    args = sys.argv
    try:
        assert len(args) == 3, ARG_ERROR
        text: str = args[1]
        assert all(char.isalnum() or char == " " for char in text), ARG_ERROR
        number = int(args[2])
        result = [
            word for word in text.split()
            if (lambda w: len(w) > number)(word)
        ]
        print(result)
    except (ValueError, AssertionError):
        print(f"AssertionError: {ARG_ERROR}")


if __name__ == "__main__":
    main()
