from merlin.engine.battle import Prepare
from merlin.engine.item import Item


class Character(object):
    def __init__(self, name, base_attack, base_hp):
        self.name = name
        self.base_attack = base_attack
        self.base_hp = base_hp
        self.is_dead = False
        self.battle = Prepare(self)
        self.item = Item(self)

    @property
    def status(self):
        return self.__dict__


class Hero(Character):
    pass


class Monster(Character):
    pass
