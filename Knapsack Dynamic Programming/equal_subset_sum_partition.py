"""MY CODE - top down"""

def can_partition(num):
  # TODO: Write your code here
  if sum(num) % 2 == 1:
    return False
  desired_sum = int(sum(num) / 2)
  dp = [[-1 for i in range(desired_sum + 1)] for j in range(len(num))]
  return helper(dp, num, desired_sum, 0)

def helper(dp, num, sum_to_go, index):
  if sum_to_go < 0 or index >= len(num):
    return False
  if sum_to_go == 0:
    return True
  # if it is already memoized
  if dp[index][sum_to_go] != -1:
    return dp[index][sum_to_go]

  with_index = helper(dp, num, sum_to_go - num[index], index + 1)
  without_index = helper(dp, num, sum_to_go, index + 1)

  dp[index][sum_to_go] = with_index or without_index
  return dp[index][sum_to_go]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
"""MY CODE - bottom up"""

def can_partition(num):
  if sum(num) % 2 == 1:
    return False
  desired_sum = int(sum(num) / 2)
  dp = [[False for i in range(desired_sum + 1)] for j in range(len(num))]

  for i in range(len(num)):
    dp[i][0] = True

  for j in range(1, desired_sum + 1):
    dp[0][j] = j == num[0]

  for i in range(1, len(num)):
    for j in range(1, desired_sum + 1):
      if dp[i - 1][j]:
        dp[i][j] = dp[i-1][j]
      elif j >= num[i]:
        dp[i][j] = dp[i-1][j - num[i]]

  return dp[-1][-1]
def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()

"""SOLUTION - top down

def can_partition(num):
  s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with equal sum
  if s % 2 != 0:
    return False

  # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
  dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]
  return True if can_partition_recursive(dp, num, int(s / 2), 0) == 1 else False


def can_partition_recursive(dp, num, sum, currentIndex):
  # base check
  if sum == 0:
    return 1

  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # if we have not already processed a similar problem
  if dp[currentIndex][sum] == -1:
    # recursive call after choosing the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    if num[currentIndex] <= sum:
      if can_partition_recursive(dp, num, sum - num[currentIndex], currentIndex + 1) == 1:
        dp[currentIndex][sum] = 1
        return 1

    # recursive call after excluding the number at the currentIndex
    dp[currentIndex][sum] = can_partition_recursive(
      dp, num, sum, currentIndex + 1)

  return dp[currentIndex][sum]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
"""

"""SOLUTION - bottom up

def can_partition(num):
  s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with same total
  if s % 2 != 0:
    return False

  # we are trying to find a subset of given numbers that has a total sum of 's/2'.
  s = int(s / 2)

  n = len(num)
  dp = [[False for x in range(s+1)] for y in range(n)]

  # populate the s=0 columns, as we can always for '0' sum with an empty set
  for i in range(0, n):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for j in range(1, s+1):
    dp[0][j] = num[0] == j

  # process all subsets for all sums
  for i in range(1, n):
    for j in range(1, s+1):
      # if we can get the sum 'j' without the number at index 'i'
      if dp[i - 1][j]:
        dp[i][j] = dp[i - 1][j]
      elif j >= num[i]:  # else if we can find a subset to get the remaining sum
        dp[i][j] = dp[i - 1][j - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][s]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()

"""
