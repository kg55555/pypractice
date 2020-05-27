tokyo = {'country': 'japan', 'population': 12338734, 'fact': 'Tokyo is beautiful!'}
vancouver = {'country': 'canada', 'population': 4829453, 'fact': 'Vancouver is cold!'}
new_york = {'country': 'usa', 'population': 7943854, 'fact': 'New York is busy!'}

cities = {'tokyo': tokyo, 'vancouver': vancouver, "new york": new_york}

for city, info in cities.items():
    print(f"{city.title()} is located in the country of {info['country']}, and has a population of {info['population']}. A fun fact is that {info['fact']}")
