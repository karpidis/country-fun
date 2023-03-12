from elo_calculator import difr
import json


class Country:
    def __init__(self, name, code, continent, population, area, elo=1500):
        self.name = name
        self.code = code
        self.continent = continent
        self.population = int(population)
        self.area = area
        self.elo = elo

    def __str__(self):
        return self.name

    def update_elo(self, opponent_elo, guess_result):
        actual_score = 0 if guess_result == 'win' else 1
        elo_change = difr(self.elo, opponent_elo, actual_score, 20)
        self.elo += elo_change

    @classmethod
    def from_json(cls, filename):
        with open(filename) as f:
            data = json.load(f)
        return cls(**data)

    @staticmethod
    def pop_area(area, population):
        return area / population
