""""MY CODE"""

def find_happy_number(num):
  # define fast, slow variable
  fast, slow = num, num

  while True:
    fast = find_square_sum(find_square_sum(fast))
    slow = find_square_sum(slow)
    if fast == slow and slow != 1:
      return False
    if slow == 1:
      return True


def find_square_sum(num):
  current_sum = 0
  while num > 0:
    current_sum += (num % 10) ** 2
    num = num // 10
  return current_sum

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()

"""SOLUTION
def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square_sum(slow)  # move one step
    fast = find_square_sum(find_square_sum(fast))  # move two steps
    if slow == fast:  # found the cycle
      break
  return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
  _sum = 0
  while (num > 0):
    digit = num % 10
    _sum += digit * digit
    num //= 10
  return _sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()

"""