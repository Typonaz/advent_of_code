def reading(file_name):
    file = open(file_name)
    array = file.read().splitlines()
    file.close()
    return array


def check_tree(array, row, col):
    return array[row][col % len(array[row])] == "#"
        

def tree_counter(array, down_value, right_value):
    col = 0
    row = 0
    count = 0 
    while (row + down_value) < len(array):
        row += down_value
        col += right_value
        if check_tree(array, row, col):
            count += 1
    return count


def slopes_tree_count(array, slopes):
    trees_nums = []
    for slope in slopes:
       trees_nums.append(tree_counter(array, slope[0], slope[1]))
    return trees_nums


def mult_trees(trees_nums):
    product = 1
    for tree_num in trees_nums:
        product *= tree_num
    return product


slopes = [
    [1, 1],  
    [1, 3],  
    [1, 5],  
    [1, 7],  
    [2, 1],  
]

array = reading("file.txt")
print("puzzle 1 = ", tree_counter(array, 1, 3))

trees_nums = slopes_tree_count(array, slopes)
print("puzzle 2 = ", mult_trees(trees_nums))
