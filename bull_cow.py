
def str_list(st):
    li = []
    for i in st:
        i = int(i)
        li.append(i)
    return li
def inputs():
    u2 = input('Guess Number: ')
    return u2

def noDuplicates(num):
    num_li = str_list(num)
    while len(num_li) != len(set(num_li)):
        print("No Duplicates") 
        x = enter_num()
        num_li = str_list(x)
    return num_li

def enter_num():
    x = input('Enter Number to guess: ')
    return x

entry = enter_num()
user1 = noDuplicates(entry)
p1 = str_list(user1)
user2 = noDuplicates(inputs())
p2 = str_list(user2)

cows = 0
bulls = 0
c = []


while user1 != user2:
    for i in range(len(p1)):
        if p1[i] == p2[i]:
            bulls += 1
            c.append(p1[i])
    if bulls > 0:    
        for i in range(len(c)):
            p1.remove(c[i])
            p2.remove(c[i])

    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] == p2[j] and i != j:
                cows += 1
    print(f"Response: {bulls} Bulls, {cows} Cows")
    cows = 0
    bulls = 0
    user2 = noDuplicates(inputs())
    p2 = str_list(user2)
    p1 = str_list(user1)
    c = []

if user1 == user2:
    print("Congradulations! You Guessed right!")
