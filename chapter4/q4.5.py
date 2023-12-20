"""
Output will be 4 10. The reason is that the for loop will run 5 times, and k will be 4 at the end of the loop.
The variable t will be 0 + 1 + 2 + 3 + 4 = 10.
"""
t = 0
for k in range(5):
    t += k

print(k, t)
