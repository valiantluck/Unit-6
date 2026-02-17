
alien_0 = {}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5


print(alien_0)

alien_0['color'] = 'yellow'

print(alien_0)

del alien_0['points']

print(alien_0)

points = alien_0.get('points')  # the get method returns None if the key doesn't exist, instead of raising an error
print(points)

