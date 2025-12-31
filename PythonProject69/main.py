cars = int(input(f"Enter number of cars: "))
average_speed = 0
speed_all = 0
cars_times = 0
speed_question = False
if 1 <= cars <= 30:
    for a in range(cars):
        cars_speed = int(input(f"Enter the car's speed: "))
        speed_all = speed_all + cars_speed
        cars_times = cars_times + 1
        average_speed = speed_all / cars_times
        if cars_speed > 60:
            speed_question = True
    print(f"The average speed is: {round(average_speed, 1)}")
    if speed_question is True:
        print(f"Yes")
    else:
        print(f"No")
else:
    print(f"Wrong number of cars.")