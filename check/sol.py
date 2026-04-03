for _ in range(int(input())):
	x, y, t = [int(v) for v in input().split()]
	s = input()

	if x == 0 and y == 0:
		print(0)
		continue

	cur_x, cur_y, min_time = 0, 0, -1
	for i, ch in enumerate(s):
		if ch == 'L' and x < 0 and x < cur_x:
			cur_x -= 1
		if ch == 'R' and x > 0 and x > cur_x:
			cur_x += 1
		if ch == 'U' and y > 0 and y > cur_y:
			cur_y += 1
		if ch == 'D' and y < 0 and y < cur_y:
			cur_y -= 1
		if x == cur_x and y == cur_y:
			min_time = i + 1
			break
	
	print(min_time)
