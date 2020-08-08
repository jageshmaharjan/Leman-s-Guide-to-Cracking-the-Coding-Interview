'''
Given a list of 24 hrs time clock in "hrs:min" format,
Find minium minutes difference between any two point in the list.
example: input ["23:59", "00:00"]
        :returns 1
'''

input = ["23:30", "02:40"] # ["23:30", "02:40"] #["23:59", "00:00"]  # ["20:59", "21:20"] ["20:20", "21:30"]


def min_diff_minutes(input):
    first_clock = input[0].split(':')
    first_clock = [int(val) for val in first_clock]
    second_clock = input[1].split(':')
    second_clock = [int(val) for val in second_clock]
    if first_clock[0] == second_clock[0]:
        return second_clock[1] - first_clock[1]
    if first_clock[0] < second_clock[0] and first_clock[1] <= second_clock[1]:
        hrs_diff = second_clock[0] - first_clock[0]
        min_diff = second_clock[1] - first_clock[1]
        return hrs_diff*60 + min_diff
    if first_clock[0] < second_clock[0] and first_clock[1] > second_clock[1]:
        hrs_diff = 1 - (second_clock[0] - first_clock[0])
        min_diff = (60-first_clock[1]) + second_clock[1]
        return hrs_diff*60 + min_diff
    if first_clock[0]>second_clock[0]: #and second_clock[1] <= first_clock[1]:
        hrs_diff = (23 - first_clock[0]) + second_clock[0]
        min_diff = (60 - first_clock[1]) + (second_clock[1])
        return hrs_diff * 60 + min_diff

res = min_diff_minutes(input)
print(res)
