print("21 Number Game!")
list = [0]
def check1(s):
    if s < 4 and s > 0:
        return True
    else:
        return False
def lose():
    print("You lost the Game!\nTry Again!")
    return
def your_turn():
    print("You're Turn")
    inp = int(input("How many values would you like to Enter: "))
    check1(inp)
    if check1(inp) == True:
        while len(list) <= 21:
                for i in range(inp):
                    ent = int(input('>'))
                    if ent == list[-1]+1:
                        list.append(ent)
                    else:
                        print('Give consective number')
                        break
                    i += 1
                if list[-1] >= 21:
                    print('Computer Won!')
                else:
                    comp_turn()
    else:
        print("These many values are not valid.")

def comp_turn():
    print("Computer's Turn")
    inp = list[-1] + 1
    if inp >= 21:
        print("You Win!")
    else:
        list.append(inp)
        print(list)
        your_turn()

# whose gonna go first
print("Press 'F' to go First.\nPress 'S' to go second.\n")
turn = input(">")
if turn.lower() == 'f':
    your_turn()
    pass
elif turn.lower() == 's':
    comp_turn()
    pass
else:
    print("You've entered the Wrong entry!")
    lose()