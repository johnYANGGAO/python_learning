#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/9/16 2:47 PM
# @Author  : YangGao
# @File    : window_frame.py
from tkinter import *
from PIL import ImageTk
from PIL import Image


class Window(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('GUI')
        self.pack(fill=BOTH, expand=1)
        # 特别注意 这里command 的引用方法是个地址
        # quit_button = Button(self, text='test quit', command=self.client_exit)
        # quit_button.place(x=160, y=180)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        items = ['Exit', 'json', 'text']
        file.add_command(label=items[0], command=self.client_exit)
        file.add_command(label=items[1])
        file.add_command(label=items[2], command=self.show_text)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.show_image)
        menu.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        exit()

    def show_image(self):
        load = Image.open('/Users/johnsmac/Desktop/test_image.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def show_text(self):
        text = Label(self, text='hey there guys')
        text.pack()


root = Tk()
# the size of frame
root.geometry('400x400')
app = Window(root)
root.mainloop()
