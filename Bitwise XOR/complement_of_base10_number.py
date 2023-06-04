"""MY CODE"""
import math

def calculate_bitwise_complement(n):
  
  #mask = 2 ** (math.floor(math.log(n, 2)) + 1) - 1

  return 2 ** (math.floor(math.log(n, 2)) + 1) - n - 1

def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()

""" SOLUTION 

def calculate_bitwise_complement(num):
  # count number of total bits in 'num'
  bit_count, n = 0, num
   while n > 0:
    bit_count += 1
    n = n >> 1

  # for a number which is a complete power of '2' i.e., it can be written as pow(2, n), if we
  # subtract '1' from such a number, we get a number which has 'n' least significant bits set to '1'.
  # For example, '4' which is a complete power of '2', and '3' (which is one less than 4) has a binary
  # representation of '11' i.e., it has '2' least significant bits set to '1'
  all_bits_set = pow(2, bit_count) - 1

  # from the solution description: complement = number ^ all_bits_set
  return num ^ all_bits_set


print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))
"""