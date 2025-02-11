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

# AddLinkedList - 
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


def main():
    # Input
    k = [1,2,2,1,5,5,4,3,3,4]
    
    result = 0
    
    # Fungsi Hasil
    result =  solution(k)
    
    # Print result
    print("Hasil : ", result)
    
    
def solution(k):
    k.sort()
   
    for i in range (0,len(k),2):
       if i == len(k)-1:
           return k[i]
       elif k[i] != k[i+1]:
           return k[i]

    return -1


if __name__ == "__main__":
    main()
