"""MY CODE"""


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def find_unique_trees(n):
  result = helper([i for i in range(1, n+1)])
  return result

def helper(list_nums):
  # base cases
  if len(list_nums) == 0:
    return [None]
  elif len(list_nums) == 1:
    return [TreeNode(list_nums[0])]

  results = []
  for i in range(len(list_nums)):
    curr_num = list_nums[i]
    left_trees = helper(list_nums[0:i])
    right_trees = helper(list_nums[i+1:])

    for l_tree in left_trees:
      for r_tree in right_trees:
        temp_tree = TreeNode(curr_num)
        temp_tree.left = l_tree
        temp_tree.right = r_tree
        results.append(temp_tree)
    
  return results



def main():
  print("Total trees: " + str(len(find_unique_trees(2))))
  print("Total trees: " + str(len(find_unique_trees(3))))


main()

"""SOLUTION


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_unique_trees(n):
  if n <= 0:
    return []
  return findUnique_trees_recursive(1, n)


def findUnique_trees_recursive(start, end):
  result = []
  # base condition, return 'None' for an empty sub-tree
  # consider n = 1, in this case we will have start = end = 1, this means we should have only one tree
  # we will have two recursive calls, findUniqueTreesRecursive(1, 0) & (2, 1)
  # both of these should return 'None' for the left and the right child
  if start > end:
    result.append(None)
    return result

  for i in range(start, end+1):
    # making 'i' the root of the tree
    leftSubtrees = findUnique_trees_recursive(start, i - 1)
    rightSubtrees = findUnique_trees_recursive(i + 1, end)
    for leftTree in leftSubtrees:
      for rightTree in rightSubtrees:
        root = TreeNode(i)
        root.left = leftTree
        root.right = rightTree
        result.append(root)

  return result


def main():
  print("Total trees: " + str(len(find_unique_trees(2))))
  print("Total trees: " + str(len(find_unique_trees(3))))


main()

"""