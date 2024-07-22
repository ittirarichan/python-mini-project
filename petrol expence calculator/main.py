# main.py
import petrol_expense_calculator

def main():
    print("Welcome to the Petrol Expense Calculator!")
    distance = float(input("Enter distance traveled (in km): "))
    mileage = float(input("Enter mileage of your vehicle (km/liter): "))
    fuel_price = float(input("Enter current fuel price per liter: "))
    
    total_cost = petrol_expense_calculator.calculate_petrol_cost(distance, mileage, fuel_price)
    
    print(f"\nThe total cost of petrol for the journey is: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
