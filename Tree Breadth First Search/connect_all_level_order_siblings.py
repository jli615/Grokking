"""MY CODE"""

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  # base case
  if root == None:
    return

  # initialize queue, previousNode variable
  queue = deque()
  queue.append(root)
  previousNode = None

  # iterate through while queue is not empty
  while queue:
    # take current element
    curr = queue.popleft()
    # add children to queue
    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)
    # make connection, update previousNode
    if previousNode:
      previousNode.next = curr
    previousNode = curr

  return


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()

"""SOLUTION

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  if root is None:
    return

  queue = deque()
  queue.append(root)
  currentNode, previousNode = None, None
  while queue:
    currentNode = queue.popleft()
    if previousNode:
      previousNode.next = currentNode
    previousNode = currentNode

    # insert the children of current node in the queue
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()


"""