# create a class of Player to save number of games and score
from elo_calculator import difr
import datetime
import os
import json


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

    def player_to_file(self):
        """Save the player's attributes to a JSON file."""
        filename = f"{self.name}.json"
        filepath = os.path.join('players', filename)
        # check if the file already exists
        if os.path.exists(filepath):
            # prompt the user to overwrite the file or choose a new name
            while True:
                choice = input(f"A player with the name {self.name} already exists. "
                               f"Do you want to overwrite the file (O) or choose a new name (N)? ")
                if choice.lower() == 'o':
                    break
                elif choice.lower() == 'n':
                    self.name = input("Please enter a new name for the player: ")
                    filename = f"{self.name}.json"
                    filepath = os.path.join('players', filename)
                    if not os.path.exists(filepath):
                        break
                else:
                    print("Invalid choice. Please enter 'O' or 'N'.")

        # save the player's attributes to the file
        data = {'name': self.name, 'elo': self.elo, 'games': self.games,
                'k_factor': self.k_factor, 'last_played': str(self.last_played)}
        with open(filepath, 'w') as f:
            json.dump(data, f)
            print(f"Player {self.name} saved to file {filename}.")

    def player_from_file(self, name):
        """
        Loads a player's attributes from a JSON file.

        Args:
            name (str): The name of the player to load.

        Returns:
            None
        """
        filename = f"{name}.json"
        filepath = os.path.join('players', filename)

        if not os.path.exists(filepath):
            print(f"No player with the name {name} exists.")
            return

        with open(filepath, 'r') as f:
            data = json.load(f)

        self.name = data['name']
        self.elo = data['elo']
        self.games = data['games']
        self.k_factor = data['k_factor']
        self.last_played = datetime.datetime.strptime(data['last_played'], '%Y-%m-%d').date()

        print(f"Player {name} loaded from file {filename}.")

