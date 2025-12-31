first_day_km = int(input(f"Enter km of first day: "))
max_km = int(input(f"Enter max number of km: "))
days = 1
result = first_day_km
while result < max_km:
    result = result * (1 + 0.1)
    days = days + 1
print(f"It will take {days} days and {round(result, 2)} km.")