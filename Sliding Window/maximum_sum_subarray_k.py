"""MY CODE"""

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  max_sum = sum(arr[0:k])
  current_sum = max_sum

  for i in range(1, len(arr) - k):
    current_sum = current_sum - arr[i-1] + arr[i+k-1]
    if current_sum > max_sum:
      max_sum = current_sum
  return max_sum


"""SOLUTION

def max_sub_array_of_size_k(k, arr):
  max_sum , window_sum = 0, 0
  window_start = 0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[window_start]  # subtract the element going out
      window_start += 1  # slide the window ahead
  return max_sum


def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()

"""