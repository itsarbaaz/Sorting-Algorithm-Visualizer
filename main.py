from tkinter import *
from tkinter import ttk 
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort

import random
from colors import *

window=Tk()
window.title("Sorting Algorithm Visualizer")
#window.maxsize(100,700)
window.config(bg=WHITE)

algorithm_name= StringVar()
algo_list=['Bubble Sort','Merge Sort']

speed_name= StringVar()
speed_list=['Fast', 'Medium', 'Slow']

data=[]

def drawData(data, colorArray):
	canvas.delete("all")
	canvas_width=800
	canvas_height=400
	x_width = canvas_width / (len(data)+1)
	offset = 4
	spacing = 2
	normalizedData = [i/ max(data) for i in data]

	for i, height in enumerate(normalizedData):
		x0 = i * x_width + offset + spacing
		y0 = canvas_height -height *390
		x1 = (i+1) * x_width + offset
		y1 = canvas_height
		canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

	window.update_idletasks()

def generate():
	global data
	data.clear()
	date=[]
	for i in range(0, 100):
		random_value = random.randint(1, 150)
		data.append(random_value)

	drawData(data, [BLUE for x in range(len(data))])


def set_speed():
	if speed_menu.get() == 'Slow':
		return 0.3
	if speed_menu.get() == 'Medium':
		return 0.2
	if speed_menu.get() == 'Fast':
		return 0.1
	else:
		return 0.01

def sort():
	global data
	timeTick = set_speed()
	if algo_menu.get() == 'Bubble Sort':
		bubble_sort(data, drawData, timeTick)

	elif algo_menu.get() == 'Merge Sort':
		merge_sort(data, 0, len(data)-1, drawData, timeTick)

UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#Dropdown to select sorting algorithm
l1 =Label(UI_frame, text='Algorithm: ', bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

#Dropdown to select sorting speed
l2 =Label(UI_frame, text='Sorting Speed: ', bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

#Sort Button
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GREY)
b1.grid(row=2, column=1, padx=5, pady=5)

#button for generating array
b2 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GREY)
b2.grid(row=2, column=0, padx=5, pady=5)

b3 = Button(UI_frame, text="Exit", command=window.quit, bg=LIGHT_GREY)
b3.grid(row=2, column=2, padx=5, pady=5)


#canvas to draw out array
canvas = Canvas(window, width=800, height=400, bg=BLACK)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()