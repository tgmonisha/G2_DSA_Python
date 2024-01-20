class Student:
    def __init__(self, student_id, name, courses):
        self.student_id = student_id
        self.name = name
        self.courses = courses


class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id not in self.students:
            self.students[student.student_id] = [student]
        else:
            # Check if the student with the same ID already exists
            for existing_student in self.students[student.student_id]:
                if existing_student.student_id == student.student_id:
                    print(
                        f"Error: Student with ID {student.student_id} already exists."
                    )
                    return
            self.students[student.student_id].append(student)

    def update_student(self, student_id, new_name=None, new_courses=None):
        if student_id in self.students:
            for student in self.students[student_id]:
                student.name = new_name if new_name is not None else student.name
                student.courses = (
                    new_courses if new_courses is not None else student.courses
                )

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def sort_students(self, criteria):
        students_to_sort = [
            student
            for students_list in self.students.values()
            for student in students_list
        ]

        if criteria == "name":
            students_to_sort.sort(key=lambda x: x.name)
        elif criteria == "courses":
            students_to_sort.sort(key=lambda x: ", ".join(x.courses))
        else:
            print("Invalid sorting criteria. Supported criteria: 'name', 'courses'")
            return

        self.students = {}
        for student in students_to_sort:
            self.add_student(student)

    def display_students(self):
        students_to_display = [
            student
            for students_list in self.students.values()
            for student in students_list
        ]
        display_students_table(students_to_display)



def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")



def get_string_input(prompt):
    return input(prompt)



def display_students_table(students):
    if not students:
        print("No students found.")
        return

    print("{:<5} {:<20} {:<20}".format("ID", "Name", "Courses"))
    print("-" * 50)

    for student in students:
        print(
            "{:<5} {:<20} {:<20}".format(
                student.student_id, student.name, ", ".join(student.courses)
            )
        )



db = StudentDatabase()

while True:
    print("\nStudent Database Menu:")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Search Students")
    print("6. Sort Students")
    print("7. Exit")

    choice = get_integer_input("Enter your choice: ")

    if choice == 1:
        student_id = get_integer_input("Enter student ID: ")
        name = get_string_input("Enter student name: ")
        courses = get_string_input("Enter student courses (comma-separated): ").split(
            ","
        )
        new_student = Student(student_id, name, courses)
        db.add_student(new_student)
        # Check if the student was added successfully
        if new_student in [
            student
            for students_list in db.students.values()
            for student in students_list
            if student.student_id == new_student.student_id
        ]:
            print("Student added successfully!")
        else:
            print("Error adding student.")

    elif choice == 2:
        db.display_students()

    elif choice == 3:
        student_id = get_integer_input("Enter student ID: ")
        new_name = get_string_input("Enter new student name (press enter to skip): ")
        new_courses = get_string_input(
            "Enter new student courses (comma-separated, press enter to skip): "
        )
        db.update_student(
            student_id,
            new_name=new_name if new_name else None,
            new_courses=new_courses.split(",") if new_courses else None,
        )
        print("Student information updated successfully!")

    elif choice == 4:
        student_id = get_integer_input("Enter student ID to delete: ")
        db.delete_student(student_id)
        print("Student deleted successfully!")

    elif choice == 5:
        keyword = get_string_input("Enter search keyword: ")
        search_criteria = get_string_input(
            "Enter search criteria (id/name/courses): "
        ).lower()
        search_results = [
            student
            for students_list in db.students.values()
            for student in students_list
            if student.student_id == keyword
            or keyword.lower() in student.name.lower()
            or any(course.lower() == keyword.lower() for course in student.courses)
        ]
        display_students_table(search_results)

    elif choice == 6:
        criteria = get_string_input("Enter sort criteria (name/courses): ")
        db.sort_students(criteria)
        print("Students sorted successfully!")

    elif choice == 7:
        print("Exiting Student Database System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
