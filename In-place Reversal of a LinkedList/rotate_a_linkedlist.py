"""MY CODE"""

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def rotate(head, rotations):
  # create copy pointer to avoid editing original
  new_head = head
  # rotate through while rotations > 0:
  while rotations > 0:
    new_head = new_head.next or head
    rotations -= 1
  # new pointer to go through and ensure it links all the way through
  iterator = new_head
  while iterator.next != new_head:
    if iterator.next is None:
      iterator.next = head
    iterator = iterator.next
  iterator.next = None
  return new_head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()

"""SOLUTION

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def rotate(head, rotations):
  if head is None or head.next is None or rotations <= 0:
    return head

  # find the length and the last node of the list
  last_node = head
  list_length = 1
  while last_node.next is not None:
    last_node = last_node.next
    list_length += 1

  last_node.next = head  # connect the last node with the head to make it a circular list
  rotations %= list_length  # no need to do rotations more than the length of the list
  skip_length = list_length - rotations
  last_node_of_rotated_list = head
  for i in range(skip_length - 1):
    last_node_of_rotated_list = last_node_of_rotated_list.next

  # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
  head = last_node_of_rotated_list.next
  last_node_of_rotated_list.next = None
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()


"""