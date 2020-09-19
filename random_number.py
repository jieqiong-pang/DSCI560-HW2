import random

with open('random_number.txt','w') as f:
    for i in range(0,1000):
        f.write(str(random.randint(1,100))+'\n')