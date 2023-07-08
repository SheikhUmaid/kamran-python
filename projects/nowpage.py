import random 

num1 = random.randint(0,10)
num2 = random.randint(0,10)

solution = num1 * num2
for i in range(10):
    print(f"{num1} X {num2} = ")

    user_input = int(input("Enter solution: "))

    if user_input == solution:
        print("you won!")
        break
    else:
        print("try again")
