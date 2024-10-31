capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "Lillie", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print lillie

# print(travel_log["France"][1])

# double nested list
nested_list = ["A", "B", ["C", "D"]]

# print "D"
print(nested_list[2][1])

# print stuttgart
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])