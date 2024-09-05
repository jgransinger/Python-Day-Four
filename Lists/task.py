fruits = ["apples", "pears", "bananers", "tomatoes"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
                     "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
                     "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
                     "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[25])

states_of_america[2] = "Taco-Land" #replaced NJ
states_of_america.append("SaladLand")
states_of_america.extend(["PizzaLand", "BurgerLand"])
print(states_of_america)

state_number = int(input("Enter the number in which a state joined the USA: "))
print(f"The number {state_number} state to join the union was: {states_of_america[state_number]}")

