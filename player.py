# create a class of Player to save number of games and score
# create a function to get number of players and names of players
from elo_calculator import difr
import datetime
import os
import json


def get_number_names_of_players():
    """Returns the number of players in the players' directory."""
    number_of_players = None
    while type(number_of_players) != int:
        try:
            number_of_players = int(input("How many players are there? "))
        except ValueError:
            print("Please enter a number.")
    players: list[Player] = []
    for i in range(number_of_players):
        player_name = input("Enter the name of player {}: ".format(i + 1))
        player = Player.from_file(player_name)
        players.append(player)
    return players


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
        Updates the player's K-factor based on the number of games played and the time since their last game.

        If the player has played 20 or more games, their K-factor is set to 20. If the player has not played for
        more than 2 months, their K-factor is set back to the default value of 40.

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

    def to_file(self):
        """Saves the player's attributes to a JSON file."""
        filename = f"{self.name}.json"
        filepath = os.path.join('players', filename)
        data = {'name': self.name, 'elo': self.elo, 'games': self.games,
                'k_factor': self.k_factor, 'last_played': str(self.last_played)}
        with open(filepath, 'w') as f:
            json.dump(data, f)
            print(f"Player {self.name} saved to file {filename}.")

    @classmethod
    def from_file(cls, name):
        """
        Loads a player's attributes from a JSON file or creates a new player object.

        Args:
            name (str): The name of the player.

        Returns:
            A new Player object.
        """
        filename = f"{name}.json"
        filepath = os.path.join('players', filename)

        if os.path.exists(filepath):
            while True:
                choice = input(f"A player with the name {name} already exists. "
                               f"Do you want to load the existing player (L) or create a new one with a different name"
                               f" (N)? ")
                if choice.lower() == 'l':
                    with open(filepath, 'r') as f:
                        data = json.load(f)

                    return cls(name=data['name'], elo=data['elo'], games=data['games'],
                               k_factor=data['k_factor'],
                               last_played=datetime.datetime.strptime(data['last_played'], '%Y-%m-%d').date())
                elif choice.lower() == 'n':
                    while True:
                        new_name = input("Please enter a new name for the player: ")
                        new_filename = f"{new_name}.json"
                        new_filepath = os.path.join('players', new_filename)
                        if not os.path.exists(new_filepath):
                            break
                        print("A player with that name already exists.")
                    return cls(name=new_name)
                else:
                    print("Invalid choice. Please enter 'L' or 'N'.")
        else:
            return cls(name=name)
