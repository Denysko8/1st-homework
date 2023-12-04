from enum import Enum


class PlanetType(Enum):
    TERRESTRIAL = 1
    JOVIAN = 2


class Planet():
    def __init__(self, name, mass, orbital_velocity, mean_temperature, length_of_day, distance_from_sun, planet_type):
        self.name = name
        self.mass = mass
        self.orbital_velocity = orbital_velocity
        self.mean_temperature = mean_temperature
        self.length_of_day = length_of_day
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type


class Planetary():
    def __init__(self):
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def sort_by_length_of_day(self):
        self.planets.sort(key=lambda planet: planet.length_of_day)

    def find_distance_between_plantes(self, planetA, planetB):
        distance_between = abs(planetA.distance_from_sun - planetB.distance_from_sun)
        return distance_between

    def find_average_mass_of_planets(self):
        total_mass = sum(planet.mass for planet in self.planets)
        average_mass = total_mass / len(self.planets)
        return average_mass


planet_1 = Planet('Orbit', 150e14, '500 m/s', 3456, 15, 79e56, PlanetType.TERRESTRIAL)
planet_2 = Planet('Dirol', 160e13, '100 m/s', 12999, 5, 80e90, PlanetType.JOVIAN)
planet_3 = Planet('BubleGum', 100e13, '10 m/s', 1100, 8, 70e90, PlanetType.JOVIAN)

planetary_system = Planetary()
planetary_system.add_planet(planet_1)
planetary_system.add_planet(planet_2)
planetary_system.add_planet(planet_3)

planetary_system.sort_by_lenght_of_day()
sorted_planets = [[planet.name, planet.length_of_day] for planet in planetary_system.planets]
print(f"List of sorted planets by their length of day {sorted_planets}\n")

distance_between_planets = planetary_system.findDistanceBetween(planet_1, planet_3)
print(f"Distance between {planet_1.name} and {planet_3.name} is {distance_between_planets}\n")

average_mass = planetary_system.findAverageMass()
print(f"Average mass of the planets equal {average_mass}")
