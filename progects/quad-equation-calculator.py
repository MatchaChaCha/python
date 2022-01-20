import math

print("****************** Mr. Leeece's Quadratic Equation Solver ******************")

#Collect Coefficients of the Quadratic and Verify if allowed
a = input("Enter a value for root A: ")
isFloat = False
while not isFloat:
    try:
        a = float(a)
        isFloat = True
    except:
        a = input("Please enter a valid number: ")

b = input("Enter a value for root B: ")
isFloat = False
while not isFloat:
    try:
        b = float(b)
        isFloat = True
    except:
        b = input("Please enter a valid number: ")

c = input("Enter a value for root C: ")
isFloat = False
while not isFloat:
    try:
        c = float(c)
        isFloat = True
    except:
        c = input("Please enter a valid number: ")

#Catch for when a = 0, resolution of the equation for a line
if a == 0:
    print("This equation isn't a quadratic equation, but it's solution is:")
    if b == 0:
        if c == 0:
            print("The solution is ℝ")
            exit()
        else:
            print ("X is impossible")
    else:
        x = -c/b         
    print(f"X = {x}")
    exit()


#Calcolate Determinant
delta = b ** 2 - 4*a*c

#Determine how many solutions there are 
if delta < 0:
    print("This quadratic doesn't intersect with the X axis, it has no solutions.")

    

#Calcolate the solutions
if delta > 0:
    x1 = ((-b + math.sqrt(delta)) / 2*a)
    x2 = ((-b - math.sqrt(delta)) / 2*a)
    print(F"This quadratic has two solutions:")
    print(F"X1 ≈ {x1}")
    print(F"X2 ≈ {x2}")
elif delta == 0:
    x3 = (-b/2*a)
    print(F"This quadratic has one solution:")
    print (F"X ≈ {x3}")
else:
    print("This quadratic doesn't intersect with the X axis, it has no solutions.")