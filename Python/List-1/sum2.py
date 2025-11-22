def sum2(nums):
  """
  Calculate the sum of the first 2 elements in an array.
  
  Args:
      nums: A list of integers
      
  Returns:
      An integer representing the sum of the first 2 elements.
      If the array has fewer than 2 elements, returns the sum of 
      available elements (or 0 for an empty array).
  """
  
  # Check if the array is empty
  # If there are no elements, there's nothing to sum, so return 0
  if len(nums) == 0:
    return 0
  
  # Check if the array has only one element
  # If so, we can't sum 2 elements, so just return the single element
  elif len(nums) == 1:
    return nums[0]
  
  # If we reach this point, the array has at least 2 elements
  # Return the sum of the first element (index 0) and second element (index 1)
  return nums[0] + nums[1]
  