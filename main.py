import tkinter as tk
from myclass import MyTkImage

def update_canvas():
    canvas.delete('background')
    canvas.image = img.return_tk()
    canvas.create_image(0,0,anchor=tk.NW,image=canvas.image)
    print(img.return_pil())

def LeftClick(event):
    img.zoom_out(2)
    update_canvas()

def RightClick(event):
    img.zoom_in(1.1)
    update_canvas()

def MiddleClick(event):
    img.zoom_reset()
    update_canvas()


if __name__ == "__main__":
    root = tk.Tk()
    img = MyTkImage('labels.jpeg')
    root.bind('<Button-1>', LeftClick)
    root.bind('<Button-2>', MiddleClick)
    root.bind('<Button-3>', RightClick)
    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()
    canvas.image = img.return_tk()
    canvas.create_image(0,0,anchor=tk.NW,image=canvas.image,\
                        tags='background')
    root.mainloop()