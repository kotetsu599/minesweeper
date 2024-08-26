import random


bomb_locations = []
nums_list_ookisa = []
nums_list_hirosa = []
nums_list_hirosa1 = []
hirosa = int(input("広さ:"))
amount_of_bombs = int(input("爆弾の数:"))
ookisa = hirosa * hirosa
for i in range(hirosa):
    nums_list_hirosa.append(i)
for i in range(hirosa):
    nums_list_hirosa1.append(i+hirosa*hirosa-hirosa)
for i in range(ookisa):
    nums_list_ookisa.append(i)
positions = {i:0 for i in range(ookisa)}

for i in range(amount_of_bombs):
    bomb_location = random.randint(0,ookisa-1)
    if bomb_location != positions[i]:
        positions[bomb_location]="爆"
        bomb_locations.append(bomb_location)
    else:
        i-=1

one = [-1,hirosa-1,hirosa,+hirosa+1,+1]
two = [-hirosa,-hirosa-1,-1,hirosa-1,hirosa]
three = [-1,-hirosa-1,-hirosa,-hirosa+1,+1]
four = [-hirosa,-hirosa+1,+1,+hirosa+1,hirosa]
five = [-1,-hirosa-1,-hirosa,-hirosa+1,+1,+hirosa+1,hirosa,hirosa-1]
hidariue = [+1,+hirosa+1,hirosa]
migiue = [-1,hirosa-1,hirosa]
hidarisita = [-hirosa,-hirosa+1,+1]
migisita = [-1,-hirosa-1,-hirosa]
mannnaka = [-1,-hirosa-1,-hirosa,-hirosa+1,+1,hirosa+1,hirosa,hirosa-1]

nums_ue = []
for num_list_hirosa in nums_list_hirosa:
    if num_list_hirosa not in [0,hirosa-1]:
        nums_ue.append(num_list_hirosa)

nums_migi = []
for num_list_ookisa in nums_list_ookisa:
    if (num_list_ookisa + 1) % hirosa == 0:
        nums_migi.append(num_list_ookisa)

nums_sita = []
for num_list_hirosa in nums_list_hirosa1:
    if num_list_hirosa not in [0,hirosa*hirosa-1]:
        nums_sita.append(num_list_hirosa)

nums_hidari = []
for num_list_ookisa in nums_list_ookisa:
    if num_list_ookisa % hirosa == 0:
        nums_hidari.append(num_list_ookisa)

for i in range(ookisa):
    if positions[i] != "爆":
        positions[i] = 0
        if i == 0:
            for _ in range(3):
                if i+hidariue[_] in bomb_locations:
                    positions[i]+=1
        elif i == hirosa-1:
            for _ in range(3):
                if i+migiue[_] in bomb_locations:
                    positions[i]+=1

        elif i == hirosa*hirosa-hirosa:
            for _ in range(3):
                if i+hidarisita[_] in bomb_locations:
                    positions[i]+=1

        elif i == hirosa*hirosa-1:
            for _ in range(3):
                if i+migisita[_] in bomb_locations:
                    positions[i]+=1
 
        
        elif i in nums_ue: #one
            for _ in range(5):
                if i+one[_] in bomb_locations:
                    positions[i]+=1

        elif i in nums_migi:
            for _ in range(5):
                if i+two[_] in bomb_locations:
                    positions[i]+=1

        elif i in nums_sita:
            for _ in range(5):
                if i+three[_] in bomb_locations:
                    positions[i]+=1

        elif i in nums_hidari:
            for _ in range(5):
                if i+four[_] in bomb_locations:
                    positions[i]+=1
        
        else:
            for _ in range(8):
                 if i+mannnaka[_] in bomb_locations:
                    positions[i]+=1
def to_fullwidth(num):
    return ''.join(chr(ord('０') + ord(c) - ord('0')) if c.isdigit() else c for c in str(num))
def colorize(char):
    if char == '爆':
        return f'\033[96m{char}\033[0m'
    elif char == '0':
        return char
    else:
        return f'\033[92m{char}\033[0m'


content = ""
for i in range(0, ookisa, hirosa):
    row = [f"{colorize(to_fullwidth(str(positions[j])))}" for j in range(i, i + hirosa)]
    content += ''.join(row) + '\n'

input(content)