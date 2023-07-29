names = []
with open("Input/Names/invited_names.txt") as nomes:
    for name in nomes:
        names.append(name.strip())
#print(names)

with open("Input/Letters/starting_letter.txt") as carta:
    content = carta.read()

print(content)

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as newFile:
        newContent=content.replace("[name]", f"{name}")
        newFile.write(newContent)