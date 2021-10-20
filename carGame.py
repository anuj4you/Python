
# Car game using if else.


order = ""
running = False
while True:
    order = input(">").lower()
    if order == "start":
        if running:
            print("Car already started...")
        else:
            print("Car started ..")
            running = True

    elif order == "stop":
        if not running:
            print("Car already stopped.")
        else:
            print("Car stopped")
            running = False
    elif order == "help":
        print("""
start - to start the car.
stop - to stop the car.
quit - to quit the game.
help - to get instructions.""")
    elif order == "quit":
        break
    else:
        print("I don't understand that...")
