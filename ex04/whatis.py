import sys


def whatis(number: int) -> str:
    return "I'm Even." if number % 2 == 0 else "I'm Odd."


def main():
    args_count = len(sys.argv)
    if args_count == 1:
        return
    assert args_count == 2, "more than one argument is provided"
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer") from None
    print(whatis(number))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")


# Expected output:
# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# Error handling
# If more than one argument is given, or if the provided argument is not an integer, print
# an AssertionError.
# Expected output:
# 9Training Piscine Python for Data Science - 0
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided
