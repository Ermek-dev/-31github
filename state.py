from abc import ABC,abstractmethod


class State(ABC):
    sep_temp = f'+{"":-^5}+{"":-^20}+{"":-^10}+{"":-^10}+{"":-^10}+{"":-^10}+'
    temp = '|{:^5}|{:^20}|{:^10}|{:^10}|{:^10}|{:^10}|'

    def __init__(self,name,age,satiety=0,mood=0,health=0):
        self.name = name
        self.age = age
        self.satiety = satiety
        self.mood = mood
        self.health = health
        self.animals = []
        self._animal = None


    def set_animal(self,animal):
        self.animal = animal


    @abstractmethod
    def add_animal(self):
        pass


    @abstractmethod
    def feed(self):
        pass


    @abstractmethod
    def play(self):
        pass


    @abstractmethod
    def heal(self):
        pass


    def print_animals(self):
        print(self.sep_temp)
        print(
            self.temp.format(
                '#', 'имя', 'возраст', 'здоровье',
                'настроение', 'сытость'
            )
        )
        print(self.sep_temp)
        print("%22s %10s %10s %10s %10s " % (self.name,self.age,self.health,self.mood,self.satiety))
        print(self.sep_temp)


    def _find_animal_by_name(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal


    def add_animal(self):
        name = input('Введите имя животного: ')
        if not self._find_animal_by_name(name):
            try:
                age = int(input('Введите возраст животного: '))
                if age > 18 or age < 1:
                    raise ValueError()
            except ValueError:
                print('Вы ввели некорректный возраст!')
                return
            self.animals.append(
                State(name=name, age=age)
            )
            self.print_animals()
        else:
            raise ValueError('Животное с подобным именем уже существует!')

    def feed(self):
        print("Вы покормили животное")
        self.satiety += 1
        self.mood += 1
        self.health += 1


    def play(self):
        print("Вы поиграли с животным")
        self.satiety -= 1
        self.mood += 1
        self.health += 1


    def heal(self):
        print("Вы полечили животное")
        self.mood += 1
        self.health += 1


c = State('mILK',18)
c.print_animals()
c.add_animal()



