water_height = float(input(f"Enter water height: "))
years = int(input(f"Enter number of years: "))
for z in range(1, years+1):
    print(z, round(water_height * z, 1))




