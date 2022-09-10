import abc


class AbstractKS(object):
    def __init__(self, blackboard):
        self.__secret_key = None
        self.blackboard = blackboard

    @abc.abstractmethod
    def is_matched(self, type_number):
        raise NotImplementedError('Must provide implementation in subclass.')

    @abc.abstractmethod
    def encrypt(self, phrase):
        raise NotImplementedError('Must provide implementation in subclass.')

    @abc.abstractmethod
    def decrypt(self, phrase):
        raise NotImplementedError('Must provide implementation in subclass.')
