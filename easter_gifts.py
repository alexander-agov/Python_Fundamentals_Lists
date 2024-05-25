gifts_for_buying = input().split(" ")
commands = input().split(" ")
while commands != ["No", "Money"]:
    if commands[0] == "OutOfStock":
        if commands[1] in gifts_for_buying:
            while commands[1] in gifts_for_buying:
                gifts_for_buying[gifts_for_buying.index(commands[1])] = "None"
        else:
            commands = input ().split ( " " )
            continue
    if commands[0] == "Required":
        if len(gifts_for_buying)-1 >= int(commands[2]) >= 0:
            gifts_for_buying[int(commands[2])] = commands[1]
        else:
            commands = input ().split ( " " )
            continue
    if commands[0] == "JustInCase":
        gifts_for_buying.pop()
        gifts_for_buying.append(commands[1])
    commands = input().split(" ")
while "None" in gifts_for_buying:
    gifts_for_buying.remove("None")
print(" ".join(map(str, gifts_for_buying)))




