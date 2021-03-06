# main code block
username = input("Hello, please enter a username: ")
print("Hello " + username + ", welcome to the compound interest calculator!")

starting_amount = int(input("Enter an amount in which you would like to start investing: "))
print("Your starting amount is: " + str(starting_amount) + " dollars.")

duration = int(input("Ok " + username + ", for how many years would you like to stay invested? "))
print("Your investment will be kept for " + str(duration) + " years.")

interest_rate = float(input("Which interest rate are you expecting?: "))
print("You have an interest rate of " + str(interest_rate) + "% per year.")

last_statement = input("Are you ready to know your future wealth? (Type Yes or No): ")

def result(starting, years, interest):
    Amount = starting * (pow((1 + interest / 100), years))
    CI = Amount - starting
    print("Total wealth is: " + str(round(Amount, 2)) + " dollars.")
    print("Compound interest is: " + str(round(CI, 2)) + " dollar.s")

wealth = result(starting_amount, duration, interest_rate)
print(wealth)
