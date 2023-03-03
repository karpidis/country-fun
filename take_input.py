import re

country_game_re = re.compile(r'^(bigger|smaller) than\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)$', re.IGNORECASE)

def country_input(c_input):
    """Returns a tuple of (comparison, country) if the input is valid, otherwise returns False
    >>> country_input('bigger than Greece')
    ('bigger', 'Greece')
    >>> country_input('smaller than Greece')
    ('smaller', 'Greece')
    >>> country_input('Japan is bigger than Greece')
    False
    >>> country_input('Japan is beautiful')
    False
    >>> country_input("Is Portugal bigger than Spain?")
    False
    >>> country_input("Smaller than the largest continent on earth")
    False
    """
    match = re.match(country_game_re, c_input)
    if match:
        comparison,country = match.groups()
        return comparison, country
    else:
        return False