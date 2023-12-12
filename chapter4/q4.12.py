"""
alphabetized by last name.
"""

people = ['John Smith', 'Jackie Jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']

# Sort the list by last name
people.sort(key=lambda name: name.split()[1])

# Print the list
for name in people:
    print(name)
    
