"""
 * Reto #35
 * BATALLA POKÉMON
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
"""
from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name, p_class):
        self.name = name
        self.p_class = p_class
        self. life = 100

    @abstractmethod
    def attack(self, victim):
        pass

    @abstractmethod
    def defend(self, attacker):
        pass


class FirePokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Fire")

    def attack(self, victim):
        pass

    def defend(self, attacker):
        pass


class WaterPokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Water")

    def attack(self, victim):
        pass

    def defend(self, attacker):
        pass


class PlantPokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Plant")

    def attack(self, victim):
        pass

    def defend(self, attacker):
        pass


class ElectricPokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Electric")

    def attack(self, victim):
        pass

    def defend(self, attacker):
        pass
