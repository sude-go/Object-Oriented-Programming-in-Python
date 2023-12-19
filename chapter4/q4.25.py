"""
Assume that we have a list of strings named indonesian. Give a sequence
of commands that alters the list so as to replace each occurrence of the value 'java'
with the value 'python' in its place.
"""

indonesian = ['java programming', 'learn java', 'java is fun', 'java is cool']

for i in range(len(indonesian)):
    indonesian[i] = indonesian[i].replace('java', 'python')
print(indonesian)
