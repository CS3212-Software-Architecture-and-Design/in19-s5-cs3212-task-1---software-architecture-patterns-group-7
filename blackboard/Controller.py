import blackboard


class Controller(object):

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def encrypt(self, phrase):
        for ks in self.blackboard.ks:
            if ks.is_matched(int(phrase[0])):
                self.blackboard.encrypted_letter_list += phrase[0]
                ks.encrypt(phrase[1:])
                break
        output = ' '.join(self.blackboard.encrypted_letter_list)
        self.blackboard.encrypted_letter_list = []
        return output

    def decrypt(self, phrase_lst):
        for ks in self.blackboard.ks:
            if ks.is_matched(int(phrase_lst[0])):
                self.blackboard.decrypted_letter_list += phrase_lst[0]
                ks.decrypt(phrase_lst[1:])
                break
        output = ''.join(self.blackboard.decrypted_letter_list)
        self.blackboard.decrypted_letter_list = []
        return output

