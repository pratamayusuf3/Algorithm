def solution(k):
    
    if len(k) == 0 or len(k) == 1:
        return -1
    
    k.sort()
    
    result = 0
    
    # Sum Max Lower Value for each pair
    for i in range(0, len(k), 2):
        result += k[i]
        
    return result


# Input
k = [1,4,3,2]

# Output 
result = solution(k)

# Print result
print("Hasil : ",result)
