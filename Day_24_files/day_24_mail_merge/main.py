with open('./Input/Names/invited_names.txt', 'r') as file:
    names = file.readlines()

with open('./Output/ReadyToSend/example.txt', 'r') as file:
    content = file.read()

for name in names:
    name_strip = name.strip('\n')
    with open(f'./Output/ReadyToSend/letter_for_{name_strip}.txt', 'w') as file:
        file.writelines(content.replace('[name]', name_strip))


