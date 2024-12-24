# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - DONE
# Turing1 - DONE

# 4Sum - DONE
# IntToRoman - DONE
# MedianTwoSortedArrays -


def solution(num):
    
    normal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]    
    i = 0 
    result = ""
    
    while num > 0 :
        if num >= normal[i] :
            result += roman[i]
            num -= normal[i]
        else :
            i += 1
        
    return result


# input
k = 2549

# output
result = solution(k)

# print result
print("Hasil   :", result)