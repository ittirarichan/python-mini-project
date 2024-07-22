# main.py
from salon import Salon

def main():
    salon = Salon("My Salon")

    while True:
        print("\nWelcome to My Salon Management System")
        print("1. Add Staff Member")
        print("2. Add Service")
        print("3. Make Appointment")
        print("4. Display Staff Members")
        print("5. Display Services Offered")
        print("6. Display Scheduled Appointments")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            staff_name = input("Enter staff member's name: ")
            salon.add_staff(staff_name)
        elif choice == '2':
            service_name = input("Enter service name: ")
            price = float(input("Enter service price: "))
            salon.add_service(service_name, price)
        elif choice == '3':
            customer_name = input("Enter customer's name: ")
            service_name = input("Enter service name: ")
            appointment_time = input("Enter appointment time (e.g., '2024-07-25 10:00 AM'): ")
            salon.make_appointment(customer_name, service_name, appointment_time)
        elif choice == '4':
            salon.display_staff()
        elif choice == '5':
            salon.display_services()
        elif choice == '6':
            salon.display_appointments()
        elif choice == '7':
            print("Exiting salon management system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
