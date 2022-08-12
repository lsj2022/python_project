#6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
#Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people. Loop through your list of people. As you
#loop through the list, print everything you know about each person.

person = {'first_name': 'Thomas', 'last_name':'Abraham', 'age': '30', 'city':'sterling'}
person_1 = {'first_name': 'Lis', 'last_name': 'James', 'age': '27', 'city': 'richmond'}
person_2 = {'first_name': 'James','last_name':'David', 'age': '62', 'city':'charlottesville'}

peoples = [person, person_1, person_2]

for values in peoples:
    name= values["first_name"] +" " + values["last_name"]
    age = values['age']
    city = values['city']
    print(f"My name is {name}, I am {age} years old. I am from {city}. ")


#6-8. Pets: Make several dictionaries, where each dictionary represents a different
#pet. In each dictionary, include the kind of animal and the owner’s name.
#Store these dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet.

pet_1= {
    'owner_name': 'Lis',
    'animals_name': 'rocky',
    'animal_type': 'dog'
}
pet_2 = {
    'owner_name': 'Thomas',
    'animals_name': 'beepboop',
    'animal_type': 'cat'
}
pet_3 = {
    'owner_name':'Lissu',
    'animals_name':'browny',
    'animal_type': 'dog'

}

pets = [pet_1, pet_2, pet_3]

for animals in pets:
    name = animals['owner_name']
    animal = animals['animals_name']
    type = animals['animal_type']
    print(f"\nMy name is {name}, I own a {type}. His name is {animal}.")


#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
##names to use as keys in the dictionary, and store one to three favorite places
#for each person. To make this exercise a bit more interesting, ask some friends
#to name a few of their favorite places. Loop through the dictionary, and print
#each person’s name and their favorite places.


favorite_place = {
    'Lis': 'greece',
    'Thomas': 'D.C',
    'Renny': 'Paris',
    'Lissu': 'New york'
}


for name, place in favorite_place.items():
    print(f"{name}'s favorite place to travel is {place.title()}.")