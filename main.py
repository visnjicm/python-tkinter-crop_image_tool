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

    # reset image keybind
    if event.char == '0':
        img.zoom_reset()
        img.x, img.y = 0, 0
        update_canvas(img.x, img.y)


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
    # print(event)
    img.rect_x0 = event.x
    img.rect_y0 = event.y


def MiddleClick(event):
    # print(event)
    canvas.create_rectangle(img.rect_x0, img.rect_y0, img.rect_x1, img.rect_y1)
    # print(img.rect_x0, img.rect_y0, img.rect_x1, img.rect_y1)
    # print(img.x, img.y)
    cropped_coordinates = (img.rect_x0 - img.x, img.rect_y0 - img.y,
                           img.rect_x1 - img.x, img.rect_y1 - img.y)
    new_img = img.pil.crop(cropped_coordinates)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"files/output_{timestamp}.png"
    new_img.save(fp=file_path)


def RightClick(event):
    # print(event)
    img.rect_x1 = event.x
    img.rect_y1 = event.y


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
    canvas = tk.Canvas(root, width=1280, height=720)
    canvas.pack()
    canvas.image = img.return_tk()
    canvas.image.x = 0
    canvas.image.y = 0
    canvas.create_image(0, 0, anchor=tk.NW, image=canvas.image, tags='background')
    root.mainloop()
