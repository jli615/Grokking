"""MY CODE"""

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
  result = []
  # TODO: Write your code here
  # base case
  if root == None:
    return result

  # initialize queue
  queue = deque()
  queue.append(root)

  # iterate through while queue is not empty
  while queue:

  # track levelSize
    level_size = len(queue)

  # all elements other than last element
    for i in range(level_size - 1):
      curr = queue.popleft()
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
      
  # if we are at end of level, add node to array
    last_elem = queue.popleft()
    result.append(last_elem)
    if last_elem.left:
      queue.append(last_elem.left)
    if last_elem.right:
      queue.append(last_elem.right)

  # add children to queue
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()

"""SOLUTION

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    for i in range(0, levelSize):
      currentNode = queue.popleft()
      # if it is the last node of this level, add it to the result
      if i == levelSize - 1:
        result.append(currentNode)
      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()

"""