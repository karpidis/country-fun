import random
from country_list import un_members, un_members_dict
import os
from country import Country
from take_input import country_input


def what_we_compare():
    choices = {"1": "Population",
               "2": "Area",
               "3": "People per km²"
               }
    print("You can play for: ")
    for key, value in choices:
        print(key + "." + value)
    while True:
        choice = input("What is your choice?", )
        if choice in choices:
            return choices[choice]
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


def main():
    country_list = un_members
    random.shuffle(country_list)
    starting_country = next_country(country_list)
    print(starting_country.name+" with population of "+str(starting_country.population) +
          " and code "+starting_country.code)
    sorted_list = [starting_country]
    wrong_guesses = 0
    while country_list:
        if wrong_guesses == 3:
            print("You lost")
            break
        sorted_countries = [country.name for country in sorted_list]
        print(sorted_countries)
        new_country = next_country(country_list)
        print(new_country.name + " with code " + new_country.code)

        while wrong_guesses < 3:
            pop_question = input(f"The {new_country.name} population is bigger or smaller than:? ")
            if not country_input(pop_question):
                print("Invalid input. Please try again.")
            else:
                katataxi, chora = country_input(pop_question)
                katataxi = katataxi.capitalize()
                chora = chora.capitalize()
                if chora not in sorted_countries:
                    print(f"{chora} is not in the sorted list. Please choose another country to compare.")
                else:
                    chora_pos = sorted_countries.index(chora)
                    if katataxi == "Bigger":
                        if new_country.population > sorted_list[chora_pos].population:
                            if chora_pos == len(sorted_countries) - 1:
                                sorted_list.insert(chora_pos + 1, new_country)
                                sorted_countries.insert(chora_pos + 1, new_country.name)
                            else:
                                if new_country.population < sorted_list[chora_pos + 1].population:
                                    sorted_list.insert(chora_pos + 1, new_country)
                                    sorted_countries.insert(chora_pos + 1, new_country.name)
                                else:
                                    print("Wrong answer")
                                    wrong_guesses += 1
                                    print(f'{new_country.name} population is {new_country.population} ')
                                    sorted_list.append(new_country)
                                    sorted_list.sort(key=lambda country: country.population)
                                    break
                        else:
                            print("Wrong answer")
                            wrong_guesses += 1
                            print(f'{new_country.name} population is {new_country.population} ')
                            sorted_list.append(new_country)
                            sorted_list.sort(key=lambda country: country.population)
                            break
                    elif katataxi == "Smaller":
                        if new_country.population < sorted_list[chora_pos].population:
                            if chora_pos == 0:
                                sorted_list.insert(chora_pos, new_country)
                                sorted_countries.insert(chora_pos, new_country.name)
                            else:
                                if new_country.population > sorted_list[chora_pos - 1].population:
                                    sorted_list.insert(chora_pos, new_country)
                                    sorted_countries.insert(chora_pos, new_country.name)
                                else:
                                    print("Wrong answer")
                                    wrong_guesses += 1
                                    print(f'{new_country.name} population is {new_country.population} ')
                                    sorted_list.append(new_country)
                                    sorted_list.sort(key=lambda country: country.population)
                                    break
                        else:
                            print("Wrong answer")
                            wrong_guesses += 1
                            print(f'{new_country.name} population is {new_country.population} ')
                            sorted_list.append(new_country)
                            sorted_list.sort(key=lambda country: country.population)
                            break
                    print(pop_question)
                    break


if __name__ == '__main__':
    main()
