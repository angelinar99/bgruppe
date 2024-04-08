"""
OrderOfNumbers
"""
#Task 01
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second: "))
sum = n1 + n2
print("Total sum" + " " + str(sum))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second: "))
sum = n1 + n2
if sum <= 0:
    print(f"The number is zero or negative")
elif sum > 0 and n2 < n1:
        print(f"The number has an error")
else:
    print("Thanks and bye")



#Task 02

# Provide your solution here
number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
number_three = int(input("Enter third number: "))


if number_one < number_two < number_three:
    print("The numbers are ascending")
elif number_one > number_two > number_three:
    print("The numbers are descending")
else:
    print("No specific order of numbers")

sum = number_one + number_two + number_three
is_odd = sum % 2 != 0
print(f"Is the {sum} odd? {is_odd}")
is_even = sum % 2 == 0
print(f"Is the {sum} even? {is_even}")