# Don't add songs that you like to a file by opening it with a text editor again and again
# Just run this script with python and bind that action to some key (I prefer Ctrl + Shift + Alt + S)
# Now just write the song, your songs lists is saved :D

# from Tkinter import *
import Tkinter as tk
# master = Tk()
# Label(master, text="Last Name").grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop( )


root = tk.Tk()
root.geometry("300x150")
# l = tk.Label(root, text="First Name").grid(row=0)
# print l
def func(event):
    # print("You hit return.")
    content = str(e1.get())
    a={}
    a['link'] = '/home/ironman/random/songs/link' # File which stores good songs link
    a['list'] = '/home/ironman/random/songs/list' # File which stores good songs list
    if content.find('http') != -1:
        openingFile = a['link']
    else:
        openingFile = a['list']
    # print content
    with open(openingFile, "a") as f:
    	f.write(content + "\n")
    exit(0)
root.bind('<Return>', func)
root.wm_title("      Input New Song")

# def onclick():
#     print("You clicked the button")

# button = tk.Button(root, text="click me", command=onclick)
# button.pack()
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
e1.place(x=50, y=50, width=200) #width in pixels

# e1.geometry("500x500")

e1.focus_set()
root.mainloop()