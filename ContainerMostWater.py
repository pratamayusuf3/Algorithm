def solution(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    # start dari yang terjauh
    while left < right :
        current_area = min(height[left],height[right]) * (right - left)
        max_area = max(max_area, current_area)
        
        # yang lebih pendek bergerak
        if height[left] < height[right] :
            left += 1
        else :
            right -= 1
            
    return max_area

# input
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# output 
result = solution(height)
print("Hasil : ",result)