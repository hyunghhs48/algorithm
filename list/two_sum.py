#배열
def twoSum(nums, target):
  n = len(nums)
  for i in range(n):
    for j in range(i + 1, n):  #같은 수끼리 더할 수 없음
      if nums[i] + nums[j] == target:
        return True

  return False


print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))

# 중첩반복문 -> 시간 복잡도가 O(n^2)라 범위 내에서 시간복잡도 초과될 수 있