import unittest, string
from .Shift import Shift
from .Ablak import Ablak


class CodolasTest(unittest.TestCase):
    shift = Shift()

    def test_shift(self):
        code = "kacsa"
        coded = (self.shift.encode(code, 140))
        decoded = (self.shift.decode(coded, 140))
        print(coded)
        print(decoded)
        self.assertEqual(coded, "SÍL+Í")
        self.assertEqual(decoded, code)


if __name__ == '__main__':
    unittest.main()
