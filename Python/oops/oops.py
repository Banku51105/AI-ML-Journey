def removeDuplicates(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums.append(nums.pop(nums[i]))
    return nums
print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))