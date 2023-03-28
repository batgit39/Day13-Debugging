#task 1
# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
    # print("This is an even number.")
# else:
    # print("This is an odd number.")

#solution - the operator used in if statement is assignment operator instead of comparision operator
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")



#task 2
# year = input("Which year do you want to check?")

# if year % 4 == 0:
    # if year % 100 == 0:
        # if year % 400 == 0: 
            # print("Leap year.")
        # else:
            # print("Not leap year.")
    # else:
        # print("Leap year.")
# else:
    # print("Not leap year.")

#solution - the type of year is string so the interpreter can't do math on it, just convert it to integer
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0: 
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


#task 3
# for number in range(1, 101):
    # if number % 3 == 0 or number % 5 == 0:
        # print("FizzBuzz")
    # if number % 3 == 0: 
        # print("Fizz")
    # if number % 5 == 0: 
        # print("Buzz")
    # else:
        # print([number])

#solution problem 1 - there are 3 if's which will execute and we will get FizzFizzBuzz on a number divisible by 3.
#To counter this just put all the if's in elif ladder.
# problem 2 - the first if says or so if the number is divisible by 3 or 5, FizzBuzz will be printed.
#Simply change that to and and problem solved
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0: 
        print("Fizz")
    elif number % 5 == 0: 
        print("Buzz")
    else:
        print([number])
