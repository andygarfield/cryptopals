def main(val_str: str):
    val = bytes.fromhex(val_str)

    max_spaces_val = 0
    max_spaces = 0
    for i in range(256):
        new_str = xor_string(val, i)

        if (spaces := new_str.count(b" ")) > max_spaces:
            max_spaces = spaces
            max_spaces_val = i

    print(max_spaces_val)
    print(bytes(xor_string(val, max_spaces_val)).decode())


def xor_string(original: bytes, xor_val: int) -> bytearray:
    new_str = bytearray(len(original))
    for j in range(len(original)):
        new_str[j] = original[j] ^ xor_val

    return new_str


if __name__ == "__main__":
    main("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
