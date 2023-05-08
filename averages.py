#gets user input and if number continues, if not quits.
user_input = input("Enter a number, enter q to quit:")

#initializes variables
numbers_sum = 0
numbers_count = 0
numbers_average = 0

#while look allows the program to continue taking input until
while (user_input != "q"):
    user_input = int(user_input)
    #adds the number value to the current sum of all previous numbers
    numbers_sum += user_input
    #increases the count by 1
    numbers_count += 1
    #continues the input checks
    user_input = input("Enter a number, enter q to quit:")

#calculates the average
numbers_average = numbers_sum / numbers_count

#prints all required information
print(f"the sum of the numbers entered is {numbers_sum}")
print(f"the count of the numbers entered is {numbers_count}")
print(f"the average of the numbers entered is {numbers_average}")