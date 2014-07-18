class Character(object):
    def __init__(self, name, base_attack, base_hp):
        self.name = name
        self.base_attack = base_attack
        self.base_hp = base_hp
        self.is_dead = False

    @property
    def status(self):
        return self.__dict__


class Hero(Character):
    pass


class Monster(Character):
    pass
