from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for idx, val in enumerate(nums):
      for idx2, val2 in enumerate(nums):
        if (idx == idx2):
          continue
        if (val+val2 == target):
          return [idx, idx2]
    return
