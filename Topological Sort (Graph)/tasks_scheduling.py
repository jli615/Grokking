"""MY CODE"""

from collections import deque

def is_scheduling_possible(tasks, prerequisites):
  # TODO: Write your code here
  order = []
  queue = deque()

  #  track children, in degrees of each 
  children = {i: [] for i in range(tasks)}
  in_degrees = {i: 0 for i in range(tasks)}

  for start, end in prerequisites:
    children[start].append(end)
    in_degrees[end] += 1

  # add sources to queue
  for vertex, degree in in_degrees.items():
    if degree == 0:
      queue.append(vertex)

  # while queue is not empty, for each element, add to order, take childrens indegrees down
  while queue:
    vertex = queue.popleft()
    order.append(vertex)
    for child in children[vertex]:
      in_degrees[child] -= 1
      if in_degrees[child] == 0:
        queue.append(child)
      
  if len(order) == tasks:
    return True
  else:
    return False



def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()

"""SOLUTION

from collections import deque


def is_scheduling_possible(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return False

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
  graph = {i: [] for i in range(tasks)}  # adjacency list graph

  # b. Build the graph
  for prerequisite in prerequisites:
    parent, child = prerequisite[0], prerequisite[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
  # will not be able to schedule all tasks
  return len(sortedOrder) == tasks


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()

"""