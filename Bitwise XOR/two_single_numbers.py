"""MY CODE"""

def find_single_numbers(nums):
  # TODO: Write your code here
  # first xor
  n1xn2 = 0
  for num in nums:
    n1xn2 ^= num

  # find the location of the first one bit
  first_one_bit = 1
  while n1xn2 % (2 * first_one_bit) != first_one_bit:
    first_one_bit *= 2
  
  # separate into lower and upper half
  zeroed_half = []
  oned_half = []

  for num in nums:
    if num % (2 * first_one_bit) >= first_one_bit:
      oned_half.append(num)
    else:
      zeroed_half.append(num)
  
  first_output = 0
  for num in oned_half:
    first_output ^= num

  second_output = 0
  for num in zeroed_half:
    second_output ^= num

  return [first_output, second_output]


def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()

"""SOLUTION

def find_single_numbers(nums):
    # get the XOR of the all the numbers
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # get the rightmost bit that is '1'
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    num1, num2 = 0, 0

    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()

"""