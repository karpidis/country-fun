from elo_calculator import difr
class Country:
    def __init__(self, name, code, continent, population, area):
        self.name = name
        self.code = code
        self.code = continent
        self.population = population
        self.area = area
        # self.capital = capital
        # self.phone_code = phone_code
        self.elo = 1500 #initial elo

    def update_elo(self, opponent_elo, guess_result):
        """
        Updates the country's ELO score based on the result of a guess by a player.

        Args:
            opponent_elo (int): The ELO score of the player making the guess.
            guess_result (str): A string indicating the result of the guess, either "win" or "loss".

        Returns:
            None
        """
        if guess_result == 'win':
            actual_score = 1
        else:
            actual_score = 0
        # calculate ELO change using difr function with k_factor 20
        elo_change = difr(self.elo, opponent_elo, actual_score, 20)
        self.elo += elo_change  # update ELO score

