import re

def reading(file_name):
    return [int(x) for x in open(file_name).read().splitlines()]

def sum_of_increased_depth(sonar_history):
    sum_of_increased_depth = 0 
    for i in range(1, len(sonar_history)):
        if sonar_history[i-1] < sonar_history[i]:
            sum_of_increased_depth += 1
    return sum_of_increased_depth

def sum_of_mesurements(sonar_history):
    sum_of_mesurements = []
    for i in range(len(sonar_history)-2) :
        sum_of_mesurements.append(sonar_history[i] + sonar_history[i+1] + sonar_history[i+2])
    return sum_of_mesurements

sonar_history = reading("input.txt")

sum1 = sum_of_increased_depth(sonar_history)        
print(sum1 , "depths are larger than the previous depth")

sum_of_mesurements = sum_of_mesurements(sonar_history)
sum2 =  sum_of_increased_depth(sum_of_mesurements) 
print (sum2, "sums are larger than the previous sum")
