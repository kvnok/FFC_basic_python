from datetime import datetime, timedelta

def calc_new_time_and_days(start, duration):
	#convert start to datatime object
	time_format = "%I:%M %p"
	start_datetime = datetime.strptime(start, time_format)
	# print(start_datetime)
	#parse duration for hours and minutes
	hours, minutes = map(int, duration.split(":"))
	s_hrs = int(start.split(":")[0])
	s_mins = int(start.split(":")[1].split(" ")[0])
	if start.split(":")[1].split(" ")[1] == "PM":
		s_hrs += 12
	#total mins
	total_mins_start = s_hrs * 60 + s_mins
	total_mins_duration = hours * 60 + minutes
	#calc days and remaining minutes
	days = (total_mins_duration + total_mins_start) // (24 * 60) #integer devision
	remaining_minutes = total_mins_duration % (24 * 60)
	#add days and remaining minutes
	sum_datatime = start_datetime + timedelta(days=days, minutes=remaining_minutes)
	#to AM/PM format
	latest_time = sum_datatime.strftime(time_format)
	return latest_time, days

def add_time(start, duration, day_of_week=None):
	new_time = ""
	day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	latest_time, days = calc_new_time_and_days(start, duration)
	if latest_time[0] == '0':
		new_time += str(latest_time)[1:]
	else:
		new_time += str(latest_time)
	#if optional argument is given
	if day_of_week is not None:
		index = 0
		for entry in day_names:
			if entry.lower() == day_of_week.lower():
				break
			index += 1
		index += days
		new_time += ", " + day_names[index % 7]
	if days > 0:
		new_time += " ("
		if days == 1:
			new_time += "next day"
		else:
			new_time += str(days) + " days later"
		new_time += ")"	
	return new_time
