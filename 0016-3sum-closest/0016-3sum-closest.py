class Solution(object):
    def threeSumClosest(self, nums, target):

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left < right:

                current = nums[i] + nums[left] + nums[right]

                if abs(current - target) < abs(closest - target):

                    closest = current
                
                if current == target:

                    return current
                
                elif current < target:

                    left += 1
                else:

                    right -= 1
        return closest
                

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        