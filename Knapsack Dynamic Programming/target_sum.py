"""MY CODE"""

"""def find_target_subsets(num, s):
  array_sum = sum(num)
  # TODO: Write your code here 
  dp = [[0 for i in range(-array_sum, array_sum + 1)] for i in range(len(num))]

  dp[0][num[0]] = 1
  dp[0][-num[0]] = 1

  for i in range(1, len(num)):
    for j in range(-array_sum, array_sum + 1):
      dp[i][j] = dp[i-1][j-num[i]] + dp[i-1][j+num[i]]
    
  return dp[-1][s]


def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
"""

def find_target_subsets(num, s):
  if (s + sum(num)) % 2 == 1:
    return 0
  desired_sum = (s + sum(num)) // 2
  
  dp = [[0 for j in range(desired_sum + 1)] for i in range(len(num))]

  for i in range(len(num)):
    dp[i][0] = 1
  
  for j in range(1, desired_sum + 1):
    dp[0][j] = num[0] == j

  for i in range(1, len(num)):
    for j in range(1, desired_sum + 1):
      output = dp[i-1][j]
      if j >= num[i]:
        output += dp[i-1][j-num[i]]
      dp[i][j] = output

  return dp[-1][-1]

def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()

"""SOLUTIONS WITH O(N*S) and O(S) SPACE COMPELXITY

def find_target_subsets(num, s):
  totalSum = sum(num)

  # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s + totalSum) / 2'
  if totalSum < s or (s + totalSum) % 2 == 1:
    return 0

  return count_subsets(num, (s + totalSum) // 2)


# this function is exactly similar to what we have in 'Count of Subset Sum' problem.
def count_subsets(num, s):
  n = len(num)
  dp = [[0 for x in range(s+1)] for y in range(n)]

  # populate the sum = 0 columns, as we will always have an empty set for zero sum
  for i in range(0, n):
    dp[i][0] = 1

  # with only one number, we can form a subset only when the required sum is
  # equal to the number
  for s in range(1, s+1):
    dp[0][s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(1, s+1):
      dp[i][s] = dp[i - 1][s]
      if s >= num[i]:
        dp[i][s] += dp[i - 1][s - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][s]


def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()


def find_target_subsets(num, s):
  totalSum = sum(num)

  # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s +totalSum) / 2'
  if totalSum < s or (s + totalSum) % 2 == 1:
    return 0

  return count_subsets(num, (s + totalSum) // 2)


# this function is exactly similar to what we have in 'Count of Subset Sum' problem
def count_subsets(num, sum):
  n = len(num)
  dp = [0 for x in range(sum+1)]
  dp[0] = 1

  # with only one number, we can form a subset only when the required sum is equal to the number
  for s in range(1, sum+1):
    dp[s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(sum, -1, -1):
      if s >= num[i]:
        dp[s] += dp[s - num[i]]

  return dp[sum]


def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()

"""

