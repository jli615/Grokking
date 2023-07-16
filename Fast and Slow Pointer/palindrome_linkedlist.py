"""MY CODE"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  # base case
  if head is None or head.next is None:
    return True
  
  # find middle of linked list
  fast, slow = head, head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  # slow is now at the back half middle of list

  # reverse the back half of the linked list
  head_second_half = reverse(slow)
  copy_head_second_half = head_second_half
  # prev is now at the end of the list

  # check from front and back
  while (head is not None and head_second_half is not None):
    if head.value != head_second_half.value:
      break  # not a palindrome

    head = head.next
    head_second_half = head_second_half.next

  reverse(copy_head_second_half)  # revert the reverse of the second half

  if head is None or head_second_half is None:  # if both halves match
    return True
  return False
  """
  front, back = head, prev
  while front != slow:
    if front.value != back.value:
      return False
    front = front.next
    back = back.next

  return True
  """

def reverse(curr):
  prev = None
  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  return prev

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

"""SOLUTION
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  if head is None or head.next is None:
    return True

  # find middle of the LinkedList
  slow, fast = head, head
  while (fast is not None and fast.next is not None):
    slow = slow.next
    fast = fast.next.next

  head_second_half = reverse(slow)  # reverse the second half
  # store the head of reversed part to revert back later
  copy_head_second_half = head_second_half

  # compare the first and the second half
  while (head is not None and head_second_half is not None):
    if head.value != head_second_half.value:
      break  # not a palindrome

    head = head.next
    head_second_half = head_second_half.next

  reverse(copy_head_second_half)  # revert the reverse of the second half

  if head is None or head_second_half is None:  # if both halves match
    return True

  return False


def reverse(head):
  prev = None
  while (head is not None):
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

"""