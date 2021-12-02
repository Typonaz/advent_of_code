import re

def reading(file_name):
    return [(ligne[0: len(ligne)-2] , int(ligne[-1:])) for ligne in open(file_name).read().splitlines()]

def direction(list_of_commands):
    sum_horizontal= 0
    sum_vertical = 0 
    for i in range(len(list_of_commands)):
        if list_of_commands[i][0] == "forward":
            sum_horizontal += list_of_commands[i][1]
        elif list_of_commands[i][0] == "down":
            sum_vertical += list_of_commands[i][1]
        else :
             sum_vertical -= list_of_commands[i][1]
    return sum_horizontal*sum_vertical

def direction_with_aim(list_of_commands):
    sum_horizontal= 0
    sum_vertical = 0 
    aim = 0
    for i in range(len(list_of_commands)):
        if list_of_commands[i][0] == "forward":
            sum_horizontal += list_of_commands[i][1]
            sum_vertical += list_of_commands[i][1]*aim
        elif list_of_commands[i][0] == "down":
            aim += list_of_commands[i][1]
        else :
             aim -= list_of_commands[i][1]
    return sum_horizontal*sum_vertical

list_of_commands = reading("input.txt")
print("The result is =", direction(list_of_commands))
print("The result is =", direction_with_aim(list_of_commands))
