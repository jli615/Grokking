"""MY CODE"""

def make_squares(arr):
  squares = []

  # define pointers
  left, right = 0, len(arr) - 1

  while left <= right:
    if abs(arr[left]) > abs(arr[right]):
      squares = [arr[left]**2] + squares
      left += 1
    else:
      squares = [arr[right]**2] + squares
      right -= 1
     
  return squares
  
  """ CS61A solution
  squares = []
  # TODO: Write your code here
  squares = sorted(arr, key = abs)
  squares = list(map(lambda x: x ** 2, squares))

  return squares
  """

  """SOLUTION
  
  def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()

  """