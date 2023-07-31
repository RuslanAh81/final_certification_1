from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def set_presenter(self, presenter):
        """

        :param presenter:
        :return:
        """

    @abstractmethod
    def start(self):
        """

        """