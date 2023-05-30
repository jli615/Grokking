"""MY CODE"""

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_trees(n):
  count = count_trees_helper(1, n)
  return count

# helper
def count_trees_helper(start, end):
  # base case:
  if start >= end:
    return 1

  output = 0
  for i in range(start, end + 1):
    left_outputs = count_trees_helper(start, i - 1)
    right_outputs = count_trees_helper(i + 1, end)
    output = output + left_outputs * right_outputs 
  return output

def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()

"""SOLUTION

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_trees(n):
  return count_trees_rec({}, n)


def count_trees_rec(map, n):
  if n in map:
    return map[n]

  if n <= 1:
    return 1
  count = 0
  for i in range(1, n+1):
    # making 'i' the root of the tree
    countOfLeftSubtrees = count_trees_rec(map, i - 1)
    countOfRightSubtrees = count_trees_rec(map, n - i)
    count += (countOfLeftSubtrees * countOfRightSubtrees)

  map[n] = count
  return count


def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()

"""