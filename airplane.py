from transport import Transport


class AirPlane(Transport):

    def move(self):
        print("Раскручиваем пропеллер и летим")

    def repair(self):
        print("Выгоняем в ангар и чиним")

    def clean(self):
        print("Самолет заезжает в ангар мойку")

    @property
    def name(self):
        return "Tu-144a"
