cities = ['vancouver', 'beijing', 'tokyo', 'london', 'new york']
cities.sort(reverse= True)
print(cities)
print("Bye bye,", cities.pop(1), "!")
del cities[1]
cities.remove('beijing')
print(cities)
cities.insert(0, 'toronto')
cities.append('osaka')
print(cities)
print(sorted(cities))
print(cities[3])