"""MY CODE"""

def flip_and_invert_image(matrix):
  #TODO: Write your code here.
  length = len(matrix)
  output = []
  # iterate through rows of matrix
  for i in range(len(matrix)):
    output.append([])
    row = matrix[i]
    for j in range(len(row)):
      output[i].append(1 ^ row[length - 1 - j])

  return output

def main():
  print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
  print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()

"""SOLUTION

def flip_an_invert_image(matrix):
  C = len(matrix)
  for row in matrix:
    for i in range((C+1)//2):
      row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1
      
  return matrix

def main():
    print(flip_an_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_an_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()

"""