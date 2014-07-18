Merlin Engine
=============
![merlin](/docs/merlin_728x270.png)

Merlin is a micro-engine written in Python for build RPG Games.

It's for fun, made to learn, search and improve my knowledge about create my own RPG engine, hope you like and help me improve it. 
The goal is keep using pure Python for be used everywhere, any lib, desktop or web application. 


### installation:

```
$ git clone git@github.com:lerrua/merlin-engine.git
$ cd merlin-engine
$ python setup.py install
```


### usage example:

Prepare opponents for the battle, basically are two dicts with attributes 'base_attack' and 'base_hp'.

```python
>>> from merlin.engine.battle import Prepare

# using sample heroes and monsters
>>> from merlin.fixtures import aragorn, orc

>>> hero = Prepare(aragorn)
>>> foe = Prepare(orc)

>>> foe.status
{'base_hp': 90, 'name': 'Orc', 'base_attack': 20, is_dead: False}

>>> hero.status
{'base_hp': 170, 'name': 'Aragorn', 'base_attack': 50, is_dead: False}
```

Here's a sample battle:
```python
>>> hero.attack(foe)
40
>>> foe.status
{'base_hp': 40, 'name': 'Orc', 'base_attack': 20, is_dead: False}

>>> hero.attack(foe)
foe is dead.
-10
>>> foe.status
{'base_hp': -10, 'name': 'Orc', 'base_attack': 20, is_dead: True}
```

We have some available actions after battle.
```python
>>> hero.attack(foe)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "merlin/engine/battle.py", line 22, in attack
    raise DeadException('foe is already dead! Stop hit him!')
DeadException: foe is already dead! Stop hit him!

# don't hit the dead body, collect the droppable items
>>> hero.collect(foe)
```
