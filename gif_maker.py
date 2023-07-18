import os
from PIL import Image

import moviepy
from moviepy.editor import VideoFileClip

from tkinter import Tk
from tkinter.ttk import Combobox
from tkinter import filedialog, Button, Entry, Label


#https://burningrizen.tistory.com/261

def image2gif(input_img):
	#path = './source/'
	#imgs = [path + img for img in temp_img]
	imgs = input_img
	images = [Image.open(img) for img in imgs]

	max_width = max([img.size[0] for img in images])
	max_height = max([img.size[1] for img in images])

	images = [img.resize((max_width, max_height)) for img in images]

	durate = float(image_fps.get())*1000

	im = images[0]
	im.save('./output/{}.gif'.format(output_name.get()), save_all=True, append_images=images[1:], loop=0xff, duration=durate)

	#print(imgs)
	print('process done. {count} images, output size : ({width}, {height}), duration : {duration}s.'.format(count=len(images), width=max_width, height=max_height, duration=durate/1000))

def image_opener():
	img = filedialog.askopenfilenames(filetypes=[('images', '*.jpg;*.jpeg;*.png'), ('any file', '*.*')], initialdir='./source/')
	imgs_list = []

	for im in img:
		imgs_list.append(im.replace('C:', ''))


	try:
		image2gif(imgs_list)
	except:
		print('no files.')
def video_opener():
	print('do')
	"""
	img = filedialog.askopenfilename(filetypes=[('video', '*.mp4'), ('any file', '*.*')], initialdir='./source/')

	try:
		video2gif(img)
	except:
		print('no files.')
	"""


window = Tk()
window.title('GIF Maker 2.0.0')
window.geometry('350x250+150+150')
window.resizable(False, False)
window.iconbitmap('./icon.ico')


output_lbl = Label(window, text='output name : ')
output_lbl.grid(row=0, column=0, columnspan=2)
output_name = Entry(window, width=20)
output_name.insert(0, 'output')
output_name.grid(row=0, column=2, columnspan=5)

img_lbl = Label(window, text='--image2gif--')
img_lbl.grid(row=1, column=0, columnspan=2)
image_fps_lbl = Label(window, text='fps : ')
image_fps_lbl.grid(row=2, column=0)
image_fps = Combobox(window, values=[0.1, 0.2, 0.5, 0.8, 1.0, 2.0], width=5)
image_fps.current(2)
image_fps.grid(row=2, column=1)
image_scale_lbl = Label(window, text='scale : ')
image_scale_lbl.grid(row=2, column=2)
image_sclae = Combobox(window, values=['max', 'min'], width=10)
image_sclae.current(0)
image_sclae.grid(row=2, column=3, columnspan=3)
img_btn = Button(text='Open and Gif', command=image_opener, width=10)
img_btn.grid(row=2, column=7)

vid_lbl = Label(window, text='--video2gif--')
vid_lbl.grid(row=3, column=0, columnspan=2)
vid_fps_lbl = Label(window, text='fps : ')
vid_fps_lbl.grid(row=4, column=0)
vid_fps = Combobox(window, values=['fps', 20, 12, 10, 6, 5, 3], width=5)
vid_fps.current(0)
vid_fps.grid(row=4, column=1)
vid_btw_label = Label(window, text='section : ')
vid_btw_label.grid(row=4, column=2)
vid_btw_str = Entry(window, width=5)
vid_btw_str.grid(row=4, column=3)
vid_btw_ = Label(window, text='~')
vid_btw_.grid(row=4, column=4)
vid_btw_stp = Entry(window, width=5)
vid_btw_stp.grid(row=4, column=5)
vid_btw_unit = Label(window, text='[sec]')
vid_btw_unit.grid(row=5, column=5)
vid_btn = Button(window, text='Open and Gif', command=video_opener, width=10)
vid_btw_str.insert(0, 0)
vid_btw_stp.insert(0, 30)
vid_btn.grid(row=4, column=7)


window.mainloop()

print('program done.')