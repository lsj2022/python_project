#using get() to access values:
alien_0 ={'color':'green','speed':'slow'}
print(alien_0['points'])
# trace back error happens here because we are asking to print
# a value that is not defined at this time

alien_0 = {'color':'green','speed': 'slow'}
point_value = alien_0.get('points','No point value assigned.')
print(point_value)
