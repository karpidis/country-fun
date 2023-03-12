import os
from country import Country
from country_list import un_members_dict
from take_input import country_input


def wrong_answer(new_country, sorted_by, wrong_guesses, sorted_country_list):
    print("Wrong guess.")
    wrong_guesses += 1
    print(f'{new_country.name} {sorted_by} is {getattr(new_country, sorted_by)}')
    sorted_country_list.append(new_country)  # add the country to the list of objects countries
    sorted_country_list.sort(key=lambda country: getattr(country, sorted_by))  # sort the list of objects countries
    return wrong_guesses, sorted_country_list


def country_sort_game(sorted_country_list, haraktiristiko, country_list_str):
    """ This is the main function of the game. It takes input from the user and checks if the input is correct."""
    wrong_guesses = 0
    while country_list_str:
        # this while loop is for the case that the user has less than 3 wrong guesses
        if wrong_guesses == 3:
            sorted_country_list = [country.name for country in sorted_country_list]
            print(sorted_country_list)  # final print of the countries that have been played.
            print(f"You guessed {len(sorted_country_list) - 3} countries correctly. You lost")
            break
        sorted_countries = [country.name for country in sorted_country_list]  # list of str with played countries
        print(sorted_countries)
        # The country that the user has to guess the popul, area or density
        new_country = next_country(country_list_str)
        print(new_country.name + " with code " + new_country.code)
        # This while loop is for the case that the user has less than 3 wrong guesses
        while wrong_guesses < 3:
            pop_question = input(f"The {new_country.name} {haraktiristiko} is bigger or smaller than:? ")
            if not country_input(pop_question):
                print("Invalid input. Please try again.")
            else:
                katataxi, chora = country_input(pop_question)
                katataxi = katataxi.title()
                chora = chora.title()
                if chora not in sorted_countries:
                    print(f"{chora} is not in the sorted list. Please choose another country to compare.")
                else:
                    chora_pos = sorted_countries.index(chora)
                    if katataxi == "Bigger":
                        """check if chosen country is bigger"""
                        if getattr(new_country, haraktiristiko) > \
                                getattr(sorted_country_list[chora_pos], haraktiristiko):
                            if chora_pos == len(sorted_countries) - 1:
                                # insert the new country in the list  of objects countries
                                sorted_country_list.insert(chora_pos + 1, new_country)
                                # insert the new country in the list of str countries
                                sorted_countries.insert(chora_pos + 1, new_country.name)
                            else:
                                if getattr(new_country, haraktiristiko) < \
                                        getattr(sorted_country_list[chora_pos + 1], haraktiristiko):
                                    # insert the new country in the list  of objects countries
                                    sorted_country_list.insert(chora_pos + 1, new_country)
                                    # insert the new country in the list of str countries
                                    sorted_countries.insert(chora_pos + 1, new_country.name)
                                else:
                                    wrong_guesses, sorted_country_list = \
                                        wrong_answer(new_country, haraktiristiko, wrong_guesses, sorted_country_list)
                                    break
                        else:
                            wrong_guesses, sorted_country_list = \
                                wrong_answer(new_country, haraktiristiko, wrong_guesses, sorted_country_list)
                            break
                    elif katataxi == "Smaller":
                        """check if chosen country is smaller"""
                        if getattr(new_country, haraktiristiko) < \
                                getattr(sorted_country_list[chora_pos], haraktiristiko):
                            if chora_pos == 0:
                                # insert the new country in the list  of objects countries
                                sorted_country_list.insert(chora_pos, new_country)
                                # insert the new country in the list of str countries
                                sorted_countries.insert(chora_pos, new_country.name)
                            else:
                                if getattr(new_country, haraktiristiko) > \
                                        getattr(sorted_country_list[chora_pos - 1], haraktiristiko):
                                    # insert the new country in the list  of objects countries
                                    sorted_country_list.insert(chora_pos, new_country)
                                    # insert the new country in the list of str countries
                                    sorted_countries.insert(chora_pos, new_country.name)
                                else:
                                    wrong_guesses, sorted_country_list = \
                                        wrong_answer(new_country, haraktiristiko, wrong_guesses, sorted_country_list)
                                    break
                        else:
                            wrong_guesses, sorted_country_list = \
                                wrong_answer(new_country, haraktiristiko, wrong_guesses, sorted_country_list)
                            break
                    print(pop_question)
                    break


def what_we_compare():
    """Returns a string of what we compare
    """
    choices = {"1": "Population",
               "2": "Area",
               "3": "People per km²"
               }
    characteristic = {"1": "population",
                      "2": "area",
                      "3": "density"
                      }
    print("You can play for: ")
    for key, value in choices.items():
        print(key + "." + value)
    while True:
        choice = input("What is your choice?", )
        if choice in choices:
            return characteristic[choice]
        else:
            print('Invalid choice. Please try again')


def next_country(list_of_countries: list):
    if list_of_countries:
        first = list_of_countries.pop()
        filepath = os.path.join(os.path.dirname(__file__), 'countries')
        filename = filepath + '/' + un_members_dict[first] + '.json'
        country = Country.from_json(filename)
        return country
    if not list_of_countries:
        return None
