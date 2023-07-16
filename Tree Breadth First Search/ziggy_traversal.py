"""MY CODE"""

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  # TODO: Write your code here

  # base case
  if root == None:
    return result
  
  # initialize variables
  queue = deque()
  queue.append(root)
  reverse = -1

  # iterate through levels while there are elements in the queue
  while queue:

    # initialize variables for each level
    levelSize = len(queue)
    levelArray = []

    # iterate through each item in each level
    if reverse == -1:
      for i in range(levelSize):
        curr = queue.popleft()
        levelArray.append(curr.val)
        if curr.left:
          queue.append(curr.left)
        if curr.right:
          queue.append(curr.right)
      # change it for the next layer
      reverse = 1
    elif reverse == 1:
      for i in range(levelSize):
        curr = queue.pop()
        levelArray.append(curr.val)
        if curr.right:
          queue.appendleft(curr.right)
        if curr.left:
          queue.appendleft(curr.left)
      reverse = -1
    
    result.append(levelArray)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()

"""SOLUTION

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  leftToRight = True
  while queue:
    levelSize = len(queue)
    currentLevel = deque()
    for _ in range(levelSize):
      currentNode = queue.popleft()

      # add the node to the current level based on the traverse direction
      if leftToRight:
        currentLevel.append(currentNode.val)
      else:
        currentLevel.appendleft(currentNode.val)

      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.append(list(currentLevel))
    # reverse the traversal direction
    leftToRight = not leftToRight

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()

"""