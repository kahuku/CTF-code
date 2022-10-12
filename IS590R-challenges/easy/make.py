import random
FILES = 100
f_i = random.randint(0, FILES - 1)
for i in range(FILES):
    with open("challenge/" + str(i) + ".txt", 'w') as f:
        if i != f_i:
            f.write(random.choice(open("words.txt","r").read().splitlines()))
        else:
            f.write("byu22ind{grep_works_too}")