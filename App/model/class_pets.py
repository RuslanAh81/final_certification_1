
from model.animals import Animals


class Pets(Animals):
    def __init__(self, kind_animals):
        super().__init__(id_type=1, type_animals="домашнее животное")
        self.__kind_animals = kind_animals

    def get_id_type(self):
        return 1

    def get_type_animals(self):
        return "домашнее животное"

    def get_kind_animals(self):
        return self.__kind_animals