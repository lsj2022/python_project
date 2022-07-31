#sort Method:
cars= ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#reverse order:
cars.sort(reverse=True)
print(cars)

#sorting a list temporarily sorted()
cars= ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\n Here is the original list again:')
print(cars)

#printing list in reverse order
cars= ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#Finding the length of a list
cars= ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(len(cars))

# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.

visit= ['Greece','Mexico', 'Portugal', 'India','Turkey']
print('Here is the original list:')
print(visit)
print('Here is the sorted list:')
print(sorted(visit))
print('Here is the original list again:')
print(visit)
print('Here is the list in reverse: ')
print(sorted(visit, reverse= True))
print('Here is the list original again')
print(visit)
print('here is the list reversed ')
visit.reverse()
print(visit)
visit.reverse()
print(visit)
visit.sort()
print(visit)
visit.sort(reverse=True)
print(visit)


#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
#through 3-7 (page 42), use len() to print a message indicating the number
#of people you are inviting to dinner.

invite= ['Chris Evans', 'Thomas Abraham', 'BTS', 'John Abraham', 'Mohan lal']
print('Hi everyone, we are inviting', len(invite), 'people to the party!')

#3-10. Every Function: Think of something you could store in a list. For example,
#you could make a list of mountains, rivers, countries, cities, languages, or anything
#else you’d like. Write a program that creates a list containing these items
#and then uses each function introduced in this chapter at least once.

states = ['kerala','Virginia','Florida','Tamil Nadu','New York']
print(f'These are the states I would like to visit',sorted(states),)
print(f'The states in reverse:', sorted(states, reverse= True),)
states.append('Maryland')
print(states)
states.remove('Maryland')
print(states)
states.insert(0,'Maryland')
print(states)
del states [0]
print(states)
popped_states =states.pop()
print(f'the last state i want to visit is {popped_states}')
print(states)
first_state= states.pop(0)
print(f'the first state I want to visit is {first_state.title()}')
print(f'I would like to visit', states[1],)
print(f'I would like to visit', states[0],)
print(f'I would like to visit', states[2],)
print(f'I would like to visit', states[3],)
print(f'I would like to visit', states[4],)

print(f'I actually do not want to visit:', states[3],)
states.remove(3)

