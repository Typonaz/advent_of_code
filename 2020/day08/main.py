import re

def reading(file_name):
    file = open(file_name)
    array = file.read().splitlines()
    file.close()
    return array


def instructions(accumulator, instruction, line_index):
    tab = re.split(' ', instruction)
    if tab[0] == "acc":
        accumulator += int(tab[1])
        line_index +=1
    elif tab[0] == "jmp":
        line_index += int(tab[1])
    else : 
         line_index +=1
    return(accumulator, line_index)


def check_line(lines_index, line):
    return line in lines_index


def execute_instructions(array):
    lines_index = [0]
    line_index = 0
    accumulator = 0
    test = check_line(lines_index[:-1], line_index)
    while not test:
        accumulator, line_index = instructions(accumulator, array[line_index], line_index)
        lines_index.append(line_index)
        test = check_line(lines_index[:-1], line_index)
    return accumulator


# Une méthode qui parcour le tableau et qui remplace le premier nop/jmp qu'il croise, il prend en entré un index et le tableau 
# Une méthode fait tourner la liste et qui check si il repasse par par le même index on appel la méthode du dessus et on recommence 
def modify_array(array, index):
    modified_array = []
    instruction = ''
    instruction_value = 0
    modified_array = list(array)
    for index in range(index, len(array)):
        instruction, instruction_value = re.split(' ', array[index])
        if instruction == "jmp":
            instruction == "nop"
            modified_array[index] = (instruction + " " + instruction_value)
            return modified_array, index
        elif instruction == "nop":
            instruction == "jmp"
            modified_array[index] = (instruction + " " + instruction_value)
            return modified_array, index
    


def test_array(modified_array):
    

array = reading("input.txt")
print("puzzle 1 =", execute_instructions(array))


