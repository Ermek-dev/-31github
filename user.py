from cat import Cat




class User:
    separator_template = f'+{"":-^5}+{"":-^20}+{"":-^10}+{"":-^10}+{"":-^10}+{"":-^10}+{"":-^18}+'
    template = '|{:^5}|{:^20}|{:^10}|{:^10}|{:^10}|{:^10}|{:^18}|'
   
    def __init__(self) -> None:
        self.cats = []


    def add_cat(self):
        name = input("Enter name cat: ")
        try:
            age = int(input("Enter age cat: "))
            if age>18 or age < 1:
                raise ValueError()
        except ValueError:
            print("You entered incorrect age")
            return  
        self.cats.append(
            Cat(name=name,age=age),
        )
        self.show_cats()
        # self.cats.append(
        #     Cat(name='Jax',age=18),
        # )
        # self.cats.append(
        #     Cat(name='Nix',age=15)
        # )


    def show_cats(self):
        sorted_cats = sorted(self.cats,key=lambda item:item.avarage())
        print(self.separator_template)
        print(self.template.format(
            "#","имя","возраст","здоровье",
            "настроение","сытость","средний уровень"
            )
        )
        print(self.separator_template)
        for number,cat in enumerate(self.cats):
            name = f'* {cat.name}' if cat.is_used else cat.name
            print(self.template.format(
                number+1,name,cat.age,
                cat.health,cat.mood,cat.satiefy,
                int(cat.avarage())
                )
            )
            print(self.separator_template)
            # print(f"{number}|{cat.name}|{cat.age}|{cat.health}|{cat.mood}|{cat.satiety}|{cat.avarage()}")   


    def __get_action(self):
        return {
            'feed': self.feed,
            'play': self.play,
            'heal': self.heal,
            'sleep':self.sleep,
            'add': self.add
        }

    def choose_action(self):
        actions = self.__get_action()
        while True:
            command = input('Choose one of the action ' + ', '.join(actions.keys()) + '\n >')
            current_action = actions = actions.get(command, None)
            if current_action is not None:
                return current_action
            else:
                print('You entered incorrect command')

    def __find_cat(self):
        while True:
            cat_name = input("Enter the name cat \n > ")
            for cat in self.cats:
                if cat.name == cat_name:
                    return cat
                else:
                    print("No cat responsed")


    def feed(self):
        cat = self.__find_cat()
        is not cat.is_used:
            cat.change_values_after_sleep('mood', True)
            cat.change_values_after_sleep('health', True)
            cat.is_used = True
            print(f"You eat with cat {cat.name}")
        else:
            print('Already ate everything')


    def play(self):
        cat = self.__find_cat()
        is not cat.is_used:
            cat.change_values_after_sleep('mood', True)
            cat.change_values_after_sleep('health',True)
            cat.change_values_after_sleep('satiefy',False)
            cat.is_used = True
            print(f"You play with cat {cat.name}")

    def heal(self):
        cat = self.__find_cat()
        if not cat.is_used:
            cat.change_values_after_sleep('mood', False)
            cat.change_values_after_sleep('health', True)
            cat.change_values_after_sleep('satiefy', False)
            cat.is_used = True
             print(f"You taken to the vet with cat {cat.name}")
        else:
            print("Have you seen how much an abdominal ultrasound for a cat costs?")

    def sleep(self):
        for cat in self.cats:
            cat.change_values_after_sleep()
        self.show_cats()

