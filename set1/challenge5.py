import base64
from pathlib import Path

PHRASE = """T is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife.
However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.
"My dear Mr. Bennet," said his lady to him one day, "have you heard that Netherfield Park is let at last?"
Mr. Bennet replied that he had not.
"But it is," returned she; "for Mrs. Long has just been here, and she told me all about it."
Mr. Bennet made no answer.
"Do not you want to know who has taken it?" cried his wife, impatiently.
"You want to tell me, and I have no objection to hearing it.\""""
KEY = "ICE"


base_dir = Path(__file__).parent


def main():
    encoded = bytearray(len(PHRASE))
    for i, char in enumerate(PHRASE):
        encoded[i] = ord(char) ^ ord(KEY[i % len(KEY)])

    with open(base_dir / "6.txt", "wb+") as f:
        _ = f.write(base64.b64encode(encoded))


if __name__ == "__main__":
    main()
