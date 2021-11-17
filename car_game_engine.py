command = ""
started = False
stop_count = 0

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
         print ("Car has been already started!")
        else:
            print ("Car started")
            started = True
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started == False
            print("Car stopped")
    elif command == "quit":
        break
    elif command == "help":
        print(''' 
Start - to start the car
Stop - to stop the car
Quit - to exit   
        ''')
    else:
        print ("Not an accepted command")

