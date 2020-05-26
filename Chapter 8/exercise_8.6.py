def city_country(city, country):
    cc = city.title() + ", " + country.title()
    return cc

print(city_country("vancouver", "canada"))
print(city_country("beijing", "china"))
print(city_country("new york", "usa"))