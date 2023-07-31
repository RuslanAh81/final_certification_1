from tabulate import tabulate
from model.pets import Cats, Dogs, Hamsters
from model.pack_animals import Horses, Camels, Donkeys



class RegistryAnimals:
    def __init__(self):
        self.__log_registry = []
        print(" создаем словарь")
        print(self.__log_registry)

    def get_log_registry(self):
        return self.get_log_registry()

    def number_of_animals(self):
        print(len(self.__log_registry))
        return len(self.__log_registry)

    def __add_cat(self, name, birth_date, command, id_animal=None):
        cat = Cats(id_animal, name, birth_date, command)
        self.__log_registry.append(cat)

    def __add_dog(self, name, birth_date, command, id_animal=None):
        dog = Dogs(id_animal, name, birth_date, command)
        self.__log_registry.append(dog)

    def __add_hamster(self, name, birth_date, command, id_animal=None):
        hamster = Hamsters(id_animal, name, birth_date, command)
        self.__log_registry.append(hamster)

    def __add_horse(self, name, birth_date, command, id_animal=None):
        horse = Horses(id_animal, name, birth_date, command)
        self.__log_registry.append(horse)

    def __add_camel(self, name, birth_date, command, id_animal=None):
        camel = Camels(id_animal, name, birth_date, command)
        self.__log_registry.append(camel)

    def __add_donkey(self, name, birth_date, command, id_animal=None):
        donkey = Donkeys(id_animal, name, birth_date, command)
        self.__log_registry.append(donkey)

    __function_add_animal = {'кошка': __add_cat, 'собака': __add_dog, 'хомяк': __add_hamster, 'лошадь': __add_horse,
                             'верблюд': __add_camel,'осел': __add_donkey}

    def add_animal(self, kind, name, birth_date, command):
        for key, value in self.__function_add_animal.items():
            if key ==kind:
                value(self, name, birth_date, command)
                break

    @property
    def tabl_registry(self):
        headers = ['№', 'Тип животного', 'Вид животного', 'Имя',
                   'Дата рождения', 'Список команд']
        tabl = [[i, animal.get_type_animals(),
                 animal.get_kind_animals(), animal.get_name(),
                 animal.get_birth_date(), animal.get_command()]
                for i, animal in enumerate(self.__log_registry, start=1)]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')

    def list_kind_pets(self):
        kind_pets = set()
        for item in self.__log_registry:
            if item.get_id_type() == 1:
                kind_pets.add(item.get_kind_animals())
        return kind_pets

    def list_kind_pack(self):
        kind_pack = set()
        for item in self.__log_registry:
            if item.get_id_type() == 2:
                kind_pack.add(item.get_kind_animals())
        return kind_pack

    def find_animal(self, index):
        return self.__log_registry[index]

    def get_command(self, index):
        return self.__log_registry[index].get_command()

    def add_command(self, index, commands):
        self.__log_registry[index].add_command(commands)

