#simple dictionary

alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

#dictionary= collection of key-value pairs; key is connected to a value
# dictionary is wrapped by {} with values inside the braces
#used to give discriptions to a value/variable

#accessing values in a dictionary

alien_0 = {'color' : 'green', 'points': 5}
new_points = alien_0 ['points']
print(f'You just earned {new_points} points!')


#adding new key-value pairs:
alien_0 = {'color': "green", 'points':5}
alien_0['x position'] =0
alien_0['y position'] = 25
print(alien_0)


#starting with an empty dictionary:

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points']= 5
print(alien_0)

#modify values in dictionary
alien_0 = {'color': 'green'}
print(f"the alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0 ['color']}.")

alien_0 ={'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position: {alien_0['x_position']}")

#move alien to the right:
#determine how far to move the alien based on its current speed
if alien_0['speed']=='slow':
    x_increment = 1
elif alien_0['speed']=='medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment= 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")


#removing key value pairs:
alien_0 = {'color':'green', 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)


#dictionary of similar objects:
favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward': 'ruby',
                      'phil':'python'}
language =favorite_languages ['sarah'].title()
print(f"sarah's favorite language is {language}.")


