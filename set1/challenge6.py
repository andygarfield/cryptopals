import base64
from io import StringIO
from math import inf
from pathlib import Path

MIN_KEY_SIZE = 2
MAX_KEY_SIZE = 40
base_dir = Path(__file__).parent


def main():
    encoded = get_encoded_string()

    key_size = find_probably_keysize(encoded)
    blocks: list[bytearray] = []

    # seed buffers
    for i in range(key_size):
        blocks.append(bytearray())

    for i, b in enumerate(encoded):
        blocks[i % key_size].append(b)

    key = bytearray()
    for block in blocks:
        xor_value = find_xor_value(bytes(block))
        key.append(xor_value)

    print("key -", bytes(key).decode())

    decoded = bytearray(len(encoded))
    for i, char in enumerate(encoded):
        decoded[i] = char ^ key[i % len(key)]

    print(decoded.decode("cp1252"))


def find_xor_value(input_val: bytes):
    max_letters_val = 0
    max_letters = 0

    values: list[int] = (list(range(ord("a"), ord("z") + 1)) + list(range(ord("A"), ord("Z") + 1))) + [
        ord(" "),
        ord("."),
    ]

    for i in values:
        new_str = xor_string(input_val, i)

        letters_count = 0
        for b in new_str:
            # if (ord("A") <= b <= ord("Z")) or (ord("a") <= b <= ord("z") or b == ord(" ") or b == ord(".")):
            if b == ord(" "):
                letters_count += 1
        if letters_count > max_letters:
            max_letters = letters_count
            max_letters_val = i

    return max_letters_val


def xor_string(original: bytes, xor_val: int) -> bytearray:
    new_str = bytearray(len(original))
    for j in range(len(original)):
        new_str[j] = original[j] ^ xor_val

    return new_str


def find_probably_keysize(encoded: bytes) -> int:
    smallest_distance_keysize = inf
    smallest_normalized_distance = inf

    hamming_sum = 0
    hamming_count = 0
    for key_size in range(MIN_KEY_SIZE, MAX_KEY_SIZE + 1):
        iteration = 0
        while True:
            if key_size * (iteration + 2) >= len(encoded):
                break
            hamming_sum += (
                compute_hamming_distance(
                    encoded[key_size * iteration : key_size * (iteration + 1)],
                    encoded[key_size * (iteration + 1) : key_size * (iteration + 2)],
                )
                / key_size
            )
            hamming_count += 1
            iteration += 2
        normalized_distance = hamming_sum / hamming_count

        if normalized_distance < smallest_normalized_distance:
            smallest_distance_keysize = key_size
            smallest_normalized_distance = normalized_distance
            print("smallest", smallest_distance_keysize, normalized_distance)
        else:
            print("bigger", key_size, normalized_distance)

    return int(smallest_distance_keysize)


def compute_hamming_distance(s1: bytes, s2: bytes):
    assert len(s1) == len(s2)

    distance = 0
    for i in range(len(s1)):
        distance += "{0:b}".format(s1[i] ^ s2[i]).count("1")

    return distance


def get_encoded_string() -> bytes:
    base64_str = StringIO()
    with open(base_dir / "6.txt") as f:
        for line in f:
            _ = base64_str.write(line.strip())

    return base64.b64decode(base64_str.getvalue())


if __name__ == "__main__":
    main()
