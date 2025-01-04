# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - DONE
# Turing1 - DONE

# 4Sum - DONE
# IntToRoman - DONE
# MedianTwoSortedArrays - DONE
# ReverseLetterOnly - DONE
# Turing2 - DONE

# AddLinkedList - DONE
# LetterComboOfPhone - DONE
# PalindromeNumber - DONE
# RomanToInt -



def solution(x):
    num_str = str(x)
    left = 0
    right = len(num_str) - 1
    
    while left < right :
        if num_str[left] != num_str[right]:
            return False
        left += 1
        right -= 1
    return True

# Input
x = 1223221

# Output
result = solution(x)

# Print Result
print("Hasil : ", result)