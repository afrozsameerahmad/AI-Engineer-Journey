'''
The current population of a town is 1000. the population of town is increasing at the rate of 10% per year
you have to write  a program to find out the population at the end of each of the last 10 years 

'''
current_population = 1000
growth_rate = 0.10
for year in range(1, 11):
    current_population += current_population * growth_rate
    print(f"Population at the end of year {year}: {int(current_population)}")
