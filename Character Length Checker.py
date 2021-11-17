name = input ('Name: ')

while (len(name)) < 3:
        print ("Sorry, the minimum allowed characters is 3")
    # input ('Name: ') How to make it go back to beggining? loop but then how to exit?
elif len(name) > 50:
    name = input ("Sorry, the maximum allowed characters is 50" )
    #input ('Name: ')
elif len(name) > 3 and len(name) < 50:
    print (f"{name} looks good!")
# also if i enter "yes", nothing happens, why?