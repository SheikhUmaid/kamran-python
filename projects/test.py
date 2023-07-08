class Student:
    name = ""
    roll = ""
    image = ""

    def __init__(self, name, roll, image):
        self.name = name
        self.roll = roll
        self.image = image


    def print_info(self):
        print()



student1= Student("kamran", "10", "image")
print(student1.name)
# student2= Student()
# # student1.name = "kamran"
# # student1.roll = "10"
# # student1.image = "ajshdjh"

        # print("Created")