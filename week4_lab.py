def celsius_to_fahrenheit(celsius):
    """
    This function converts a temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit





secret_number = 467
while True:
    guess = int(input("Guess the secret number (between 1 and 1000): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number.")
        break