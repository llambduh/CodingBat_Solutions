def same_first_last(nums):
  """
  Determines if the first and last elements of an array are equal.
  
  Args:
    nums: A list of integers
    
  Returns:
    True if the array has at least 1 element and the first element 
    equals the last element, False otherwise
  """
  
  # First, check if the array meets the minimum length requirement
  # If the array is empty (length < 1), we cannot compare first and last elements
  # Return False immediately to avoid index errors
  if len(nums) < 1:
    return False
  
  # At this point, we know the array has at least 1 element
  # Compare the first element (index 0) with the last element (index -1)
  # Note: nums[-1] is Python's way of accessing the last element
  # If the array has only 1 element, nums[0] and nums[-1] refer to the same element,
  # which will always be equal, so this correctly returns True
  return nums[0] == nums[-1]
  