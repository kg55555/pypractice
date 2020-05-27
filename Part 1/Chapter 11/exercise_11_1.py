def city_formatter(city, country):
    formatted = f"{city.title()}, {country.title()}"
    return formatted

print(city_formatter('hello', 'world'))