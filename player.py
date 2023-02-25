# create a class of Player to save number of games and score
from elo_calculator import difr
import datetime
class Player:
    """I create a player that will have a rating, name and number of games"""

    def __init__(self, name, elo=1500, games=0, k_factor=40, last_played=datetime.date(2023, 1, 1)):
        self.name = name
        self.elo = elo
        self.games = games
        self.k_factor = k_factor
        self.last_played = last_played

    def add_game(self):
        self.games += 1

    def update_elo(self, opponent_elo, guess_result):
        """
        Updates the player's ELO score based on the result of a guess against a country.

        Args:
            opponent_elo (int): The ELO score of the country being guessed.
            guess_result (str): A string indicating the result of the guess, either "win" or "loss".

        Returns:
            None
        """
        if guess_result == 'win':
            actual_score = 1
        else:
            actual_score = 0
        # calculate ELO change using difr function
        elo_change = difr(self.elo, opponent_elo, actual_score, self.k_factor)
        self.elo += elo_change  # update ELO score

    def update_k_factor(self):
        """
        Updates the player's K factor based on the number of games played and the time since their last game.

        If the player has played 20 or more games, their K factor is set to 20. If the player has not played for
        more than 2 months, their K factor is set back to the default value of 40.

        """
        today = datetime.date.today()
        if self.games >= 20 & (today - self.last_played).days <= 60:
            self.k_factor = 20
        else:
            self.k_factor = 40

    def update_last_played(self):
        """
        Updates the player's last_played attribute to the current date.
        """
        self.last_played = datetime.date.today()
