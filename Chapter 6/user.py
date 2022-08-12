# looping through a dictionary:

user_0 = {
    'username': 'efermi',
    'first':'enrico',
    'last':'fermi'
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


favorite_languages = {
    'jen': 'python',
    'sarah':'C',
    'edward': 'ruby',
    'phil': 'python'
}
for name,language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite langauge is {language.title()}")

# looping through all the keys in the dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil','sarah','erin']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t {name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

# Looping through a dictionary's key in a particular order

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")


#looping through all values in dictionary

print(f"The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())







