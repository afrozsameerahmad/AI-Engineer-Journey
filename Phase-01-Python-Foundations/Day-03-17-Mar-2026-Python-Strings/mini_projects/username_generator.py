full_name = input("Enter your full name: ")
birth_year = input("Enter your birth year: ")
city = input("Enter your city: ")

# format name
name = full_name.lower().replace(" ", "_")

# city code (first 3 letters)
city_code = city.lower()[:3]

# last two digits of birth year
year = birth_year[-2:]

username = name + "_" + year + "_" + city_code

print("Generated Username:", username)