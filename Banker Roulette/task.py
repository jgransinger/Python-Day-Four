import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
chosen_one = random.randint(0,4)
print(friends[chosen_one])

#Correct Method Per Course
print(random.choice(friends))