# temperature converter
# Goal:User enters temperature in Celsius and program converts it to Fahrenheit.

# taking input from the user
celsius = float(input("Enter temperature in Celsius: "))
# converting Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
# printing the result
print(f"{celsius}°C is equal to {fahrenheit}°F")

