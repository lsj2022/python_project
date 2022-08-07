#6-1. Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.

person = {'first_name': 'Thomas', 'last_name':'Abraham', 'age':'30', 'city':'sterling'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program.

favorite_number= {'Renny': 1, 'Thomas':2, 'Lis': 3, 'James': 4, 'Sherly': 5}
print(f"Renny's favorite number is {favorite_number['Renny']}")
print(f"Thomas' favorite number is {favorite_number['Thomas']}")
print(f"Lis' favorite number is {favorite_number['Lis']}")
print(f"James' favorite number is {favorite_number['James']}")
print(f"Sherly's favorite number is {favorite_number['Sherly']}")

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let’s call it a glossary.

#Think of five programming words you’ve learned about in the previous
#chapters. Use these words as the keys in your glossary, and store their
#meanings as values.

#Print each word and its meaning as neatly formatted output. You might
#print the word followed by a colon and then its meaning, or print the word
#on one line and then print its meaning indented on a second line. Use the
#newline character (\n) to insert a blank line between each word-meaning
#pair in your output.

glossary = {
        'integer':'whole number',
        'string':'characters',
        'for_loop': 'loops',
        'if_statement':'validation',
        'elif':'if else'    }
print(f"integer = \n{glossary['integer']}")
print(f"string = \n{glossary['string']}")
print(f"for_loop =\n {glossary['for_loop']}")
print(f"if statements = \n {glossary['if_statement']}")
print(f"elif = \n {glossary['elif']}")











