import random


words = [
    "filip",
    "retard",
    "is",
    "why"
]

write_content = []


for i in range(len(words)):
    write_content.append(random.choice(words))

output_str = ", ".join(write_content)
print (output_str)

x = input()

while True:
    if x != output_str:
        print("invalid input")
        x = input()
    else:
        print("Correct!")
        break