from abc import ABC, abstractmethod
from random import randint


class Pokemon(ABC):
    def __init__(self, name, p_class):
        self.name = name
        self.p_class = p_class
        self. life = randint(100, 1000)
        self.power = randint(1, 100)
        self.defense = randint(1, 100)
        self.is_defending = 1

    def attack(self, victim):
        effectiveness = self.counter(True, victim.p_class)
        damage = 50 * (self.power / self.defense) * effectiveness
        return damage * self.is_defending

    def defend(self, attacker):
        effectiveness = self.counter(False, attacker.p_class)
        if effectiveness == 0.5:
            self.is_defending = 0.75
        elif effectiveness == 1:
            self.is_defending = 0.50
        else:
            self.is_defending = 0.25

    @abstractmethod
    def counter(self, atk_def: bool, pkm_type: str) -> float:
        """
        Check for the combination, so it can return the booster
        :param atk_def: True for attack, False for defend
        :param pkm_type: Pokemon type
        :return: The booster for the defense or attack
        """


class FirePokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Fire")

    def counter(self, atk_def: bool, pkm_type: str) -> float:
        pokemon_type = ('Fire', 'Water', 'Plant', 'Electricity')
        enemy: int = pokemon_type.index(pkm_type)
        attack = (0.5, 0.5, 2, 1)
        defense = (0.5, 2, 0.5, 1)
        if atk_def:
            return attack[enemy]
        else:
            return defense[enemy]


class WaterPokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Water")

    def counter(self, atk_def: bool, pkm_type: str) -> float:
        pokemon_type = ('Fire', 'Water', 'Plant', 'Electricity')
        enemy: int = pokemon_type.index(pkm_type)
        attack = (2, 0.5, 0.5, 1)
        defense = (0.5, 0.5, 2, 2)
        if atk_def:
            return attack[enemy]
        else:
            return defense[enemy]


class PlantPokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Plant")

    def counter(self, atk_def: bool, pkm_type: str) -> float:
        pokemon_type = ('Fire', 'Water', 'Plant', 'Electricity')
        enemy: int = pokemon_type.index(pkm_type)
        attack = (2, 0.5, 0.5, 0.5)
        defense = (0.5, 2, 0.5, 1)
        if atk_def:
            return attack[enemy]
        else:
            return defense[enemy]


class ElectricPokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Electric")

    def counter(self, atk_def: bool, pkm_type: str) -> float:
        pokemon_type = ('Fire', 'Water', 'Plant', 'Electricity')
        enemy: int = pokemon_type.index(pkm_type)
        attack = (1, 2, 0.5, 0.5)
        defense = (1, 1, 1, 0.5)
        if atk_def:
            return attack[enemy]
        else:
            return defense[enemy]
