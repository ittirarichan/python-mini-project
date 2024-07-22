# salon.py

class Salon:
    def __init__(self, name):
        self.name = name
        self.staff = []
        self.services = []
        self.appointments = []

    def add_staff(self, staff_name):
        """Add a staff member to the salon."""
        self.staff.append(staff_name)
        print(f"{staff_name} has been added to the staff.")

    def add_service(self, service_name, price):
        """Add a service to the salon."""
        self.services.append({"service_name": service_name, "price": price})
        print(f"Service '{service_name}' has been added with price ${price}.")

    def make_appointment(self, customer_name, service_name, appointment_time):
        """Schedule an appointment."""
        appointment = {
            "customer_name": customer_name,
            "service_name": service_name,
            "appointment_time": appointment_time
        }
        self.appointments.append(appointment)
        print(f"Appointment scheduled for {customer_name} for {service_name} at {appointment_time}.")

    def display_staff(self):
        """Display all staff members."""
        print("Salon Staff:")
        for staff in self.staff:
            print("- " + staff)

    def display_services(self):
        """Display all services offered."""
        print("Services Offered:")
        for service in self.services:
            print(f"- {service['service_name']}: ${service['price']}")

    def display_appointments(self):
        """Display all scheduled appointments."""
        print("Scheduled Appointments:")
        for appointment in self.appointments:
            print(f"- {appointment['customer_name']} | {appointment['service_name']} | {appointment['appointment_time']}")

# Example usage
if __name__ == "__main__":
    salon = Salon("My Salon")

    # Add staff members
    salon.add_staff("Alice")
    salon.add_staff("Bob")

    # Add services
    salon.add_service("Haircut", 30)
    salon.add_service("Manicure", 20)

    # Schedule appointments
    salon.make_appointment("Customer1", "Haircut", "2024-07-25 10:00 AM")
    salon.make_appointment("Customer2", "Manicure", "2024-07-26 11:30 AM")

    # Display staff, services, and appointments
    salon.display_staff()
    print()
    salon.display_services()
    print()
    salon.display_appointments()
