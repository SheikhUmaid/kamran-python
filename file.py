import time

# file = open("data.txt",'a')

# print(file.write("Hello World kamddssssran"))

# file.close()

# time.sleep(7)



with open("data.txt", 'a') as file:
    file.write("Hello woerld with open")

time.sleep(7)
