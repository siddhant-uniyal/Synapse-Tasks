from itertools import combinations
import sys

given_list = ['0001','0011','0101','1011','1101','1111']

convert = lambda x : int(x,2)

converted_list = list(map(convert,given_list))

total = sum(converted_list)

half_sum = int(total/2) #ideal solution for a list of sum n , is [n/2,n/2] OR [n+1/2,n-1/2]. We use half_sum as a filter for the best solution
                       
def best_sum(nums):
    check = sys.maxsize
    for r in range(1 , len(nums) + 1): #chooses length of subset , starting from 1 till length of list
        for subset in combinations(nums, r): #creates the subset
            result = sum(subset)
            difference = abs(result-half_sum) #checking how far off the sum of the current subset is from (total of list)/2
            if(difference<check): #true for first step
                check = difference  #every iteration starting from the second will be checked against the previous one
                best = result # the best sum is the one closest to total/2
    return best 

last_elem = best_sum(converted_list)

req_list = [last_elem , total - last_elem]

print(req_list)

