travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany':['Stuttgart', 'Berlin']
}

print(travel_log['France'][1])

nested_list = ['A','B', ['C','D']]
print(nested_list[2][1])# first [2] access the second ['C''D'] and the seconde [1] access the letter D

travel_log = {
    'France':{
        'num_times_viseted': 8,
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
    },
    'Germany': {
        'cities_visited':['Stuttgart', 'Berlin'],
        'num_times_visisted': 12
    },
}

print(travel_log['Germany']['cities_visited'][0]) # to access through the multiple dictionaries and lists