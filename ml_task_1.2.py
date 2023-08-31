from itertools import combinations
import sys

given_list = ['0001','0011','0101','1011','1101','1111']

convert = lambda x : int(x,2)

converted_list = list(map(convert,given_list))

total = sum(converted_list)
#we need to partition the list in two subsets , such that their difference is the least
#no other way to do this but to brute force , generate every possible subset and check each one                        
def best_sum(nums):
    check = sys.maxsize
    for r in range(1 , len(nums)): #chooses length of subset , starting from 1 till length of list - 1. if we consider the entire list a subset , in case of lists with negative values and zero/negative sums it gives wrong output
        for subset in combinations(nums, r): #creates the subset
            result = sum(subset)
            difference = abs(total - 2*result) #if one elem is result , other elem is total-result.so diff = total-2*result
            if(difference<check): #true for first step
                check = difference  #every iteration starting from the second will be checked against the previous one
                best = result #this sum is better than the previous one. so store it
    return best 

last_elem = best_sum(converted_list)

req_list = [last_elem , total - last_elem]

print(req_list)


