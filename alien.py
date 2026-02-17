
alien_0 = {}

# make 30 green aliens

for aliens_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien_0.append(new_alien)
    
for alien in alien_0[:3]: 
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
        alien['points'] = 10
# show the first 5 aliens 
for alien in alien_0[:5]:
    print(alien)
# show how many aliens have been created
print(f"Total number of aliens: {len(alien_0)}")

