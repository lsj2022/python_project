#nesting = store multiple dictionaries in a list
# a list of dictionaries:

alien_0 = {'color':'green', 'points':5}
alien_1= {'color': 'yellow', 'points':10}
alien_2 = {'color':'red', 'points': 15}

aliens = [alien_0, alien_1,alien_2]

for alien in aliens:
    print(alien)

# make an empty list for storing
aliens= []
# make 30 green aliens
for aliens_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

#show the first 5 aliens:

for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created:
print(f"Total number of aliens: {len (aliens)}")


#modifying the list:

aliens = []
for alien_numbers in range (30):
    new_alien = {'color':'green','points':5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color']=='green':
        alien ['color'] = 'yellow'
        alien ['speed']= 'medium'
        alien ['points']= 10
for alien in aliens [:5]:
    print(alien)
print("...")