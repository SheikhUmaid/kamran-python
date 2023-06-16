import random



level = 1
score = 0

def Level1(): 
    while 1:
        print(f"Level {level} \n Score {score}")
        listt = ['-','+','*']
        random_operator = random.sample(listt,1)

        ist = random.randint(0,10)
        second = random.randint(0,10)

        if random_operator[0] == '-':
            answer = ist - second
            print(f"{ist} {random_operator[0]} {second} = ?: \n")
            user_answer = int(input("Enter answer"))
            if user_answer == answer:
                print("you won!")
                score += 1
            else:
                score -= 1
                print("wrong answer")
        elif random_operator[0] == '*':
            answer = ist * second
            print(f"{ist} {random_operator[0]} {second} = ?: \n")
            user_answer = int(input("Enter answer"))
            if user_answer == answer:
                score += 1
                print("you won!")
            else:
                score -= 1
                print("wrong answer")
        if random_operator[0] == '+':
            answer = ist + second
            print(f"{ist} {random_operator[0]} {second} = ?: \n")
            user_answer = int(input("Enter answer"))
            if user_answer == answer:
                score += 1
                print("you won!")
            else:
                score -= 1
                print("wrong answer")


def Level2(): 
    while 1:
        print(f"Level {level} \n Score {score}")
        listt = ['-','+','*']
        random_operator = random.sample(listt,1)

        ist = random.randint(20,100)
        second = random.randint(20,100)

        if random_operator[0] == '-':
            answer = ist - second
            print(f"{ist} {random_operator[0]} {second} = ?: \n")
            user_answer = int(input("Enter answer"))
            if user_answer == answer:
                print("you won!")
                score += 1
            else:
                score -= 1
                print("wrong answer")
        elif random_operator[0] == '*':
            answer = ist * second
            print(f"{ist} {random_operator[0]} {second} = ?: \n")
            user_answer = int(input("Enter answer"))
            if user_answer == answer:
                score += 1
                print("you won!")
            else:
                score -= 1
                print("wrong answer")
        if random_operator[0] == '+':
            answer = ist + second
            print(f"{ist} {random_operator[0]} {second} = ?: \n")
            user_answer = int(input("Enter answer"))
            if user_answer == answer:
                score += 1
                print("you won!")
            else:
                score -= 1
                print("wrong answer")


    

# def main():

if level == 1:
    Level1()
if level == 2:
    Level2()


# main()