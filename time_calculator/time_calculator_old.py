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
	small = int(begin[1][0]) + int(add[1])
	#adjust
	while small >= 60:
		big += 1
		small -= 60
	days_cut = 0
	print("input : " + start + " + " + duration)
	print("calc : " + str(big) + ":" + str(small))
	if mode == "AM" and big < 12:
		big += 12
	while big >= 24:
		big -= 24
		days_cut += 1
	#set mode again
	if big < 12:
		mode = "AM"
	else:
		mode = "PM"
	#special case for PM 
	if big >= 13:
		big -= 12
	#special case for 00:xx AM being 12:xx AM
	if big == 0:
		big += 12
	#first part of output
	new_time += str(big) + ":"
	if small <= 9:
		new_time += "0"
	new_time += str(small) + " " + mode
	#if optional argument is given
	if day_of_week is not None:
		index = 0
		for entry in days:
			if entry.lower() == day_of_week.lower():
				break
			index += 1
		index += days_cut
		new_time += ", " + days[index % 7]
	if days_cut > 0:
		new_time += " ("
		if days_cut == 1:
			new_time += "next day"
		else:
			new_time += str(days_cut) + " days later"
		new_time += ")"		
	return new_time
