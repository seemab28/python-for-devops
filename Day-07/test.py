import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge you $2")

elif type == "t2.medium":
    print("it will charge you $4")

elif type == "t2.large":
    print("it will charge you $8")

else:
    print("your input is invalid,please give valid input")