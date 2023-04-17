import time


class ParkingGarage:

    available_tickets = my_list = list(range(1, 101))
    available_spaces = my_list = list(range(1, 101))
    paid_tickets = []
    occupied_spaces = []

    def driver(self):
        home_screen = input('\n      "PAY-TO-PARK"\n(press ENTER to continue)')
        if home_screen == "":
            time.sleep(.5)
            print('\nHello')
            time.sleep(1)
            welcome_message = input(
                "\nIf you would like to Pay-To-Park please respond with yes or no.\nTo view parking garage info enter 'info'\n(Enter 'q' to quit anytime):\n")
            if welcome_message.lower() == "yes":
                time.sleep(.5)
                self.purchase_ticket()
            elif welcome_message.lower() == 'q':
                time.sleep(1)
                print('Good-bye!')
                time.sleep(2)
                self.driver()
            elif welcome_message.lower () == 'info':
              time.sleep(1)
              print(f'\nHere are the:\n\nAvailable Tickets:{len(ParkingGarage.available_tickets)}\nPaid Tickets:{len(ParkingGarage.paid_tickets)}\nAvailable Parking Spaces:{len(ParkingGarage.available_spaces)}\nOccupied Spaces:{len(ParkingGarage.occupied_spaces)}')
              time.sleep(6)
              self.driver()
            elif welcome_message.lower() == 'no':
                time.sleep(.2)
                print("\nUnderstood, bye-bye now!")
                time.sleep(2)
                self.driver()
            else:
                print("\nSorry,invalid entry. Please try again")
                time.sleep(2)
                self.driver()

    def purchase_ticket(self):
        self.paid = False
        pay = input("\nPlease swipe your credit card and then enter 'done'")
        if pay.lower() == 'done':
          time.sleep(1)
          print("\nProcessing....")
          time.sleep(3)
          print("\n\"PAYMENT APPROVED\"\n")
          time.sleep(2)
          print('Thank you, take your ticket down below.')
          time.sleep(6)
          self.paid = True
          self.store_info()  
        elif pay.lower == 'q':
          time.sleep(2)
          self.driver()  
        else:
          time.sleep(.2)
          print("\nPlease Try Again")
          time.sleep(2)
          self.driver()

    def store_info(self):
      sold_tickets = ParkingGarage.available_tickets.pop()
      self.paid_tickets.append(sold_tickets)
      taken_spaces = ParkingGarage.available_spaces.pop()
      self. occupied_spaces.append(taken_spaces)
      time.sleep(1)
      self.driver()
 
test = ParkingGarage()
test.driver()
