def main(val1: str, val2: str):
    v1 = bytes.fromhex(val1)
    v2 = bytes.fromhex(val2)

    new_buffer = bytearray(len(v1))
    for i in range(len(v1)):
        new_buffer[i] = v1[i] ^ v2[i]

    assert bytes(new_buffer) == bytes.fromhex("746865206b696420646f6e277420706c6179")


if __name__ == "__main__":
    val1 = "1c0111001f010100061a024b53535009181c"
    val2 = "686974207468652062756c6c277320657965"
    main(val1, val2)
