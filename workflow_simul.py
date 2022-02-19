import numpy as np


def get_avg_commit_duration():
	return (commit_time[-1] - commit_time[0]) / (len(commit_time) - 1)


def get_next_fetch():
	if len(commit_time) == 0 or len(commit_time) == 1:
		return now + 30
	return now + get_avg_commit_duration()


def update_last_ten_commit_interval():
	commit_time.append(now)
	if len(commit_time) > 11:  # need 11 timestamp to measure 10 interval
		commit_time.pop(0)


def get_next_commit():
	shape, scale = 36, 5 / 6
	time = now + np.random.gamma(shape, scale)
	update_last_ten_commit_interval()
	return time


commit_time = []
now = 0
fetch_count = 0
fetch_hit = 0
committed = True
delay_avg = 0

next_fetch = get_next_fetch()
prev_commit = 0
next_commit = get_next_commit()

while now < 1000000:
	while next_fetch < next_commit:
		now = next_fetch
		if len(commit_time) == 0:
			delay = now  # only happens at the beginning when fetch = now and commit = 0
		delay = now - commit_time[-1]
		print('delay', delay)
		delay_avg = ((delay_avg * fetch_count) + delay) / (fetch_count + 1)
		fetch_count += 1

		if committed:
			fetch_hit += 1
			committed = False

		print('fetch', now)
		next_fetch = get_next_fetch()

	while next_commit < next_fetch:
		now = next_commit
		committed = True

		print('commit', now)
		next_commit = get_next_commit()
		prev_commit = now

print('Successful fetch rate:', fetch_hit / fetch_count * 100, '%')
print('Average fetch delay:', delay_avg, 'min.')
