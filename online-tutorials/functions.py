def greet_user(first_name, last_name):
    print(f'Hi there, {first_name} {last_name}!')
    print('Welcome Aboard')
    

print("Start")
greet_user(last_name = "Smith", first_name = "John") #Positional Args before Key Word Args
calc_cost(total=50, shipping=5, discount=0.1) #key word args help increase readibility in code
print("Finish")
