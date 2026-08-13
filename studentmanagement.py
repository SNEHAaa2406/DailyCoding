names = []
grades = []

while True:

    print("\n1. Add student")
    print("2. Update grade")
    print("3. Remove student")
    print("4. Calculate average")
    print("5. Show highest and lowest")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        name = input("Enter student name: ")
        grade = int(input("Enter grade: "))

        names.append(name)
        grades.append(grade)

        print("Student added successfully!")

    
    elif choice == 2:
        name = input("Enter student name: ")

        if name in names:
            index = names.index(name)

            new_grade = int(input("Enter new grade: "))
            grades[index] = new_grade

            print("Grade updated!")
        else:
            print("Student not found!")

    
    elif choice == 3:
        name = input("Enter student name: ")

        if name in names:
            index = names.index(name)

            names.pop(index)
            grades.pop(index)

            print("Student removed!")
        else:
            print("Student not found!")

    
    elif choice == 4:
        if len(grades) == 0:
            print("No grades available!")
        else:
            average = sum(grades) / len(grades)
            print("Average grade:", average)

    
    elif choice == 5:
        if len(grades) == 0:
            print("No grades available!")
        else:
            print("Highest grade:", max(grades))
            print("Lowest grade:", min(grades))

    # Exit
    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")