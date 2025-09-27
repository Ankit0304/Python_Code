class DrinkWater:
    def __init__(self):
        self.water_intake = 0  # in milliliters

    def drink(self, amount):
        self.water_intake += amount
        print(f"Drank {amount} ml of water.")

    def get_water_intake(self):
        return self.water_intake

    def reset_intake(self):
        self.water_intake = 0
        print("Water intake has been reset.")

if __name__ == "__main__":
    app = DrinkWater()
    
    while True:
        print("\n--- Drink Water Reminder ---")
        print("1. Log water intake")
        print("2. View total intake")
        print("3. Reset intake")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            try:
                amount = int(input("Enter amount in ml: "))
                if amount > 0:
                    app.drink(amount)
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == '2':
            litres = app.get_water_intake() // 1000
            mililitres = app.get_water_intake() % 1000
            if litres > 0:
                print(f"Total water intake: {litres} liters and {mililitres} ml")
            else:
                print(f"Total water intake: {mililitres} ml")

        elif choice == '3':
            app.reset_intake()
        
        elif choice == '4':
            print("Stay hydrated! Goodbye.")
            break
        
        else:
            print("Invalid choice. Please select from 1 to 4.")