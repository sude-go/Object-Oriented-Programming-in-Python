"""
(a) Predict the output if the user enters 4 and then 4.
  it will print 'answer is D'
(b) Predict the output if the user enters 2 and then 4.
    it will print 'answer is C'
(c) Predict the output if the user enters 1 and then 9.
    it will print 'answer is A'
(d) Predict the output if the user enters 2 and then 6.
    it will print 'answer is B'
"""
x = int(input('Enter a value for x: '))
y = int(input('Enter a value for y: '))

if y >= 7:
    print('answer is A')
elif x < 4:
    if y > 4:
        print('answer is B')
    else:
        print('answer is C')
else:
    print('answer is D')
