pet1 = {'name': 'mr.bubbles', "type":'dog', "owner" : 'joe'}
pet2 = {'name': 'spot', "type":'cat', "owner" : 'bob'}
pet3 = {'name': 'chester', "type":'horse', "owner" : 'chloe'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(pet['name'], pet['type'], pet['owner'])
