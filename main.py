# pass = act as a placeholder

print("\nPass Loop Control Statement")
number = int(input("Input a number to count from 1: "))
numToPass = int(input("input a number to pass/take out: "))

for i in range (1,number+1): # plus one to include the lass pint
    if i == numToPass:
        pass
    else:
        if i != number:
            print(i, end=",")
        else:
            print(i)


