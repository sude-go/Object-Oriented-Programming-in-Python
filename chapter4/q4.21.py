"""
(a) Predict the output if the user enters 4 and then 4.
   it will print 'answer is D'
(b) Predict the output if the user enters 9 and then 4.
    it will print 'answer is B'
(c) Predict the output if the user enters 1 and then 9.
    it will print 'answer is C'
(d) Predict the output if the user enters 6 and then 2.
    it will print 'answer is B'
"""

x = int(input('Enter a value for x: '))
y = int(input('Enter a value for y: '))

if x > 5:
    if y <= 3 and x > 8:
        print('answer is A')
    else:
        print('answer is B')
elif y > 6 or x < 2:
    print('answer is C')
else:
    print('answer is D')
