import random
low = int(input("Enter your low limit: "))
high = int(input("Enter your high limit: "))
randomnumber = random.randint(low, high)
print("random number between", low, "and", high, "is", randomnumber)