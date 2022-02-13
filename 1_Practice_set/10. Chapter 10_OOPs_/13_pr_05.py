# Write a class Train which has methods to book a ticket, get status(no. of seats) and get fare information of trains running under Indian Railway.

class Train:

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("***************************************")
        print(f"The name of the train is: {self.name}")
        print(f"The total number of seats available in the train are: {self.seats}")
        print("***************************************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs. {self.fare}")

    def bookTickets(self):
        if self.seats>0:
            print(f"Your seat has been booked !! Your seat number is: {self.seats}")
            self.seats-=1
        else:
            print("Sorry this train is full !!")

local = Train("Cord line local", 25, 200)
local.fareInfo()
local.getStatus()
local.bookTickets()
local.getStatus()