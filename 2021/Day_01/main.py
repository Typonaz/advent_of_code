import re

def reading(file_name):
    file = open(file_name)
    array = file.read().splitlines()
    file.close()
    return array

def sum_of_mesurements(sonar_history):
    sum_of_mesurements = []
    for i in range(len(sonar_history)-2) :
        sum_of_mesurements.append(int(sonar_history[i]) + int(sonar_history[i+1]) + int(sonar_history[i+2]))
    return (sum_of_mesurements)

def compare_depth(actual_depth, previous_depth):
    if actual_depth > previous_depth  & previous_depth != 0 :
        return True
    else : 
        return False

def sum_of_increased_depth(sonar_history):
    actual_depth = 0
    previous_depth = 1
    sum_of_increased_depth = 0 
    for depth in sonar_history:
        previous_depth = actual_depth
        actual_depth = int(depth)
        if compare_depth(actual_depth, previous_depth) == True :
            sum_of_increased_depth += 1

    return sum_of_increased_depth
 

sonar_history = reading("input.txt")

sum1 = sum_of_increased_depth(sonar_history)        
print(sum1 , "depths are larger than the previous depth")


sum_of_mesurements = sum_of_mesurements(sonar_history)
sum2 =  sum_of_increased_depth(sum_of_mesurements) 
print (sum2, "sums are larger than the previous sum")
