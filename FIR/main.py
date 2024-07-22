from add import *
from display import *
from search import *
from update import *
firs={}

while True:
    print("\nPolice FIR Entering System")
    print("1. Register FIR")
    print("2. Update FIR Status")
    print("3. Search FIR by ID")
    print("4. Display All FIRs")
    print("5. Exit")

    choice=input("Enter your choice (1-5): ")

    if choice=='1':
        fir_id=input("Enter FIR ID: ")
        victim_name=input("Enter Victim Name: ")
        incident_date=input("Enter Incident Date: ")
        description=input("Enter Incident Description: ")
        add_fir(firs, fir_id, victim_name, incident_date, description)

    elif choice=='2':
        fir_id=input("Enter FIR ID to update status: ")
        new_status=input("Enter New Status: ")
        update_fir_status(firs, fir_id, new_status)

    elif choice=='3':
        fir_id=input("Enter FIR ID to search: ")
        fir_info=search_fir_by_id(firs, fir_id)
        if fir_info:
            print(f"Found FIR:\nFIR ID: {fir_id}, Victim Name: {fir_info['victim_name']}, Incident Date: {fir_info['incident_date']}, Status: {fir_info['status']}")
        else:
            print(f"FIR ID {fir_id} not found.")

    elif choice=='4':
        display_all_firs(firs)

    elif choice=='5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")