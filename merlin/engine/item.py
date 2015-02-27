from merlin import config
from merlin.engine.character import Monster

SHOW_MESSAGES = getattr(config, 'SHOW_MESSAGES', False)


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
