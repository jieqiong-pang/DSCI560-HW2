file = open('random_number.txt')

with open('equation.txt','w') as f:
    for line in file:
        y = 3*int(line)+6
        f.write(str(y)+'\n')

