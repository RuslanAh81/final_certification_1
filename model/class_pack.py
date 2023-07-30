
from model.animals import Animals


class PackAnimals(Animals):
    def __init__(self, kind_animals):
        super().__init(id_type=2, type_animals="вьючное животное")
        self.kind_animals = kind_animals
        
    def get_id_type(self):
        return 2

    def get_type_animals(self):
        return "вьючное животное"

    def get_kind_animals(self):
        return self.kind_animals

