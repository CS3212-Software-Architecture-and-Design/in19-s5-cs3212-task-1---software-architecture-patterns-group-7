from blackboard.AbstractKS import AbstractKS


class KS_Type3(AbstractKS):
    def __init__(self, blackboard):
        super().__init__(blackboard)
        self.__type_no = 3
        self.__secret_key = 'ab_1cd@3'

    def is_matched(self, type_no):
        return self.__type_no == type_no

    def encrypt(self, phrase):
        for i in range(len(phrase)):
            self.blackboard.encrypted_letter_list.append(str(
                ord(phrase[i]) ^ ord(self.__secret_key[i % len(self.__secret_key)])))

    def decrypt(self, phrase):
        for i in range(len(phrase)):
            self.blackboard.decrypted_letter_list.append(chr(
                int(phrase[i]) ^ ord(self.__secret_key[i % len(self.__secret_key)])))

