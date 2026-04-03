from os import system

test_cnt = 0
while True:
	test_cnt += 1
	system("gen.py > data.in")
	system("sol.py < data.in > data.ans")
	system("debug.exe < data.in > data.out")
	if system("fc data.out data.ans"):
		print(f"Wrong Answer on Testpoint No.{test_cnt}.")
		break
	else:
		print(f"Accept on Testpoint No.{test_cnt}.")