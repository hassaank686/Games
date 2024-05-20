def remove_match_char(male, female):
    
    male_list = list(male)
    female_list = list(female)

    for letter in male_list[:]:
        if female_list.count(letter) > 0:
            female_list.remove(letter)
            male_list.remove(letter)

    count = len(male_list) + len(female_list)
    return [count, True]

# Driver code

p1 = input("Player 1 Name: ")
p1 = p1.lower()
p1 = p1.replace(" ","")

p2 = input("Player 2 Name: ")
p2 = p2.lower()
p2 = p2.replace(" ","")

result = ['Friends', "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
lists_flag = remove_match_char(p1, p2)
count = lists_flag[0]
flag = lists_flag[1]


while len(result) > 1:
    
    split_index = (count % len(result)-1)

    if split_index >= 0:
        left = result[:split_index]
        right = result[split_index+1:]
        result = right + left
    else:
        result = result[:len(result)-1]

print("Relationship Status: ", result[0])