from merlin import config
from merlin.engine.character import Monster
from merlin.exceptions import DeadException

SHOW_MESSAGES = getattr(config, 'SHOW_MESSAGES', False)


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

        if foe.is_dead:
            raise DeadException('foe is already dead! Stop hit him!')

        foe.base_hp = foe.base_hp - self.char.base_attack

        if foe.base_hp <= 0:
            foe.is_dead = True
            print 'foe is dead.' if SHOW_MESSAGES else None
        return foe.base_hp

    def collect(self, foe):
        if not isinstance(foe, Monster):
            raise TypeError('foe should be a Monster object')
        pass
