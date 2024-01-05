import tkinter as tk
from myclass import MyTkImage
from datetime import datetime
import sys


def update_canvas(x, y):
    canvas.delete('background')
    canvas.image = img.return_tk()
    canvas.create_image(x, y, anchor=tk.NW, image=canvas.image)
    # print(800 - img.pil.width, 600 - img.pil.height)
    # print(x, y)
    # print(img.return_pil())


def KeyPress(event):
    # zoom out keybind
    if event.char == '-':
        img.zoom_out(1.3)
        update_canvas(img.x, img.y)

    # zoom in keybind
    if event.char == '=':
        img.zoom_in(1.3)
        update_canvas(img.x, img.y)

    # reset keybind
    if event.char == '0':
        img.zoom_reset()
        img.x, img.y = 0, 0
        img.rect_x0, img.rect_x1 = None, None
        img.rect_y0, img.rect_y1 = None, None
        update_canvas(img.x, img.y)

def draw_rectangle(event):
    if img.rect_x0 is not None and img.rect_y0 is not None\
            and img.rect_x1 is None and img.rect_y1 is None:
        canvas.delete('rectangle')
        canvas.create_rectangle(img.rect_x0, img.rect_y0, event.x, event.y,
                                tags='rectangle')




def WKey(event):
    img.y += 20
    if 0 > img.y > (720 - img.pil.height):
        update_canvas(img.x, img.y)
    else:
        img.y -= 20


def AKey(event):
    img.x -= 20
    if 0 > img.x > (1280 - img.pil.width):
        update_canvas(img.x, img.y)
    else:
        img.x += 20


def SKey(event):
    img.y -= 20
    if 0 > img.y > (720 - img.pil.height):
        update_canvas(img.x, img.y)
    else:
        img.y += 20


def DKey(event):
    img.x += 20
    if 0 > img.x > (1280 - img.pil.width):
        update_canvas(img.x, img.y)
    else:
        img.x -= 20


def LeftClick(event):
    img.rect_x0 = event.x
    img.rect_y0 = event.y
    img.rect_x1 = None
    img.rect_y1 = None


def MiddleClick(event):

    print(img.rect_x0, img.rect_y0, img.rect_x1, img.rect_y1)

    if img.rect_y0<img.rect_y1:
        upper = img.rect_y0
        lower = img.rect_y1
    else:
        upper = img.rect_y1
        lower = img.rect_y0

    if img.rect_x0 < img.rect_x1:
        left = img.rect_x0
        right = img.rect_x1
    else:
        left = img.rect_x1
        right = img.rect_x0

    new_img = img.pil.crop((left,upper,right,lower))

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"files/output_{timestamp}.png"

    new_img.save(fp=file_path)

    update_canvas(img.x, img.y)


def RightClick(event):
    canvas.delete('rectangle')
    img.rect_x1 = event.x
    img.rect_y1 = event.y
    canvas.create_rectangle(img.rect_x0, img.rect_y0,
                            img.rect_x1, img.rect_y1, tags='rectangle')


if __name__ == "__main__":
    file_path = sys.argv[1]
    root = tk.Tk()
    img = MyTkImage(file_path)

    root.bind("<w>", WKey)
    root.bind("<a>", AKey)
    root.bind("<s>", SKey)
    root.bind("<d>", DKey)
    root.bind("<Button-1>", LeftClick)
    root.bind("<Button-2>", MiddleClick)
    root.bind("<Button-3>", RightClick)
    root.bind('<KeyPress>', KeyPress)
    root.bind('<Motion>', draw_rectangle)




    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()
    canvas.image = img.return_tk()
    canvas.image.x = 0
    canvas.image.y = 0
    canvas.create_image(0, 0, anchor=tk.NW, image=canvas.image, tags='background')
    root.mainloop()
