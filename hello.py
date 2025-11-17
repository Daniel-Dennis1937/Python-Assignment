# # Assignment
# # Create a dictionary and store 3 student records
# students = {
#     "student1": {"name": "Daniel john", "age": 16, "grade": "A"},
#     "student2": {"name": "Mary James", "age": 17, "grade": "B"},
#     "student3": {"name": "David Samuel", "age": 15, "grade": "C"}
# }
# # print all student records
# for key, record in students.items():
#     print(f"{key}: {record}")


#     # Create a tuple of 5 students name(print out the first value and last value)
#     students = ("Daniel", "Mary", "David", "Peace", "Ruth")
#     # print the first and last values
#     print("first student:", students[0])
#     print("last student:", students[-1])


#     # Create a list of students name and print each using a for loopmber

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
       print("You cannot divide by zero")
except ValueError:
     print("Please enter a valid numbr: ")
     
user2 = {"Daniel": "5555"}

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if user2[username] == password:
        print("Login successful✅")
    else:
        print("Wrong password❌")

except KeyError:
     print("username not found❌")

     class car:
            pass
     my_car = car()

     class car:
          def __init__(self, brand, color, year):
             self.brand = brand
             self.color = color
             self.year = year


my_car = car("Toyota", "")
