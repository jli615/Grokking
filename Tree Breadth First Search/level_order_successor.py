"""MY CODE"""

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  # TODO: Write your code here
  # base case
  if root == None or key == None:
    return None
  
  # initialize queue
  queue = deque()
  queue.append(root)

  # iterate through while there are still levels to go through
  while queue:
    levelSize = len(queue)
    for i in range(levelSize):
      curr = queue.popleft()
      # add children to queue (if they exist)
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
      
      # check to see if it is answer
      if (curr.val == key):
        output = queue.popleft()
        return output

  


def main():
  root = TreeNode(1);
  root.left = TreeNode(2);
  root.right = TreeNode(3);
  root.left.left = TreeNode(4);
  root.left.right = TreeNode(5);
  
  result = find_successor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = find_successor(root, 9)
  if result:
    print(result.val)
  
  result = find_successor(root, 12)
  if result:
    print(result.val)


main()

"""SOLUTION

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if root is None:
    return None

  queue = deque()
  queue.append(root)
  while queue:
    currentNode = queue.popleft()
    # insert the children of current node in the queue
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)

    # break if we have found the key
    if currentNode.val == key:
      break

  return queue[0] if queue else None


def main():
  
  root = TreeNode(1);
  root.left = TreeNode(2);
  root.right = TreeNode(3);
  root.left.left = TreeNode(4);
  root.left.right = TreeNode(5);
  
  result = find_successor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = find_successor(root, 9)
  if result:
    print(result.val)
  
  result = find_successor(root, 12)
  if result:
    print(result.val)


main()

"""