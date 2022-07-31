#modifying elements in a list
motorcycles= ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0]= 'ducati'
print(motorcycles)
motorcycles[0]= 'honda'

#adding elements to a list:
motorcycles.append('ducati')
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#inserting elements to the list:
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#removing elements from list:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

#using the pop() method:
motorcycles= ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#use pop method to state the last owned motocycle
motorcycles= ['honda','yamaha','suzuki']

last_owned= motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned}')

first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}')
print(motorcycles)

#removing an item by value:
motorcycles= ['honda','yamaha','suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

too_expensive= 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')


# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

invite= ['BTS', 'Chris Hemsworth', 'Thomas Abraham']
print(f'Hello, {invite[0]}, I would like to invite you to my dinner party. Thank you!')
print(f'Hello, {invite[1]}, I would like to invite you to my dinner party. Thank you!')
print(f'Hello, {invite[2]}, I would like to invite you to my dinner party. Thank you!')

#Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone_else to invite.

invite= ['BTS', 'Chris Hemsworth','Thomas Abraham']
#Chris Hemsworth can't make it
invite.remove('Chris Hemsworth')
invite.insert(1,'Chris Evans')
print(invite)
print(f'Hello, {invite[0]}, I would like to invite you to my dinner party. Thank you!')
print(f'Hello, {invite[1]}, I would like to invite you to my dinner party. Thank you!')
print(f'Hello, {invite[2]}, I would like to invite you to my dinner party. Thank you!')
print(f'Hi {invite}, we have a bigger table and I will be inviting more guests.')

#inviting more guests to dinner
invite= ['BTS', 'Chris Evans', 'Thomas Abraham']
invite.insert(0,'Mohan lal')
invite.insert(2,'Mammooty')
invite.append('Sreenivasan')
print(invite)

print(f'Hello, {invite[0]}, I am inviting you to dinner. Thanks!')
print(f'Hello, {invite[1]}, I am inviting you to dinner. Thanks!')
print(f'Hello, {invite[2]}, I am inviting you to dinner. Thanks!')
print(f'Hello, {invite[3]}, I am inviting you to dinner. Thanks!')
print(f'Hello, {invite[4]}, I am inviting you to dinner. Thanks!')
print(f'Hello, {invite[5]}, I am inviting you to dinner. Thanks!')

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t
#arrive in time for the dinner, and you have space for only two guests.
print(f'Hello {invite}, there are only 2 seats available for dinner.')

remove_1= 'Mohan lal'
invite.pop(0)
print(f'Hi, {remove_1}, sorry to say you are NOT invited anymore.')
print(invite)
remove_2 = 'Mammooty'
invite.pop(1)
print(f'Hi, {remove_2}, sorry to say you are NOT invited anymore.')
print(invite)
remove_3='Thomas Abraham'
invite.pop(2)
print(f'Hi, {remove_3}, sorry to say you are NOT invited anymore.')
print(invite)
remove_4= "Sreenivasan"
invite.pop(2)
print(f'Hi, {remove_4}, sorry to say you are NOT invited anymore.')
print(invite)
print(f'Hi {invite}, you are still invited to the dinner')

del(invite)[0]
del(invite)[0]
print(invite)

