def city_formatter(city, country, population=''):
    if population:
        formatted = f"{city.title()}, {country.title()} - Population: {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted
