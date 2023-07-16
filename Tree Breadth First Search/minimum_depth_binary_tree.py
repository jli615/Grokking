"""MY CODE"""

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  # TODO: Write your code here
  height = 0

  # base case
  if root == None:
    return height

  # initialize variables
  
  queue = deque()
  queue.append(root)

  # iterate through levels
  while queue:
    height += 1
    # initialize level variables
    levelSize = len(queue)

    for i in range(levelSize):
      curr = queue.popleft()

      if not curr.left and not curr.right:
        return height
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
    


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()

"""SOLUTION

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  if root is None:
    return 0

  queue = deque()
  queue.append(root)
  minimumTreeDepth = 0
  while queue:
    minimumTreeDepth += 1
    levelSize = len(queue)
    for _ in range(levelSize):
      currentNode = queue.popleft()

      # check if this is a leaf node
      if not currentNode.left and not currentNode.right:
        return minimumTreeDepth

      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()

"""