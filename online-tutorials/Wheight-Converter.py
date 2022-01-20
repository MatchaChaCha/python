weight = float(input("Enter a weight: "))

is_lbs = True

if weight < 80:
    answer = input("Is the weight in lbs or kg (Enter 'lbs' or 'kg'): ").lower()
    while answer != "lbs" and answer != "kg":
        answer = input("You can only enter 'lbs' or 'kg'. Please try again: ").lower()
    if answer == "kg":
        is_lbs = False

if is_lbs:
    print(f"Weight in kg: {weight * 0.4535}")
else:
    print(f"Weight in lbs: {weight * 2.2046}")