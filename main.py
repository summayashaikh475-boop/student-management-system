class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name 
        self.marks = marks
      

    def display(self):
        print(f" ID: {self.roll} | Name: {self.name} | Marks: {self.marks} | Grade: {self.grade()}")

    def is_pass(self):
        return self.marks >= 40
    
    def grade(self):
        if self.marks>=80:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"
        

students = []
next_id = 1


def header(text):
    print("\n" + "=" * 50)
    print(text.center(50))
    print("=" * 50)

#FUNCTIONS
def add_student():
    global next_id
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    students.append(Student(next_id, name, marks))
    print(f"✅ Student added with ID: {next_id}")

    next_id +=1

def view_students():
    header("ALL STUDENTS")
    if not students:
        print("❌ No students found")
        return
    for s in students:
        s.display()
        if s.is_pass():
            print("Result: Pass")
        else:
            print("Result: Fail")
            
        print("-----------------------------")

def average_marks():
    header("AVERAGE MARKS")
    if not students:
        print("❌ No data available")
        return
    total = sum(s.marks for s in students)  
    avg = total / len(students) 
    print(f"Average Marks: {avg:.2f}")

def search_student():
    roll = int(input("Enter ID to search: "))
    for s in students:
        if s.roll == roll:
            s.display()
            return
    print("❌ Student not found!")  

def delete_student():
    roll = int(input("Enter ID to delete: ")) 
    for s in students:
        if s.roll == roll:
            students.remove(s)
            print("✅ Student deleted successfully!") 
            return
    print("❌ Student not found!")  

def update_marks():
    roll = int(input("Enter ID to update: "))

    for s in students:
        if s.roll == roll:
            new_marks = int(input("Enter new marks: "))
            s.marks = new_marks
            print("✅ Marks updated successfully!")
            return
    print("❌ Student not found!") 

def sort_students():
    if not students:
        print("❌ No students available")
        return
    
    sorted_list = sorted(students, key=lambda s: s.marks, reverse=True)
    header("TOPPER LIST")  
    for s in sorted_list:
        s.display()



def save_to_file():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.roll}, {s.name}, {s.marks}\n")  

def load_from_file():
    global next_id

    try:
        with open("students.txt", "r") as f: 
            for line in f:
                roll, name, marks = line.strip().split(", ")
                students.append(Student(int(roll), name, int(marks)))

                next_id = max(next_id, int(roll) + 1)
    except FileNotFoundError:
        pass

load_from_file()

while True:
    header("STUDENT MANAGEMENT SYSTEM")

    print("1. Add Student")
    print("2. View Students")
    print("3. Average Marks")
    print("4. Search student")
    print("5. Delete Student")
    print("6. Update Marks")
    print("7. Show Toppers")
    print("8. Save & Exit")

    choice = input("\n👉 Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        average_marks()
    elif choice == "4":
        search_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        update_marks()
    elif choice  == "7":
        sort_students()
    elif choice == "8":
        save_to_file()
        print("👋 Exiting......Bye!")   
        break 
    else:
        print("❌ Invalid choice!")                            