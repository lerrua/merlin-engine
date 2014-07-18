from merlin.engine.character import Monster
from merlin.exceptions import DeadException


class Prepare(object):
    """
        Prepare the champions for the battle!
    """
    def __init__(self, character):
        self.char = character

    @property
    def status(self):
        return self.char.status

    def attack(self, foe):
        if not isinstance(foe, Monster):
            raise TypeError('foe should be a Monster object')

        if foe.base_hp <= 0:
            raise DeadException('foe is already dead! Stop hit him!')

        foe.base_hp = foe.base_hp - self.char.base_attack

        if foe.base_hp <= 0:
            print 'foe is dead.'
        return foe.base_hp

    def collect(self, foe):
        if not isinstance(foe, Monster):
            raise TypeError('foe should be a Monster object')
        pass
