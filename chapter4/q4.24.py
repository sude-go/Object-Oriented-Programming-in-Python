"""
adieu 1
aloha 4
bonjour 4
ciao 2
dia duit 2
goeie dag 3
guten dag 3
hallo 2
hola 3
jambo 2
shalom 3
salaam 3
terve 4
zdravo 2
"""
greeting = ['adieu', 'aloha', 'bonjour', 'ciao', 'dia duit', 'goeie dag', 'guten dag', 'hallo', 'hola', 'jambo',
            'shalom', 'salaam', 'terve', 'zdravo']
answer = 1

for word in greeting:
    if word.count('a') == 1:
        if 'o' in word:
            if word.endswith('o'):
                answer = 2
            else:
                answer = 3
    elif len(word) < 6:
        answer = 4
    print(word, answer)
