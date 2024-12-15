import tkinter as tk
from tkinter import ttk
import datetime
import time

def load_subtitles(filename):
	groups = []
	temp = []
	with open(filename, 'r') as f:
		lines = f.readlines()

	for line in lines:
		if line != '\n':
			temp.append(line)
		else:
			groups.append(temp)
			temp = []
	return groups

def find_start_end(string):
	start, end = string.split('-->')

	def conv(x):
		x = datetime.datetime.strptime(x.strip(), '%H:%M:%S,%f')
		return datetime.timedelta(hours=x.hour, minutes=x.minute, seconds=x.second, microseconds=x.microsecond)
	return conv(start), conv(end)

class TimeSliderApp:
	def __init__(self, root, filename):
		self.root = root
		self.root.title("Time Slider")

		self.elapsed_time_sec = 0
		
		self.subtitle_groups = load_subtitles(filename)
		
		_, end_time = find_start_end(self.subtitle_groups[-1][1])
		
		# Convert start and end times to seconds
		self.start_seconds = 0
		self.end_seconds = end_time.total_seconds()
		
		# Make window full screen
		screen_width = root.winfo_screenwidth()
		screen_height = root.winfo_screenheight()
		self.root.geometry(f"{screen_width}x{screen_height}")
		
		# Create main frame
		main_frame = ttk.Frame(root, padding="20")
		main_frame.pack(fill=tk.BOTH, expand=True)
		
		self.time_label = ttk.Label(
			main_frame,
			text=0,
			font=("Arial", 72)
		)
		self.time_label.pack(pady=50)
		
		# Create slider
		self.slider = ttk.Scale(
			main_frame,
			from_=self.start_seconds,
			to=self.end_seconds,
			orient="horizontal",
			command=self.update_time
		)
		self.slider.pack(fill=tk.X, pady=50, padx=20)
		
		# Create pause/play button
		self.play_button = ttk.Button(
			main_frame,
			text="Play",
			command=self.play_pause
		)
		self.play_button.pack(pady=10)

		# Add keyboard bindings
		self.root.bind('<Escape>', lambda e: self.root.quit())
		
	def play_pause(self):
		if self.play_button["text"] == "Play":
			self.play_button["text"] = "Pause"
			while self.play_button["text"] == "Pause":
				time.sleep(1)
				# this is the main logic
				# find a group to show, 
				# then in a while loop show itr, something like this:

				# for group in groups:
				# 	index = group[0]
				# 	start, end = find_start_end(group[1])

				# 	text = "".join(group[2:]).replace(r'{\an8}', '').replace(r'<i>', '"').replace(r'</i>', '"')
				# 	pause.until(started_subtitles + start)

				# 	T.insert('1.0', "".join(text))

				# 	T.update_idletasks()
				# 	T.update()
				# 	pause.until(started_subtitles + end)
				# 	T.delete('1.0', tk.END)


				self.elapsed_time_sec += 1
				print(self.elapsed_time_sec)
				self.update_time(self.elapsed_time_sec)
		else:
			self.play_button["text"] = "Play"

	def update_time(self, value):
		# Convert slider value to time
		seconds = int(float(value))
		hours = seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = seconds % 60

		self.elapsed_time_sec = float(value)

		# Update label
		time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
		self.time_label.config(text=time_str)

def main():
	root = tk.Tk()
	# Example: Set start time to 01:30:00 and end time to 04:45:30
	app = TimeSliderApp(root, "SubtitlePlayer/Moana.2016.720p.BluRay.x264-ITA.srt")
	root.mainloop()

if __name__ == "__main__":
	main()



