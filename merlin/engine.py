from merlin import configs
from merlin.exceptions import DeadException

SHOW_MESSAGES = getattr(configs, 'SHOW_MESSAGES', False)


class Character(object):
    def __init__(self, name, base_attack, base_hp, extra={}):
        self.name = name
        self.base_attack = base_attack
        self.base_hp = base_hp
        self.is_dead = False
        self.battle = Prepare(self)
        self.extra = extra
        self.item = Item(self)

    @property
    def status(self):
        return self.__dict__


class Hero(Character):
    pass


class Monster(Character):
    pass


class Item(object):
    def __init__(self, character):
        self.char = character

    def collect(self, foe):
        if not isinstance(foe, Monster):
            raise TypeError('foe should be a Monster object')
        if not foe.is_dead:
            print 'unable to collect item.' if SHOW_MESSAGES else None
            raise Exception('unable to collect item')

    def use(self):
        pass

    def drop(self):
        pass

    def trade(self, character):
        pass


class Prepare(object):
    """
        Prepare the champions for the battle!
    """
    def __init__(self, character):
        self.char = character

    @property
    def status(self):
        return self.char.status

    def set_damage(self, attack):
        return attack

    def attack(self, foe):
        if not isinstance(foe, Monster):
            raise TypeError('foe should be a Monster object')

        if foe.is_dead:
            raise DeadException('foe is already dead! Stop hit him!')

        foe.base_hp = foe.base_hp - self.set_damage(self.char.base_attack)

        if foe.base_hp <= 0:
            foe.is_dead = True
            print 'foe is dead.' if SHOW_MESSAGES else None
        return foe.base_hp
