enter=""
while enter.lower()!="quit":
    enter = input(">").lower()
    if enter == "help":
        print(""" 
                  >Start - to start the car 
                  >Stop - to stop the car
                  >Quit - to exit 
                  """)
    elif enter == "start":
        print("Car started Ready to go !")
    elif enter == "stop":
        print("Car stopped ")
    elif enter =="quit":
        break
    else:
        print("I don't understand that...")


