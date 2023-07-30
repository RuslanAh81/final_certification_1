from data.dbmysql_manager import MySqlManager
from model import RegistryAnimals
from view.abstract_view import View


class Presenter:
    def __init__(self, view: View, log_registry: RegistryAnimals, data: MySqlManager):
        self.view = view
        self.log_registry = log_registry
        self.view.set_presenter(self)
        self.data = data

    def read_db(self):
        return self.data.read_db(self.log_registry)

    def get_tabl_registry(self):
        return self.log_registry.tabl_registry

    def all_kinds_pets(self):
        return self.log_registry.list_kind_pets()

    def all_kinds_pack(self):
        return self.log_registry.list_kind_pack()

    def add_animal(self, kind, name, birth_date, command):
        self.log_registry.add_animal(kind, name, birth_date,command)

    def save_animal_into_db(self, type_id, kind, name, birth_date, command):
        return self.data.save_animal(type_id, kind, name, birth_date, command)

    def find_animal(self, index):
        return self.log_registry.find_animal(index)

    def get_command(self, index):
        return self.log_registry.get_command(index)

    def add_command(self, index, command):
        return self.log_registry.add_command(index, command)

    def size_registry(self):
        return self.log_registry.number_of_animals()

    def save_command(self, index):
        return self.data.save_command(index, self.log_registry)
