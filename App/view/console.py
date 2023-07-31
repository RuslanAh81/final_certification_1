from datetime import datetime

from view.abstract_view import View
from view.counter import Counter

class Console(View):
    __working = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def start(self):
        self.__working = True
        read_db = self.presenter.read_db()
        if read_db == "Успешно":
            while self.__working:
                print('\n\t====Главное меню=====')
                print('\t1. Открыть реестр животных\n'
                      '\t2. Добавить животное в питомник\n'
                      '\t3. Выбрать животное для просмотра и добавления команд\n'
                      '\t4. Выход\n')
                user_choice = self.__get_number(4, 'Выберите пункт меню: ')
                match user_choice:
                    case "1":
                        print("\n\t\t Реестр животных питомника")
                        print(self.presenter.get_tabl_registry())
                    case "2":
                        self.__add_animals()
                    case "3":
                        self.__show_add_command()
                    case "4":
                        self.__working = False
        else:
            print(read_db)


    def __add_animal(self, type_id, kinds):
        print(f'\n Виды животных в питомнике: {kinds}\n')
        kind = input('Введите вид животного: ').lower()
        if kind in kinds:
            name = input('Введите имя животного: ').capitalize()
            command = input('Введите список команд через запятую, которым обучено животное.Или введите "не обучено": ')
            birth_date = self.__get_date('Введите дату рождения животного в формате ГГГ-ММ-ДД: ')
            if self.__save_animal(kind, name, command, birth_date):
                self.presenter.add_animal(kind, name, command, birth_date)
                print(self.presenter.save_animal_into_bd(type_id, kind, name, command, birth_date))
        else:
            print("\nТакого вида в настоящий момент нет в питомнике Обратитесь к администратору.")
            return

    def __add_animals(self):
        print('\n======= Типы животных в питомнике ======')
        print('\t1. Домашние животные\n'
              '\t2. Вьючные животные\n'
              '\t3. Выход')
        user_choice = self.__get_number(3, "Выберите пункт в меню: ")
        match user_choice:
            case "1":
                self.__add_animal(user_choice, self.presenter.all_kinds_pets())
            case "2":
                self.__add_animal(user_choice, self.presenter.all_kinds_pack())
            case "3":
                return

    @staticmethod
    def __get_number(size: int, text: str):
        while True:
            user_input = input(text)
            if (user_input.isdigit() and 1<= int(user_input) <= size):
                return user_input
            print(f'\nВведите число от 1 до {size}')


    @staticmethod
    def __save_animal(kind, name, command, birth_date):
        print(f'\nВы хотите добавить животное:\n{kind} {name}\nкоманды: {command}\n д.р {birth_date}')
        user_choice = input('Сохранить изменения?(Да/Нет): ').lower()
        if user_choice in ['да', 'д', 'y', 'yes']:
            with Counter() as counter:
                if name != '' and command != '' and birth_date !='':
                    counter.add()
                    print(f"Значение счетчика: {counter.count}")
                else:
                    raise Exception('Данные некорректны! Заполнены не все значения.')
            return True
        else:
            print('\nЗапись не сохранена.\n')
            return False

    @staticmethod
    def __get_date(text):
        while True:
            user_input = input(text)
            if user_input:
                try:
                    datetime.strptime(user_input, "%Y-%m-%d")
                    return user_input
                except ValueError:
                    print("Неверный формат даты")
            return user_input

    def __show_add_command(self):
        print("\n\tДля просмотра и добавления команд необходимо ввести номер животного в реестре"
              "(ID животного). Если вы не знаете ID животного, введите 2 и в главном меню выберите 1"
              "для просмотра реестра животных.\n")
        print('\n\t====== Меню ======')
        print('\t1. Ввести номер животного для проссмотра или добавления команд\n'
              '\t2. Выход\n')
        user_choice = self.__get_number(2, "Выберите пункт меню: ")
        match user_choice:
            case "1":
                user_input = self.__get_number(self.presenter.sise_registry(), "Введите ID животного")
                index = int(user_input)-1
                self.__add_command(index)
            case "2":
                return

    def __add_command(self, index):
        print()
        print(self.presenter.find_animal(index))
        print(f'\nСписок команд: {self.presenter.get_command(index)}\n')
        user_answer = input('Добавить команду? (Да/Нет): ')
        if user_answer in ['да', 'д', 'y', 'yes']:
            commands = input('Введите команды через запятую: ')
            self.presenter.add_command(index, commands)
            print(self.presenter.save_command(index))
        else:
            print('Операция отклонена')
            return

