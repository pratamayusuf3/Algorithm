def solution(reverse_me):
    reverse_final = list(reverse_me)
    left = 0
    right = len(reverse_me) - 1
    
    while left < right:
        if not reverse_final[left].isalpha():
            left += 1
        elif not reverse_final[right].isalpha():
            right -= 1
        else:
            reverse_final[left], reverse_final[right] = reverse_final[right], reverse_final[left]
            left += 1
            right -= 1
            
    return ''.join(reverse_final)

# Input 
k = "= Hello % World !?!"

# Output
result = solution(k)    

# Print result
print("Hasil : ", result)
    