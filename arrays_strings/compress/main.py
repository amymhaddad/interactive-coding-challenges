
from compress import list_repeated_and_unique_letters, compress_string, shortest_string


def main(string):
    """Compress a string if the length of the compressed string is less than the given string"""

    repeated_letters = list_repeated_and_unique_letters(string)
    compressed_string = compress_string(repeated_letters)

    print(shortest_string(string))


if __name__ == "__main__":
    string = "AABBCC"
    main(string)
