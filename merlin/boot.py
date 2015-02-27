import yaml

from merlin.configs import PATH
from merlin.engine import Monster, Hero


def loaddb(stream):
    heroes = []
    monsters = []

    heroes.append(Hero(**stream['heroes']))
    monsters.append(Monster(**stream['monsters']))

    return heroes, monsters

stream = open(PATH + "/fixtures.yml", 'r')
fixtures = loaddb(yaml.load(stream))

heroes = fixtures[0]
monsters = fixtures[1]
