import tkinter as tk
from myclass import MyTkImage

def update_canvas(x,y):
    canvas.delete('background')
    canvas.image = img.return_tk()
    canvas.create_image(x,y,anchor=tk.NW,image=canvas.image)
    print(img.return_pil())

def KeyPress(event):
    if event.char == '-':
        img.zoom_out(1.1)
        update_canvas(img.x, img.y)

    if event.char == '=':
        img.zoom_in(1.1)
        update_canvas(img.x, img.y)

    if event.char == '0':
        img.zoom_reset()
        update_canvas(img.x, img.y)

def WKey(event):
    img.y = img.y  + 10
    update_canvas(img.x, img.y)

def AKey(event):
    img.x = img.x - 10
    update_canvas(img.x, img.y)

def SKey(event):
    img.y = img.y - 10
    update_canvas(img.x, img.y)

def DKey(event):
    img.x = img.x + 10
    update_canvas(img.x, img.y)


if __name__ == "__main__":
    root = tk.Tk()
    img = MyTkImage('labels.jpeg')

    root.bind("<w>", WKey)
    root.bind("<a>", AKey)
    root.bind("<s>", SKey)
    root.bind("<d>", DKey)

    root.bind('<KeyPress>', KeyPress)
    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()
    canvas.image = img.return_tk()
    canvas.image.x = 0
    canvas.image.y = 0
    canvas.create_image(0,0,anchor=tk.NW,image=canvas.image,\
                        tags='background')
    root.mainloop()