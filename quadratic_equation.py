#!/usr/bin/python

# Python program to solve quadratic equation

#Input the coefficients of the quadratic equation

print("Enter the coefficients of the quadratic equation:")
coefficient_a = int(input("Enter the coefficient a: "))
coefficient_b = int(input("Enter the coefficient b: "))
coefficient_c = int(input("Enter the coefficient c: "))

print("This is a quadratic equation: ",coefficient_a,"x^2 +", coefficient_b, "x +", coefficient_c, " = 0" )

#Now we need to find the discriminant, the formula is (b^2 - 4*a*c).

discriminant = (coefficient_b ** 2) - (4*coefficient_c*coefficient_a)

#The are three cases, when the equation has no solution, has one solution, and have two solutions.

if(discriminant < 0):                 #in this case the equations hasn't solution
    print("A quadratic equation has no solution")
elif(discriminant == 0):              #in this case the equation has one solution
    root = -coefficient_b / (2*coefficient_a)
    print("x = ", root)
else:                                 #in this case the equation have two solutions. x1 and x2
    root_1 = (-coefficient_b + pow(discriminant, 1/2)) / (2*coefficient_a)
    root_2 = (-coefficient_b - pow(discriminant, 1/2)) / (2*coefficient_a)
    print("x1 =", root_1, "x2 =", root_2)
