import time
import os

with open('starship.txt', 'r') as file:
    r = '\t\t ' + '\t\t '.join(file.readlines())
    
for t in range(5, -1, -1):
    os.system('clear')
    print('\n'*16+'\t\t    ',t)
    print('\n'*10+r)
    time.sleep(0.8)

for h in range(35, 0, -1):
    os.system('clear')
    print('\n'*h+r)
    r += '\n\t\t   \''