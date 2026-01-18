from pathlib import Path


def main():
    max_letters_line: bytes = b""
    max_letters_val = 0
    max_letters = 0
    with open(Path(__file__).parent / "4.txt") as f:
        for line in f:
            line = bytes.fromhex(line.strip())

            for i in range(256):
                new_str = xor_string(line, i)

                letters_count = 0
                for b in new_str:
                    if (ord("A") <= b <= ord("Z")) or (ord("a") <= b <= ord("z") or b == ord(" ") or b == ord(".")):
                        letters_count += 1
                if letters_count > max_letters:
                    max_letters = letters_count
                    max_letters_val = i
                    max_letters_line = line

    print(max_letters_val)
    print(max_letters_line.hex())
    print(bytes(xor_string(max_letters_line, max_letters_val)).decode("cp1252"))


def xor_string(original: bytes, xor_val: int) -> bytearray:
    new_str = bytearray(len(original))
    for j in range(len(original)):
        new_str[j] = original[j] ^ xor_val

    return new_str


if __name__ == "__main__":
    main()
