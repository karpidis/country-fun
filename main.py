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

    while country_list:
        sorted_countries = [country.name for country in sorted_list]
        print(sorted_countries)
        new_country = next_country(country_list)
        print(new_country.name + " with code " + new_country.code)
        pop_question = input(f"The {new_country.name} population is bigger or smaller than:? ")
        while not country_input(pop_question):
            pop_question = input(f"The {new_country.name} population is bigger or smaller than:? (ex: bigger than Greece)"
                                 f"or (ex: smaller than Gre)")
        katataxi, chora = country_input(pop_question)
        print(chora)
        if chora in sorted_countries:
            chora_pos = sorted_countries.index(chora)
            if katataxi == "bigger":
                if new_country.population > sorted_list[chora_pos].population:
                    if chora_pos == len(sorted_countries) - 1:
                        sorted_list.insert(chora_pos + 1, new_country)
                        sorted_countries.insert(chora_pos + 1, new_country.name)
                    else:
                        if new_country.population < sorted_list[chora_pos + 1].population:
                            sorted_list.insert(chora_pos +1, new_country)
                            sorted_countries.insert(chora_pos + 1, new_country.name)
                        else:
                            print("Wrong answer")
                            break
                else:
                    print("Wrong answer")
                    break
            elif katataxi == "smaller":
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
                            break
                else:
                    print("Wrong answer")
                    break
        else:
            print(f"{chora} is not in the sorted list. Please choose another country to compare.")
            continue

        print(pop_question)


if __name__ == '__main__':
    main()
