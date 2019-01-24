#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:07:06 2019

@author: angoosh
"""

from threading import Thread
import os
import tkinter as tk
import random

var = "V1.0.0"
w = 34
h = 18

def play():
    global rand
    global ls
    ls = os.listdir("/home/angoosh/Hudba")
    a = len(ls)
    rand = random.randint(0, a-1)
    directory = ls[rand]
    root.title(directory)
    path = "/home/angoosh/Hudba/"+directory
    path = '"{}"'.format(path)
    os.system("cvlc -Z -L "+path)
    
def stop():
    os.system("killall vlc")
    root.title("Random Player")
    
def start():
    Thread(target = play).start()
    
root = tk.Tk()
root.title("Random Player")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(root, text = var)
label.pack(side = tk.RIGHT)

play_b = tk.Button(frame, width = w, height = h, text = "PLAY", fg = "green", command = start)
play_b.pack(side = tk.LEFT)

stop_b = tk.Button(frame, width = w, height = h, text = "STOP", fg = "red", command = stop)
stop_b.pack(side = tk.LEFT)

root.mainloop()