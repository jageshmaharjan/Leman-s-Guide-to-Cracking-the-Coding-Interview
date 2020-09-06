'''
Given a collection of intervals, merge all overlapping intervals
example: intervals = [[1,3],[2,6],[8,10],[15,18]]
        :returns [[1,6],[8,10],[15,18]

        intervals = [[2,4],[4,7],[6,8],[9,10]]
        :returns [[2, 8], [9, 10]]
'''

intervals = [[2,4],[4,7],[6,8],[9,10]] # [[1,3],[2,6],[8,10],[15,18]]  #


def merge_itervals(intervals):
    last_interval_val = intervals[0][0]-1
    for i, interval in enumerate(intervals):
        if interval[0] <= last_interval_val:
            intervals[i-1][1] = intervals[i][1]
            intervals.pop(i)
            return merge_itervals(intervals)
        last_interval_val = interval[1]
    return intervals


res = merge_itervals(intervals)
print(res)