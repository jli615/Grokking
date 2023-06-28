"""MY CODE"""

from collections import deque

def find_trees(nodes, edges):
  # TODO: Write your code here
  num_nodes = nodes
  added_nodes = []
  layers = 0

  in_degrees = {i:0 for i in range(nodes)}
  graph = {i:[] for i in range(nodes)}

  for edge1, edge2 in edges:
    in_degrees[edge1] += 1
    in_degrees[edge2] += 1
    graph[edge1].append(edge2)
    graph[edge2].append(edge1)

  queue = deque()
  for vertex in range(nodes):
    if in_degrees[vertex] == 1:
      queue.append(vertex)

  while num_nodes > 2:
    length = len(queue)
    num_nodes -= length
    for i in range(length):
      vertex = queue.popleft()
      added_nodes.append(vertex)
      for child in graph[vertex]:
        if child not in added_nodes:
          in_degrees[child] -= 1
          if in_degrees[child] == 1:
            queue.append(child)
      
    
  return list(queue)
  

def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))


main()

"""SOLUTION

from collections import deque


def find_trees(nodes, edges):
  if nodes <= 0:
    return []

  # with only one node, since its in-degrees will be 0, therefore, we need to handle it separately
  if nodes == 1:
    return [0]

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(nodes)}  # count of incoming edges
  graph = {i: [] for i in range(nodes)}  # adjacency list graph

  # b. Build the graph
  for edge in edges:
    n1, n2 = edge[0], edge[1]
    # since this is an undirected graph, therefore, add a link for both the nodes
    graph[n1].append(n2)
    graph[n2].append(n1)
    # increment the in-degrees of both the nodes
    inDegree[n1] += 1
    inDegree[n2] += 1

  # c. Find all leaves i.e., all nodes with 1 in-degrees
  leaves = deque()
  for key in inDegree:
    if inDegree[key] == 1:
      leaves.append(key)

  # d. Remove leaves level by level and subtract each leave's children's in-degrees.
  # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
  # Any node that has already been a leaf cannot be the root of a minimum height tree, because
  # its adjacent non-leaf node will always be a better candidate.
  totalNodes = nodes
  while totalNodes > 2:
    leavesSize = len(leaves)
    totalNodes -= leavesSize
    for i in range(0, leavesSize):
      vertex = leaves.popleft()
      # get the node's children to decrement their in-degrees
      for child in graph[vertex]:
        inDegree[child] -= 1
        if inDegree[child] == 1:
          leaves.append(child)

  return list(leaves)


def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))


main()

"""