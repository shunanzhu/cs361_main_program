patient_list = [
    ["1234", "Stark", "Arya", "08:00", "07/04/2000", "111-111-1111", "Annual visit"], 
    ["4321", "Snow", "Jon", "15:40", "02/14/1990", "222-222-2222", "Rash"],
    ["2345", "Stark", "Bran", "10:00", "12/25/1988", "333-333-3333", "Diabetes follow-up"],
    ["5432", "Arryn", "Jon", "09:30", "10/31/1984", "444-444-4444", "Annual visit"],
    ]


# Login Page (1)
def login_page():
    print("\n")
    print("""
    Welcome to ClinicLog!
    Log in to view your patient appointments for the day.
    ****************************************************
    """)
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    while True:
        if username == "pearpear" and password == "Pear123":
            break
        else:
            print("Username or password are incorrect. Please try again.")
            username = input("Enter Username: ")
            password = input("Enter Password: ")


# Home Page (2)
def home_page():
    while True:
        print("\n")
        print("~Today's Schedule~")
        for patient in patient_list:
            print(patient[0], "     ", patient[1], "     ", patient[2], "     ", patient[3])

        print("""
        Options:
        1) View additional patient information
        2) Add a new patient to the schedule
        3) Remove a patient from the schedule
        4) Go to feature description page
        5) Log out
        """)

        option = input("Enter Option number: ")
        if option == "1":
            patient_info()
        if option == "2":
            add_patient()
        if option == "3":
            remove_patient()
        if option == "4":
            feature_page()
        if option == "5":
            login_page()


# Patient Info Page (3)
def patient_info():
    print("\n")
    mrn = input("Enter medical record number of patient you wish to view: #")
    print("\n~Patient Information~")
    for patient in patient_list:
            if patient[0] == mrn:
                print(f"MRN: {patient[0]}")
                print(f"Last name: {patient[1]}")
                print(f"First name: {patient[2]}")
                print(f"Appt time: {patient[3]}")
                print(f"Date of birth: {patient[4]}")
                print(f"Phone number: {patient[5]}")
                print(f"Reason for visit: {patient[6]}")
                break

    print("""
        Options:
        1) Remove this patient
        2) Return to Home Page
        """)

    option = input("Enter Option number: ")
    if option == "1":
        remove_patient()
    if option == "2":
        home_page()


# Add Patient Page (4)
def add_patient():
    fields = {
        "mrn": "Enter patient medical record number (XXXX): #",
        "ln": "Enter patient last name: ",
        "fn": "Enter patient first name: ",
        "time": "Enter patient appointment time (HH:MM): ",
        "dob": "Enter patient date of birth (MM/DD/YYYY): ",
        "contact": "Enter patient phone number (XXX-XXX-XXXX): ",
        "reason": "Enter patient's reason for visit: "
    }

    patient_data = {}
    
    for field, prompt in fields.items():
        patient_data[field] = input(prompt)
    
    while True:
        print("\nCurrent patient data:")
        for field, value in patient_data.items():
            print(f"{field}: {value}")
        
        edit_field = input("\nDo you want to edit any field? (Enter field name or 'no' to continue): ").strip().lower()
        
        if edit_field == 'no':
            break
        elif edit_field in patient_data:
            patient_data[edit_field] = input(fields[edit_field])
        else:
            print("Invalid field name. Please try again.")

    patient_list.append([
        patient_data["mrn"], 
        patient_data["ln"], 
        patient_data["fn"], 
        patient_data["time"], 
        patient_data["dob"], 
        patient_data["contact"], 
        patient_data["reason"]
    ])
    
    print("\nPatient successfully added!")

    print("""
        Options:
        1) Add another patient
        2) Return to Home Page
        """)

    option = input("Enter Option number: ")
    if option == "1":
        add_patient()
    if option == "2":
        home_page()

    
# Remove Patient Page (5)
def remove_patient():
    print("\n")
    mrn = input("Enter medical record number of patient you wish to remove: #")
    print("""
    * Once removed, this patient will no longer show on Today's Schedule
    and must be manually rescheduled if needed.
    """)
    confirm = input("Are you sure you want to remove this patient from the schedule? Y/N: ")
    if confirm == 'Y':
        for patient in patient_list:
            if patient[0] == mrn:
                patient_list.remove(patient)
                print("\n")
                print("Patient successfully removed!")
                break
    print("""
        Options:
        1) Remove another patient
        2) Return to Home Page
        """)

    option = input("Enter Option number: ")
    if option == "1":
        remove_patient()
    if option == "2":
        home_page()


# Feature Description Page (6)
def feature_page():
    while True:
        print("\n")
        print("~Feature Descriptions~")

        print("""
        - View additional patient information:
        View additional patient info such as DOB, contact info, and reason for visit. 
        - Add a new patient to the schedule:
        Add a patient to the schedule with details such as medical record number, 
        last name, first name, and appointment time.
        - Remove a patient from the schedule:
        Remove a patient who has canceled or no-showed from Today's Schedule by 
        directly searching their medical record number or by first going to their 
        information page and removing from there.  
        """)    

        print("""
        Options:
        1) Return to Home Page
        """)

        option = input("Enter Option number: ")
        if option == "1":
            home_page()


if __name__ == "__main__":
    login_page()
    home_page()
