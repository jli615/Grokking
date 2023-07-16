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


def reverse_alternate_k_elements(head, k):
  # base case
  if head is None or k <= 1:
    return head

  # create tracking variables
  previous, current = None, head
  reverse = True
  last_node_before_sublist = previous
  last_node_of_sublist = current

  # iterate through while current still has more links
  while current:
    # create variable to keep track of how much more in the sublist
    i = k
    # iterate through depending on if reverse mode is on
    if reverse:
      while current and i > 0:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        i -= 1
      # create connections
      if last_node_before_sublist:
        last_node_before_sublist.next = previous
      else:
        head = previous
      last_node_of_sublist.next = current
      # update trackers
      reverse = not reverse
      last_node_before_sublist = last_node_of_sublist
      last_node_of_sublist = current
    else:
      while current and i > 0:
        previous = current
        current = current.next
        i -= 1
      # create connections:
      last_node_before_sublist.next = temp
      # update trackers
      reverse = not reverse
      last_node_before_sublist = previous
      last_node_of_sublist = current

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
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


def reverse_alternate_k_elements(head, k):
  if k <= 1 or head is None:
    return head

  current, previous = head, None
  while current is not None: # break if we've reached the end of the list
    last_node_of_previous_part = previous
    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sub_list = current
    next = None  # will be used to temporarily store the next node

    # reverse 'k' nodes
    i = 0
    while current is not None and i < k:
      next = current.next
      current.next = previous
      previous = current
      current = next
      i += 1

    # connect with the previous part
    if last_node_of_previous_part is not None:
      last_node_of_previous_part.next = previous
    else:
      head = previous

    # connect with the next part
    last_node_of_sub_list.next = current

    # skip 'k' nodes
    i = 0
    while current is not None and i < k:
      previous = current
      current = current.next
      i += 1

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

"""