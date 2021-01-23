travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(new_country, number_visited, city_visited):
    #Primera manera
    next_country={"country": new_country,
                  "visits": number_visited,
                  "cities": city_visited}
    '''
    Segunda manera:

    next_country = {}
    next_country["country"] = new_country
    next_country["visits"] = number_visited
    next_country["cities"] = city_visited
    '''
    travel_log.append(next_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
