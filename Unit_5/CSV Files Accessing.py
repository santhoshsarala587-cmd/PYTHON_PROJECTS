import csv

file_path = r"C:\Users\Santhosh R\OneDrive\Desktop\Santhosh.csv"

def view_data():
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def add_patient():
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        disease = input("Enter Disease: ")
        doctor = input("Enter Doctor Name: ")
        dept = input("Enter Department: ")
        adate = input("Enter Admission Date: ")
        ddate = input("Enter Discharge Date: ")
        bill = input("Enter Bill Amount: ")
        
        writer.writerow([pid, name, age, gender, disease, doctor, dept, adate, ddate, bill])
    
    print("✅ Patient Added Successfully!")

def search_patient():
    name = input("Enter Patient Name to Search: ")
    
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            if name in row:
                print("Found:", row)

def delete_patient():
    pid = input("Enter Patient ID to Delete: ")
    rows = []
    
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != pid:
                rows.append(row)
    
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("🗑️ Patient Deleted Successfully!")

def access_row():
    index = int(input("Enter Row Number (starting from 0): "))
    
    with open(file_path, "r") as file:
        reader = list(csv.reader(file))
        
        if index < len(reader):
            print("Row Data:", reader[index])
        else:
            print("❌ Invalid Row Number")

def access_column():
    col_index = int(input("Enter Column Index (0-9): "))
    
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            if col_index < len(row):
                print(row[col_index])
            else:
                print("❌ Invalid Column Index")

while True:
    print("\n===== HOSPITAL MANAGEMENT =====")
    print("1. View Data")
    print("2. Add Patient")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Access Row")
    print("6. Access Column")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        view_data()
    elif choice == "2":
        add_patient()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        delete_patient()
    elif choice == "5":
        access_row()
    elif choice == "6":
        access_column()
    elif choice == "7":
        print("👋 Exiting Program...")
        break
    else:
        print("❌ Invalid Choice")