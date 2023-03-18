import random
import time

TIME_ALLOTTED = 10
PROBLEMS = 100

start_time = time.time()
solves = 0
time_spent = 0

while solves < PROBLEMS and time_spent < TIME_ALLOTTED:
    a, b = random.randint(0,1000), random.randint(0, 1000)
    print("Add: " + str(a) + " " + str(b))
    answer = int(input("Answer: "))
    if answer == a + b:
        solves += 1
    else:
        print("Wrong answer")
        exit()
    time_spent = time.time() - start_time

if time_spent > TIME_ALLOTTED:
    print("Too slow!")
else:
    print("Good job!")
    print("byu22ind{1sn.t_pYth0n_gr3@t?}")