import string


class Shift:
    def __init__(self):
        self.letters = list("aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyzAÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ+-,?!.:&@#><()=/%\"'[]$_*")

    def encode(self, szoveg: str, k: int):
        return "".join(
            [self.letters[((self.letters.index(x) + k) % len(self.letters))]
             if x in self.letters else " " for x in szoveg
             ]).rstrip(" ")

    def decode(self, code, k):
        return "".join([self.letters[((self.letters.index(x) - k) % len(self.letters))]
                        if x in self.letters else " " for x in code
                        ]).rstrip(" ")
