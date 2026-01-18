import base64
from io import StringIO
from math import inf

MIN_KEY_SIZE = 2
MAX_KEY_SIZE = 40


def main():
    encoded = get_encoded_string()

    keysize = find_probably_keysize(encoded)
    print(keysize)
    # print(smallest_distance_keysize)
    # print(smallest_normalized_distance)


def find_probably_keysize(encoded: bytes) -> int:
    smallest_distance_keysize = inf
    smallest_normalized_distance = inf
    for key_size in range(MIN_KEY_SIZE, MAX_KEY_SIZE + 1):
        distance1 = (
            compute_hamming_distance(encoded[key_size * 0 : key_size * 1], encoded[key_size * 1 : key_size * 2])
            / key_size
        )
        distance2 = (
            compute_hamming_distance(encoded[key_size * 2 : key_size * 3], encoded[key_size * 3 : key_size * 4])
            / key_size
        )
        distance3 = (
            compute_hamming_distance(encoded[key_size * 4 : key_size * 5], encoded[key_size * 5 : key_size * 6])
            / key_size
        )
        distance4 = (
            compute_hamming_distance(encoded[key_size * 6 : key_size * 7], encoded[key_size * 7 : key_size * 8])
            / key_size
        )
        normalized_distance = sum([distance1, distance2, distance3, distance4]) / 4

        # normalized_distance = distance / KEYSIZE
        if normalized_distance < smallest_normalized_distance:
            smallest_distance_keysize = key_size
            smallest_normalized_distance = normalized_distance

    return int(smallest_distance_keysize)


def compute_hamming_distance(s1: bytes, s2: bytes):
    assert len(s1) == len(s2)

    distance = 0
    for i in range(len(s1)):
        distance += "{0:b}".format(s1[i] ^ s2[i]).count("1")

    return distance


def get_encoded_string() -> bytes:
    base64_str = StringIO()
    with open("6.txt") as f:
        for line in f:
            _ = base64_str.write(line.strip())

    return base64.b64decode(base64_str.getvalue())


if __name__ == "__main__":
    main()
