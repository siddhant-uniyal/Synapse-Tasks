encoded_lists = [[1,2,3,4,6],[5,7,8,9,15],[12,14,16,18],[10,11,12,13,16,17,18,20]]

def explode_chains(list):
    final = []
    for value in list: #going within every list 
        for index,number in enumerate(value):
            if index>1 and value[index]-value[index-1]==1 and value[index-1]-value[index-2]==1: # chose index>1 so that we can go upto last element without any problem
                value.pop(index)
                value.pop(index-1)
                value.pop(index-2)
        final.append(value) #appending the list within the list after it has been operated on to answer list
    return final

result = explode_chains(encoded_lists)

print(result)
        
            
            
