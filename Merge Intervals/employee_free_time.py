"""MY CODE"""

from __future__ import print_function
from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class EmployeeInterval:
    def __init__(self, interval, employee_index, schedule_index):
        self.interval = intervals
        self.employee_index = employee_index
        self.schedule_index = schedule_index

    def __lt__(self, other):
        return self.intervals[schedule_index].start < other.intervals[schedule_index].start

def find_employee_free_time(schedule):
    ## define initial parameters
    result = []
    minHeap = []

    # add initial intervals to heap
    for i in range(len(schedule)):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

    # define previous interval
    prev_interval = minHeap[0].interval
    prev_end = prev_interval.end

    # iterate through heap until there is nothing left
    while minHeap:
        queueTop = heappop(minHeap)

        # if end is less than next start
        if queueTop.interval.start > prev_end:
            result.append(Interval(queueTop.interval.start, prev_end))
            prev_interval = queueTop

        # if end is greater than next start
        else:
            if prev_end < queueTop.interval.end:
                prev_interval = queueTop
                prev_end = queueTop.interval.end
        
        employeeSchedule = schedule[queueTop.employee_index]
        if queueTop.schedule_index + 1 < len(employeeSchedule):
            heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.schedule_index + 1], queueTop.employee_index, queueTop.schedule_index + 1))
            
    return result
            
        


    """
    # add all schedule interviews to master list
    result = []
    all_intervals = []
    for times in schedule:
        all_intervals.extend(times)

    # sort all interviews by start time
    all_intervals.sort(key = lambda x: x.start)

    # merge all slots together
    merged = []
    start = all_intervals[0].start
    end = all_intervals[0].end
    # iterate through
    for interval in all_intervals:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end
    
    # at the end: add the last item
    merged.append(Interval(start, end))

    # return open intervals by finding gaps between merged intervals
    for i in range(1, len(merged)):
        result.append(Interval(merged[i-1].end, merged[i].start))

    return result
    """




def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()

"""SOLUTION

from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, minHeap = [], []

    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

    previousInterval = minHeap[0].interval
    while minHeap:
        queueTop = heappop(minHeap)
        # if previousInterval is not overlapping with the next interval, insert a free interval
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end,
                                   queueTop.interval.start))
            previousInterval = queueTop.interval
        else:  # overlapping intervals, update the previousInterval if needed
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval

        # if there are more intervals available for the same employee, add their next interval
        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                                               queueTop.intervalIndex + 1))

    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()

"""