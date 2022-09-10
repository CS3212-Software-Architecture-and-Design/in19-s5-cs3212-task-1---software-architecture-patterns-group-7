import unittest

from blackboard import Blackboard, KS_Type1, KS_Type2, KS_Type3
from blackboard.Controller import Controller


class TestUnit(unittest.TestCase):

    def test_encrypt(self):
        blackboard = Blackboard()

        blackboard.add_ks(KS_Type1(blackboard))
        blackboard.add_ks(KS_Type2(blackboard))
        blackboard.add_ks(KS_Type3(blackboard))
        c = Controller(blackboard)
        result = c.encrypt("1word")
        self.assertEqual(str(result), "1 22 13 17 0")

        result = c.encrypt("1thilina")
        self.assertEqual(str(result), "1 21 10 10 8 12 8 6")

        result = c.encrypt("2dinusha")
        self.assertEqual(str(result), "2 5 11 95 71 16 12 82")

        result = c.encrypt("2yasiru")
        self.assertEqual(str(result), "2 24 3 66 91 17 17")

        result = c.encrypt("3sathsarani")
        self.assertEqual(str(result), "3 18 3 43 89 16 5 50 82 15 11")

        result = c.encrypt("3chamod")
        self.assertEqual(str(result), "3 2 10 62 92 12 0")

    def test_decrypt(self):
        blackboard = Blackboard()
        blackboard.add_ks(KS_Type1(blackboard))
        blackboard.add_ks(KS_Type2(blackboard))
        blackboard.add_ks(KS_Type3(blackboard))
        c = Controller(blackboard)
        result = c.decrypt(['1', '22', '13', '17', '0'])
        self.assertEqual(str(result), "1word")

        result = c.decrypt(['1', '21', '10', '10', '8', '12', '8', '6'])
        self.assertEqual(str(result), "1thilina")

        result = c.decrypt(['2', '5', '11', '95', '71', '16', '12', '82'])
        self.assertEqual(str(result), "2dinusha")

        result = c.decrypt(['2', '24', '3', '66', '91', '17', '17'])
        self.assertEqual(str(result), "2yasiru")

        result = c.decrypt(['3', '18', '3', '43', '89', '16', '5', '50', '82', '15', '11'])
        self.assertEqual(str(result), "3sathsarani")

        result = c.decrypt(['3', '2', '10', '62', '92', '12', '0'])
        self.assertEqual(str(result), "3chamod")
