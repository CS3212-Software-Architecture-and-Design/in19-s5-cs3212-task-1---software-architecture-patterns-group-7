import time
import unittest

from blackboard import Blackboard, KS_Type1, KS_Type2, KS_Type3
from blackboard.Controller import Controller


class TestIntegrate(unittest.TestCase):

    def test_encryption(self):
        blackboard = Blackboard()
        blackboard.add_ks(KS_Type1(blackboard))
        blackboard.add_ks(KS_Type2(blackboard))
        blackboard.add_ks(KS_Type3(blackboard))
        c = Controller(blackboard)

        result = c.encrypt("1 this is the assignment for SAD task 1")
        self.assertEqual(str(result),
                         "1 65 22 11 13 22 70 14 27 65 22 11 1 69 7 20 27 8 5 13 9 0 8 19 72 7 13 17 68 54 39 35 72 21 3 16 15 69 87")

        result = c.encrypt("2 this is the assignment for SAD task 1")
        self.assertEqual(str(result),
                         "2 65 22 89 91 16 68 90 71 65 22 89 87 67 5 64 71 8 5 95 95 6 10 71 20 7 13 67 18 48 37 119 20 21 3 66 89 67 85")

        result = c.encrypt("3 this is the assignment for SAD task 1")
        self.assertEqual(str(result),
                         "3 65 22 55 88 16 68 41 64 65 22 55 84 67 5 51 64 8 5 49 92 6 10 52 19 7 13 45 17 48 37 4 19 21 3 44 90 67 85")

    def test_decryption(self):
        blackboard = Blackboard()
        blackboard.add_ks(KS_Type1(blackboard))
        blackboard.add_ks(KS_Type2(blackboard))
        blackboard.add_ks(KS_Type3(blackboard))
        c = Controller(blackboard)

        result = c.decrypt(
            ['1', '65', '22', '11', '13', '22', '70', '14', '27', '65', '22', '11', '1', '69', '7', '20', '27', '8',
             '5', '13', '9', '0', '8', '19', '72', '7', '13', '17', '68', '54', '39', '35', '72', '21', '3', '16', '15',
             '69', '87'])
        self.assertEqual(str(result), "1 this is the assignment for SAD task 1")

        result = c.decrypt(
            ['2', '65', '22', '89', '91', '16', '68', '90', '71', '65', '22', '89', '87', '67', '5', '64', '71', '8',
             '5', '95', '95', '6', '10', '71', '20', '7', '13', '67', '18', '48', '37', '119', '20', '21', '3', '66',
             '89', '67', '85']
        )
        self.assertEqual(str(result), "2 this is the assignment for SAD task 1")

        result = c.decrypt(
            ['3', '65', '22', '55', '88', '16', '68', '41', '64', '65', '22', '55', '84', '67', '5', '51', '64', '8',
             '5', '49', '92', '6', '10', '52', '19', '7', '13', '45', '17', '48', '37', '4', '19', '21', '3', '44',
             '90', '67', '85']
        )
        self.assertEqual(str(result), "3 this is the assignment for SAD task 1")


if __name__ == "__main__":
    unittest.main()