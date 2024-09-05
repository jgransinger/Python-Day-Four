import random
import MyModule

random_number = random.randint(0,2)
print(random_number)

if random_number == 0:
    print("THat's a zero.")
elif random_number == 1:
    print("That's a one.")
elif random_number == 2:
    print("That's a big ole two.")

    #imported from other file MyModule
print(MyModule.myfavnum)

#Random Float floating point number
random_num = random.random()
random_num_10 = random.random() * 10
print(random_num)
print(random_num_10)

random_float = random.uniform(0,10)
print(random_float)
#-------------------------------------
print("-----")
print("Coin Flip Game: ")
coin_result = random.randint(0,1)
if coin_result == 0:
    print("Heads")
else:
    print("Tails")

