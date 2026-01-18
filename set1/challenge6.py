import base64
from io import StringIO
from math import inf

min_key_size = 2
max_key_size = 40


def main():
    encoded = get_encoded_string()

    keysize = find_probably_keysize(encoded)
    print(keysize)
    # print(smallest_distance_keysize)
    # print(smallest_normalized_distance)


def find_probably_keysize(encoded: bytes) -> int:
    smallest_distance_keysize = inf
    smallest_normalized_distance = inf
    for KEYSIZE in range(min_key_size, max_key_size + 1):
        distance1 = (
            compute_hamming_distance(encoded[KEYSIZE * 0 : KEYSIZE * 1], encoded[KEYSIZE * 1 : KEYSIZE * 2]) / KEYSIZE
        )
        distance2 = (
            compute_hamming_distance(encoded[KEYSIZE * 2 : KEYSIZE * 3], encoded[KEYSIZE * 3 : KEYSIZE * 4]) / KEYSIZE
        )
        distance3 = (
            compute_hamming_distance(encoded[KEYSIZE * 4 : KEYSIZE * 5], encoded[KEYSIZE * 5 : KEYSIZE * 6]) / KEYSIZE
        )
        distance4 = (
            compute_hamming_distance(encoded[KEYSIZE * 6 : KEYSIZE * 7], encoded[KEYSIZE * 7 : KEYSIZE * 8]) / KEYSIZE
        )
        normalized_distance = sum([distance1, distance2, distance3, distance4]) / 4

        # normalized_distance = distance / KEYSIZE
        if normalized_distance < smallest_normalized_distance:
            smallest_distance_keysize = KEYSIZE
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
