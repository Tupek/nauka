def message(dict):
    if dict.get("movie" or "name" or "role"):
        desc = "In %(movie)s, %(name)s is a %(role)s." % dict
        return desc

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}
#input_dict = {
#    "name": "Bilbo Baggins",
#    "role": "burglar"
#}

print(message(input_dict))