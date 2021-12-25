#Working with python dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

#print dictionary value
print(programming_dictionary["Bug"])

#add new value to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#create an empty dictionary
empty_dictionary = {}

#edit value
programming_dictionary["Bug"] = "This is bug."
print(programming_dictionary)

#loop through the dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

#wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)


#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]