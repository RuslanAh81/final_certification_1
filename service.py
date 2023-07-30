from data.dbmysql_manager import MySqlManager
from model.registry_animals import RegistryAnimals
from presenter.presenter import Presenter
from view.console import Console


class Service:
    def __init__(self):
        self.registry = RegistryAnimals()
        self.view = Console()
        self.data = MySqlManager('human_friends.db')
        Presenter(self.view, self.registry, self.data)

    def start(self):
        print("я тут сервис")
        self.view.start()