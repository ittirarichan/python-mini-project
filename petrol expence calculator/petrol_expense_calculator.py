# petrol_expense_calculator.py

def calculate_petrol_cost(distance, mileage, fuel_price):
    fuel_consumed = distance / mileage
    total_cost = fuel_consumed * fuel_price
    return total_cost
