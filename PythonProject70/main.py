cars = int(input(f"Enter number of cars: "))
max_speed = 0
lowest_speed = 301
less_30 = 0
wrong_speed = False
if 1 <= cars <= 30:
    for a in range(cars):
        cars_speed = int(input(f"Enter the car's speed: "))
        if 1 < cars_speed < 300:
            if cars_speed > max_speed:
                max_speed = cars_speed
            if cars_speed < lowest_speed:
                lowest_speed = cars_speed
            if cars_speed <= 30:
                less_30 = less_30 + 1
        else:
            wrong_speed = True
        if wrong_speed:
            print(f"The car's speed is incorrect")
            break
    else:
        print(max_speed - lowest_speed)
        print(less_30)
else:
    print(f"Wrong number of cars.")
