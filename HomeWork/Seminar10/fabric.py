'''Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
'''

from animals import Bird
from animals import Fish
from animals import Mammal


class AnimalFabric():
    def __init__(self, animal_type: str, name: str, uniq: int):
        self.animal_type = animal_type
        self.name = name
        self.unique_param = uniq

    def unique(self):
        pass

    def creating_animal(self):
        if self.animal_type == 'Bird':
            return Bird(self.name, self.unique_param)
        elif self.animal_type == 'Fish':
            return Fish(self.name, self.unique_param)
        elif self.animal_type == 'Mammal':
            return Mammal(self.name, self.unique_param)


if __name__ == '__main__':
    animal1 = AnimalFabric('Bird', 'Ласточка', 20).creating_animal()
    animal2 = AnimalFabric('Fish', 'Окунь', 40).creating_animal()
    animal3 = AnimalFabric('Mammal', 'Лиса', 30).creating_animal()

    print(animal1.unique())
    print(animal2.unique())
    print(animal3.unique())