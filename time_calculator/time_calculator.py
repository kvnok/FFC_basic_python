def add_time(start, duration, day_of_week=None):
	#base vars
	new_time = ""
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	#extract
	begin = start.split(":")
	begin[1] = begin[1].split(" ")
	mode = begin[1][1]
	add = duration.split(":")
	#convert
	big = int(begin[0]) + int(add[0])
	small = int(begin[1][0]) + int(add[0])
	#adjust
	if small >= 60:
		big += 1
		small -= 60
	if mode == "AM":
		big += 12
	print("BIG " + str(big) + " SMALL " + str(small))
	if day_of_week is None: #no day given
		print("if")
	else: #a day is given
		day = day_of_week
		print("else")
		index = 0
		for entry in days:
			if entry.lower() == day.lower():
				print(day)
				break
			index += 1

	return new_time
