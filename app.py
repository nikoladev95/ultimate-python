is_started = False

while True:
    car_command = input("> ")
    if car_command == "help":
        msg = """
start - to start the car
stop - to stop the car
quit - to exit
        """
        print(msg)
    elif car_command == "start" and not is_started:
        is_started = True
        print("Car started...Ready to go!")
    elif car_command == "start" and is_started:
        print("Car is already started.")
    elif car_command == "stop" and not is_started:
        print("You cannot stop the car, it's not started yet.")
    elif car_command == "stop" and is_started:
        is_started = False
        print("Car stopped.")
    elif car_command == "quit":
        break
    else:
        print("I don't understand that")