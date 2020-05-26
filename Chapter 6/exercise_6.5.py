rivers = {
    'nile': 'egypt',
    'yellow': 'china',
    'colorado': 'usa'
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}")

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)
    