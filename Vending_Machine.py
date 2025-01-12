class Receipt:
    def __init__(self):
        print("""
__     _______ _   _ ____ ___ _   _  ____   __  __    _    ____ _   _ ___ _   _ _____
\ \   / | ____| \ | |  _ |_ _| \ | |/ ___| |  \/  |  / \  / ___| | | |_ _| \ | | ____|
 \ \ / /|  _| |  \| | | | | ||  \| | |  _  | |\/| | / _ \| |   | |_| || ||  \| |  _|  
  \ V / | |___| |\  | |_| | || |\  | |_| | | |  | |/ ___ | |___|  _  || || |\  | |___     __    __    __
   \_/  |_____|_| \_|____|___|_| \_|\____| |_|  |_/_/   \_\____|_| |_|___|_| \_|_____|   |__|  |__|  |__|
              """)
        self.purchased_items = []
    #this is to add an item
    def add_item(self, name, price):
        self.purchased_items.append({"name": name, "price": price})
    #this shows the recipt
    def print_receipt(self):
        print("\n--- Receipt ---")
        total = 0
        for item in self.purchased_items:
            print(f"{item['name']:20} ${item['price']:.2f}")
            total += item['price']
        print(f"{'Total:':20} ${total:.2f}")
        print("-----------------")
#this shows the available items
class VendingMachine:
    def __init__(self):
        self.items = {
            "A1": {"name": "Coke", "price": 2.50, "stock": 13},
            "A2": {"name": "Pepsi", "price": 2.50, "stock": 12},
            "A3": {"name": "Milk", "price": 4, "stock": 14},
            "A4": {"name": "Orange Juice", "price": 7, "stock": 8},
            "A5": {"name": "Water", "price": 1.75, "stock": 5},
            "B1": {"name": "Lays", "price": 4.50, "stock": 8},
            "B2": {"name": "Pringles", "price": 6, "stock": 8},
            "B3": {"name": "Cheetos", "price": 8, "stock": 6},
            "B4": {"name": "Doritos", "price": 6, "stock": 9},
            "B5": {"name": "Piatos", "price": 5, "stock": 15},
        }
        self.balance = 0
        self.receipt = Receipt()
    #this shows the product, the price, and how many stocks
    def show_items(self):
        print("\n--- Available Items ---")
        print(f"{'Code':<5} {'Item':<20} {'Price':<10} {'Stock'}")
        print("-" * 40)
        for code, item in self.items.items():
            print(f"{code:<5} {item['name']:<20} ${item['price']:<10.2f} {item['stock']}")
        print("-" * 40)
    #this allows the user to insert money to the vending machine is it a loop system which can keep runing until break
    def insert_money(self):
        while True:
            try:
                amount = float(input("\nInsert money $: "))
                if amount > 0:
                    self.balance += amount
                    print(f"Money inserted: ${amount:.2f}")
                    print(f"Current balance: ${self.balance:.2f}")
                    break
                else:
                    print("Please insert a valid amount greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    #this allows the user to select the item they want, displays the balance and item price, also prints the reciept this is also a 
    #loop system which looks for the following conditions to be met
    def select_item(self):
        while True:
            choice = input("\nSelect an item by code (Example: A1, B2): ").upper()
            if choice in self.items:
                item = self.items[choice]
                if self.balance >= item['price']:
                    self.balance -= item['price']
                    item['stock'] -= 1
                    self.receipt.add_item(item['name'], item['price'])
                    print(f"\nDispensing {item['name']}")
                    print(f"Remaining balance: ${self.balance:.2f}")
                else:
                    print(f"\nInsufficient funds! {item['name']} costs ${item['price']:.2f}, but you only have ${self.balance:.2f}.")
                    self.insert_money()
                break
            else:
                print("Invalid selection. Please choose a valid code (Example: A1, B2).")
    #this code runs the whole vending machine its looping system,manages the balance, allows the user to select items,
    #ask's the user to select more items and then prints the receipt
    def run(self):
        self.show_items()
        while True:
            if self.balance == 0:
                self.insert_money()
            self.select_item()

            if self.balance > 0:
                continue_choice = input("\nWould you like to make another purchase? (y/n): ").lower()
                if continue_choice != 'y':
                    self.receipt.print_receipt()
                    print(f"Remaining balance: ${self.balance:.2f}")
                    print("Thank you for using the vending machine")
                    break
            else:
                self.receipt.print_receipt()
                print(f"Remaining balance: ${self.balance:.2f}")
                print("You don't have enough balance for another purchase.")
                break

vending_machine = VendingMachine()
vending_machine.run()