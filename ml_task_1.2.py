from itertools import combinations

given_list = ['0001','0011','0101','1011','1101','1111']

convert = lambda x : int(x,2)

converted_list =  list(map(convert,given_list))

total = sum(converted_list)

half_sum = int(total/2)

def subset_sums(nums):
    result = []
    for r in range(len(nums) + 1):
        for subset in combinations(nums, r):
            result.append(sum(subset))
    return result

check = 10000

last_elem = 0

sums = subset_sums(converted_list)

for count,value in enumerate(sums):
    if(abs(value-half_sum)<check):
        check = abs(value-half_sum)
        last_elem = value

req_list = [last_elem,total-last_elem]

print(req_list) 
