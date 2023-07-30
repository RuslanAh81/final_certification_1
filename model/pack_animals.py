from model.class_pack import PackAnimals


class Horses(PackAnimals):
    def __init__(self, id_animal, name, birth_date, command):
        super().__init__(kind_animals="лошадь")
        self.__name = name
        self.__birth_date = birth_date
        self.__command = command
        self.__id_animal = id_animal

    def get_id_animal(self):
        return self.__id_animal

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_command(self):
        return self.__command

    def add_command(self, new_commands):
        if self.__command == '' or self.__command == 'не обучено':
            self.__command = new_commands
        else:
            self.__command = self.__command + ', ' + new_commands

    def __str__(self):
        return f'{self.get_kind_animals()} {self.__name}\n{self.__birth_date}\nкоманды: {self.__command}'


class Camels(PackAnimals):
    def __init__(self, id_animal, name, birth_date, command):
        super().__init__(kind_animals="верблюд")
        self.__name = name
        self.__birth_date = birth_date
        self.__command = command
        self.__id_animal = id_animal

    def get_id_animal(self):
        return self.__id_animal

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_command(self):
        return self.__command

    def add_command(self, new_commands):
        if self.__command == '' or self.__command == 'не обучено':
            self.__command = new_commands
        else:
            self.__command = self.__command + ', ' + new_commands

    def __str__(self):
        return f'{self.get_kind_animals()} {self.__name}\n{self.__birth_date}\nкоманды: {self.__command}'


class Donkeys(PackAnimals):
    def __init__(self, id_animal, name, birth_date, command):
        super().__init__(kind_animals="осел")
        self.__name = name
        self.__birth_date = birth_date
        self.__command = command
        self.__id_animal = id_animal

    def get_id_animal(self):
        return self.__id_animal

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_command(self):
        return self.__command

    def add_command(self, new_commands):
        if self.__command == '' or self.__command == 'не обучено':
            self.__command = new_commands
        else:
            self.__command = self.__command + ', ' + new_commands

    def __str__(self):
        return f'{self.get_kind_animals()} {self.__name}\n{self.__birth_date}\nкоманды: {self.__command}'