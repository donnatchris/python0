import sys
from ft_package import count_in_list


def main():
    """
    Main function to count occurrences of a string in a list.
    """
    my_list = ["toto", "tata", "toto"]

    args = sys.argv
    args_len = len(args)
    if args_len != 2:
        print("Usage: python test.py <string>")
        print('Count the occurrences of a string in a predefined list:')
        print('["toto", "tata", "toto"].')
        return
    print(count_in_list(my_list, args[1]))


if __name__ == "__main__":
    main()
