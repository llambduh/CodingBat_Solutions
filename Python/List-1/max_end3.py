def max_end3(nums):
  bigger_num = max(nums[0], nums[-1])
  nums[:] = [bigger_num] * len(nums)
  return nums
  