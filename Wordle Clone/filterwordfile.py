import os

file = open("words.txt", "r")
# wordle = open("wordle.txt", "w")

for i in file:
    if len(i) == 6:
        print(i)
        # wordle.write(i)

file.close()
# wordle.close()

print("done")