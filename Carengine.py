# Car Game with While loop -

command = ""
started = False
while True :   #command != "quit" with a few words.It will stop only when we write quit.
    command = input("> ").lower() #instead of writing in all command.lower to give me lower letters
    if command == "start":
        if started:  #here, if started is True we print...
            print("Car is already started")
        else:
            started = True  #here we make started = True
        print("Car started..ready to go!")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
        print("The car stopped")
    elif command == "help":   #for multiple lines i write """ """" x3
        print("""         
Start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print( " I don't understand that")