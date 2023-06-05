from datetime import datetime, timedelta

current_time = datetime.strptime(input(), "%H:%M:%S")
action_time = datetime.strptime(input(), "%H:%M:%S")

if current_time > action_time:
    action_time += timedelta(days=1)

time_diff = action_time - current_time
if current_time == action_time:
    print('24:00:00')
else:
    print(str(time_diff).zfill(8))
