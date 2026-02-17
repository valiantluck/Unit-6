fav_lang = {'jen': 'python', 'sarah': 'c', 
            'edward': 'ruby', 'phil': 'python'}

# using values 
print("The following languages have been mentioned:")

for language in fav_lang.values():
    print(language.title())