class ParkingGarage:
    def __init__(self, num_tickets, num_parking_spaces):
        self.num_tickets = num_tickets
        self.num_parking_spaces = num_parking_spaces
        current_tickets = []
        parking_spots = range(1, 101)

    def driver(self):
        valid_ticket = False
        while valid_Ticket:
            verify_ticket = input("would you like to purchase a ticket?: ")
        if verify_ticket == "yes":
            self.purchase_ticket
        if valid_ticket == "no":
            print("thank you, have a nice day!")
            

    def purchase_ticket(self):
        pass

        def take_ticket(self):
            while True:
                purchase_ticket = False
            valid_ticket = input("do you have a ticket?: ")
            if valid_ticket == "yes":
                valid_ticket = valid_ticket.lower()
                purchase_ticket = True
            if purchase_ticket == True:
                current_tickets.append(valid_ticket)
            if valid_ticket == "no":
                print("sorry you need to buy a ticket to proceed.")

            def pay_for_parking(self):
                valid_ticket = int(input("What is your ticket number?: "))
                if valid_ticket in self.current_tickets:
                    payment = input("Enter your payment amount: ")
                    self.current_tickets[purchase_ticket]["paid"] = True
                    print("Payment has been accepted! You have 20 minutes to leave the garage.")
                elif current_tickets:
                    print("Your ticket has been paid already.")
                else:
                    print("Sorry! the ticket number is invalid.")

            def leave_garage(self):
                valid_ticket = int(input("what is your ticket number?: "))
                if self.current_tickets.get(ticket):
                    if self.current_ticket[ticket]["paid"]:
                        print("Thank you, have a nice day!")
                        self.parking_spaces.append(self.current_tickets[ticket]["parking_space"])
                        self.valid_ticket.append(ticket)
                        del self.current_tickets[ticket]
                    else:
                        print("you did not pay that ticket because it has not been paid")
                else:
                    print("this is the invalid ticket number, please try again.")

test = ParkingGarage(valid_ticket)
print(test.valid_ticket)
