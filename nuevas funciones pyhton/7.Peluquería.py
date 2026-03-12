client = int(input(" enter your arrival time:"))

if client > 6 and client <= 11:
    print("the morning hours ")
elif client > 12 and client <= 17:
    print("if it comes in the afternoon")
elif client > 18 and client <= 22:
    print("if it comes in the night")
else:
    print("outside of working hours in any other case")
