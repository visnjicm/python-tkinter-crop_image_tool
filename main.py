import tkinter as tk
from myclass import MyTkImage

def LeftClick(event):
    img.zoom_out(2)
    canvas.delete('background')
    canvas.image = img.return_tk()
    canvas.create_image(0,0,anchor=tk.NW,image=canvas.image)
    print(img.return_pil())

def RightClick(event):
    img.zoom_in(2)
    canvas.delete('background')
    canvas.image = img.return_tk()
    canvas.create_image(0,0,anchor=tk.NW,image=canvas.image)
    print(img.return_pil())


if __name__ == "__main__":
    root = tk.Tk()
    img = MyTkImage('labels.jpeg')
    root.bind('<Button-1>', LeftClick)
    root.bind('<Button-3>', RightClick)
    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()
    canvas.image = img.return_tk()
    canvas.create_image(0,0,anchor=tk.NW,image=canvas.image,\
                        tags='background')
    root.mainloop()