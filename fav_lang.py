fav_lang = {'jen': 'python', 'sarah': 'c', 
            'edward': 'ruby', 'phil': 'python'}

# using values 
print("The following languages have been mentioned:")

for language in set(fav_lang.values()): 
    print(language.title())
#set() function removes duplicates from the list of values
