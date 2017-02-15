import webbrowser
import time 


total_break = 3
break_count = 0

print("The program started on : " + time.ctime())
while (break_count < total_break):
	time.sleep(1 * 60 * 60)
	webbrowser.open("https://youtu.be/-PdYdF2ZZj0")
	break_count += 1
