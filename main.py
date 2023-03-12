import random
from country_list import un_members
import player
from game_logic import country_sort_game, what_we_compare, next_country


def main():
    country_list = un_members  # list of string countries
    random.shuffle(country_list)
    starting_country = next_country(country_list)  # Country object
    players = player.get_number_names_of_players()
    sorted_by = what_we_compare()
    print(starting_country.name+f" with {sorted_by} of " + str(getattr(starting_country, sorted_by)) +
          " and code "+starting_country.code)
    sorted_list = [starting_country]  # list of Country objects

    # elo system implementation
    country_sort_game(sorted_list, sorted_by, country_list)


if __name__ == '__main__':
    main()
