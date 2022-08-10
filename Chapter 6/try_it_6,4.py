# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.



glossary = {
        'integer':'whole number',
        'string':'characters',
        'for_loop': 'loops',
        'if_statement':'validation',
        'elif':'if else'    }

for key, value in glossary.items():
    print(f" {key} = {value}")

#6-5. Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt'.

#    Use a loop to print a sentence about each river, such as The Nile runs
#       through Egypt.
#    Use a loop to print the name of each river included in the dictionary.
#    Use a loop to print the name of each country included in the dictionary.

rivers = {
    "amazon river" : 'brazil', 'nile': 'egypt', 'ganges' : 'india'
}
for river, country in rivers.items():
    print(f" The {river} runs through {country}. ")


for river in rivers.keys():
    print(river)
for city in rivers.values():
    print(city)

#6-6. Polling: Use the code in favorite_languages.py (page 97).

#Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.

# Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}
take_poll = ['lis','thomas','mary','jen','sarah','edward','phil']
for name in take_poll:
    if name in favorite_languages:
        print(f" {name}, Thank you for taking the poll")
    else:
        print(f" {name}, Please take poll")

