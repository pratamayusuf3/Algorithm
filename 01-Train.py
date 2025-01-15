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
# RomanToInt - DONE
# Turing3 - DONE

# BalanceDigit - DONE
# LongestComPrefix - DONE
# RegexMatch - DONE
# StrToInt - DONE
# TwoSum - DONE

# BinaryDepth - DONE
# LongestPalindromSubstring -




    

def solution(k):
    
    if len(k) == 0 or k[0] is None:
        return 0
    
    depth = 0
    queue = [0]
    
    while queue:
        current_size = len(queue)
        depth += 1
        
        for i in range (current_size):
            index = queue.pop(0)
            
            left_idx = (2 * index) + 1
            if left_idx < len(k) and k[left_idx] is not None:
                queue.append(left_idx)
                
            right_idx = (2 * index) + 2
            if right_idx < len(k) and k[right_idx] is not None:
                queue.append(right_idx)
            
    return depth
    

# input
k = ["1", "9", "29", None, None, "15", "7"]

# output
result = solution(k)
print("Hasil : ", result)