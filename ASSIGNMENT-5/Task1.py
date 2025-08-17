students = {"Alice":85, "Sai":45, "Bob":33}
name = input("Enter the student's name: ")
if name in students:
    print(name +"'s marks: ", students[name])
else:
    print("Student not found.")