# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - DONE
# Turing1 - DONE

# 4Sum - DONE
# IntToRoman - DONE
# MedianTwoSortedArrays - DONE
# ReverseLetterOnly - DONE
# Turing2 - 

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
# LongestPalindromSubstring - DONE
# RemoveNthNode -
# ThreeSum - DONE
# ZigZag - DONE


def solution(k):
    list_k = list(k)
    
    left = 0
    right = len(list_k) - 1
    
    while left < right:
        if not list_k[left].isalpha():
            left += 1
        elif not list_k[right].isalpha():
            right -= 1
        else:
            list_k[left], list_k[right] = list_k[right], list_k[left]
            left += 1
            right -= 1
            
    return "".join(list_k)
    

# Input 
k = "= Hello % World !?!"

# Output
result = solution(k)    

# Print result
print("Hasil : ", result)
