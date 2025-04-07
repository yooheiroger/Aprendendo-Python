import random

random_integer = random.randint(1,10)#generates a random number between 1 and 10
print(random_integer)

random_number_0_to_1 = random.random()*10# generate a number but between 0,0 to 1
print(random_number_0_to_1)

random_float = random.uniform(1,10)
print(random_float)

random_heads_tails = random.randint(0,1)
print(random_heads_tails)
if random_heads_tails > 0:
    print('heads')
else:
    print('Tails')