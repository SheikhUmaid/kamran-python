while True:
    exp = input("Enter Expression: ")

    answer = eval(exp)
    print(answer)

    with open('db.txt','a') as file:
        file.write(f"{exp} = {answer} \n")
