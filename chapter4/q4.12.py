"""
Assume that people is a list of names, each represented as a string using the
format 'firstName lastName'. Print out the names one per line, yet alpha-
betized by last name.
"""

people = ['John Smith', 'Jackie Jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']

# Sort the list by last name
people.sort(key=lambda name: name.split()[1])

# Print the list
for name in people:
    print(name)
    