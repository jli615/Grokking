"""MY CODE"""

def merge(intervals_a, intervals_b):
  result = []

  # define counters and parameters
  i, j, start, end = 0, 0, 0, 1

  while i < len(intervals_a) and j < len(intervals_b):
    # current intervals 
    a = intervals_a[i]
    b = intervals_b[j]
    # if they intersect
    if b[start] <= a[start] <= b[end] or a[start] <= b[start] <= a[end]:
      # intersecting interval
      interval_start = max(a[start], b[start])
      interval_end = min(a[end], b[end])
      result.append([interval_start, interval_end])
      # shift one of the intervals forward depending on which one ends first
      if b[end] <= a[end]:
        j += 1
      else:
        i += 1
    # if b is behind a
    elif b[end] < a[start]:
      j += 1
    #is a is behind b
    elif a[end] < b[start]:
      i += 1

  return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()

"""SOLUTION

def merge(intervals_a, intervals_b):
  result = []
  i, j, start, end = 0, 0, 0, 1

  while i < len(intervals_a) and j < len(intervals_b):
    # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
    a_overlaps_b = intervals_a[i][start] >= intervals_b[j][start] and \
                   intervals_a[i][start] <= intervals_b[j][end]

    # check if intervals overlap and intervals_b[j]'s start time lies within the other intervals_a[i]
    b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and \
                   intervals_b[j][start] <= intervals_a[i][end]

    # store the the intersection part
    if (a_overlaps_b or b_overlaps_a):
      result.append([max(intervals_a[i][start], intervals_b[j][start]), min(
        intervals_a[i][end], intervals_b[j][end])])

    # move next from the interval which is finishing first
    if intervals_a[i][end] < intervals_b[j][end]:
      i += 1
    else:
      j += 1

  return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()

"""