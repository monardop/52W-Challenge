from abc import ABC, abstractmethod
from random import randint


class Pokemon(ABC):
    def __init__(self, name, p_class):
        self.name = name
        self.p_class = p_class
        self. life = randint(100, 1000)
        self.power = randint(1, 100)
        self.defense = randint(1, 100)
        self.is_defending = False

    @abstractmethod
    def attack(self, victim):
        pass

    @abstractmethod
    def defend(self, attacker):
        pass

    @abstractmethod
    def counter(self, atk_def: bool, pkm_type: str) -> float:
        """
        Check for the combination, so it can return the booster
        :param atk_def: True for attack, False for defend
        :param pkm_type: pokemon type
        :return: The booster for the defense or attack
        """


class FirePokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Fire")

    def attack(self, victim: Pokemon):
        effectiveness = self.counter(True, victim.p_class)
        if victim.is_defending:
            pass
        else:
            return 50 * (self.power / self.defense) * effectiveness

    def defend(self, attacker):
        self.is_defending = True

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

    def attack(self, victim):
        pass

    def defend(self, attacker):
        pass

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

    def attack(self, victim):
        pass

    def defend(self, attacker):
        pass

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

    def attack(self, victim):
        pass

    def defend(self, attacker):
        self.is_defending = True

    def counter(self, atk_def: bool, pkm_type: str) -> float:
        pokemon_type = ('Fire', 'Water', 'Plant', 'Electricity')
        enemy: int = pokemon_type.index(pkm_type)
        attack = (1, 2, 0.5, 0.5)
        defense = (1, 1, 1, 0.5)
        if atk_def:
            return attack[enemy]
        else:
            return defense[enemy]
