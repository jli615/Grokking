"""MY CODE"""

def can_attend_all_appointments(intervals):
  # sort the intervals by starting time
  intervals.sort(key = lambda x: x[0])
  # define parameters
  start, end = 0, 1

  # establish tracking variable
  prev_end = intervals[0][end]

  # iterate through and check whether or not previous interval's end is less than next interval's start
  for interval in intervals[1:]:
    if prev_end > interval[start]:
      return False
    prev_end = interval[end]

  return True


def main():
  print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()

"""SOLUTION

def can_attend_all_appointments(intervals):
  intervals.sort(key=lambda x: x[0])
  start, end = 0, 1
  for i in range(1, len(intervals)):
    if intervals[i][start] < intervals[i-1][end]:
      # please note the comparison above, it is "<" and not "<="
      # while merging we needed "<=" comparison, as we will be merging the two
      # intervals having condition "intervals[i][start] == intervals[i - 1][end]" but
      # such intervals don't represent conflicting appointments as one starts right
      # after the other
      return False
  return True


def main():
  print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()

"""