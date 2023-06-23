"""MY CODE"""

def count_subsets(num, sum):
  dp = [[-1 for i in range(sum + 1)] for j in range(len(num))]
  return helper(dp, num, sum, 0)

def helper(dp, num, sum, index):
  if sum == 0:
    return 1

  if index >= len(num) or sum < 0:
    return 0
  
  if dp[index][sum] != -1:
    return dp[index][sum]
  
  # without
  sum1 = helper(dp, num, sum, index + 1)
  sum2 = 0
  if num[index] <= sum:
    sum2 = helper(dp, num, sum - num[index], index + 1)

  dp[index][sum] = sum1 + sum2
  return dp[index][sum]

def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
"""
def count_subsets(num, sum):
  #TODO: Write - Your - Code
  dp = [[-1 for i in range(sum + 1)] for j in range(len(num))]

  for i in range(len(num)):
    dp[i][0] = 1

  for j in range(1, sum + 1):
    dp[0][j] = num[0] == j

  for i in range(1, len(num)):
    for j in range(1, sum + 1):
      output = dp[i-1][j]
      if j >= num[i]:
        output += dp[i-1][j-num[i]]
      dp[i][j] = output

  return dp[-1][-1]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
"""

"""SOLUTIONS 
def count_subsets(num, sum):
  return count_subsets_recursive(num, sum, 0)


def count_subsets_recursive(num, sum, currentIndex):
  # base checks
  if sum == 0:
    return 1
  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # recursive call after selecting the number at the currentIndex
  # if the number at currentIndex exceeds the sum, we shouldn't process this
  sum1 = 0
  if num[currentIndex] <= sum:
    sum1 = count_subsets_recursive(
      num, sum - num[currentIndex], currentIndex + 1)

  # recursive call after excluding the number at the currentIndex
  sum2 = count_subsets_recursive(num, sum, currentIndex + 1)

  return sum1 + sum2


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()

def count_subsets(num, sum):
  # create a two dimensional array for Memoization, each element is initialized to '-1'
  dp = [[-1 for x in range(sum+1)] for y in range(len(num))]
  return count_subsets_recursive(dp, num, sum, 0)


def count_subsets_recursive(dp, num, sum, currentIndex):
  # base checks
  if sum == 0:
    return 1

  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # check if we have not already processed a similar problem
  if dp[currentIndex][sum] == -1:
    # recursive call after choosing the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    sum1 = 0
    if num[currentIndex] <= sum:
      sum1 = count_subsets_recursive(
        dp, num, sum - num[currentIndex], currentIndex + 1)

    # recursive call after excluding the number at the currentIndex
    sum2 = count_subsets_recursive(dp, num, sum, currentIndex + 1)

    dp[currentIndex][sum] = sum1 + sum2

  return dp[currentIndex][sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()







"""