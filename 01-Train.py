# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - DONE
# Turing1 - DONE

# 4Sum - DONE
# IntToRoman - DONE
# MedianTwoSortedArrays - DONE
# ReverseLetterOnly -


def solution(nums1, nums2):
    
    merge_nums = nums1 + nums2
    merge_nums.sort()
    
    if len(merge_nums) % 2 == 1:
        result = merge_nums[len(merge_nums) // 2]
    else :
        result1 = merge_nums[(len(merge_nums) // 2) - 1]
        result2 = merge_nums[(len(merge_nums) // 2)]
        result = (result1 + result2) / 2
        
    return result


# Main Program
nums1 = [1,3,4]
nums2 = [2]

result = solution(nums1,nums2)
print("Hasil : ",result)