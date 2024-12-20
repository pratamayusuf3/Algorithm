def threeSumClosest(nums, target):
    
        '''
        Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
        Return the sum of the three integers.
        You may assume that each input would have exactly one solution.
        '''
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        # menginisialisasi variabel dengan nilai awal yang sangat besar
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i+1, len(nums)-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                # karena nilai awal variabel sangat besar, maka kondisi ini akan sesuai
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest_sum
    

if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    
    result = threeSumClosest(nums, target)
    
    print("Hasil : ", result)