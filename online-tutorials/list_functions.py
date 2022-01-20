# my attempt
   # numbers = [5, 2, 1, 7, 2, 4, 2, 2, 2, 2, 2, 3]
   # place_count = numbers[0]

    #numbers.sort()

   # for nums in numbers:
   #  place_plus = place_count + 1
   #  if place_count == place_plus:
    # numbers.remove(place_count)
   # print(numbers)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

uniques.sort()
print(uniques)