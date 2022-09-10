from blackboard.Blackboard import Blackboard
from blackboard.Controller import Controller
from blackboard.KS_Type1 import KS_Type1
from blackboard.KS_Type2 import KS_Type2
from blackboard.KS_Type3 import KS_Type3

if __name__ == '__main__':
    blackboard = Blackboard()

    blackboard.add_ks(KS_Type1(blackboard))
    blackboard.add_ks(KS_Type2(blackboard))
    blackboard.add_ks(KS_Type3(blackboard))

    c = Controller(blackboard)
    operation = int(input("Enter 1 for encrypt and 2 for decrypt: \n"))
    from pprint import pprint

    if operation == 1:
        contributions = c.encrypt(input("Enter the word to encrypt with secret key ranked from 1 to 3, "
                                        "eg: 1wordtoencrypt "
                                        "or 2wordtoencrypt or 3wordtoencrypt: \n"))
        pprint(contributions)
    elif operation == 2:
        encrypted_letter_list = input("Enter the word to decrypt with secret key ranked from 1 to 3, "
                                      "eg: encryptedword "
                                      "or encryptedword or encryptedword: \n").split()
        contributions = c.decrypt(encrypted_letter_list)
        pprint(contributions)