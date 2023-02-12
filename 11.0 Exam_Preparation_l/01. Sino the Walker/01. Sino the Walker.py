from datetime import datetime, timedelta

time_leaving, steps, step_time = [input() for _ in range(3)]

h, m, s = list(map(int, time_leaving.split(':')))
walk_time = int(steps) * int(step_time) % (24 * 60 * 60)

dt = datetime(2023, 9, 24, h, m, s)
result = dt + timedelta(seconds=walk_time)
print('Time Arrival:', str(result)[11:])

''' 
input:
12:30:30
90
1
output:
Time Arrival: 12:32:00
'''
