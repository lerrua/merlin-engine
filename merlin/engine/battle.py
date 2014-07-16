

class Prepare(object):
    """
    Prepare the champions for the battle!

    Usage:
        hero = Prepare(name="Aragorn", base_attack=100, base_hp=100)
    or like this:
        aragorn = {"name": "Aragorn", "base_attack": 100, "base_hp": 100}
        hero = Prepare(**aragorn)
    """
    def __init__(self, name, base_attack, base_hp):
        self.name = name
        self.base_attack = base_attack
        self.base_hp = base_hp

    @property
    def status(self):
        return self.__dict__

    def attack(self, foe):
        if not isinstance(foe, Prepare):
            raise TypeError('foe should be a Prepare object')

        if foe.base_hp <= 0:
            raise Exception('foe is already dead! Stop hit him!')

        foe.base_hp = foe.base_hp - self.base_attack

        if foe.base_hp <= 0:
            print 'foe is dead.'
        return foe.base_hp
