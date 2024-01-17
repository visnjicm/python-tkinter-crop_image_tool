import tkinter as tk
from datetime import datetime
from MyTkImage import MyTkImage


class TkinterApp():
    image_path = "labels.jpeg"

    def _update_canvas(self):
        self.canvas.delete('background')
        self.canvas.image = self.img.return_tk()
        self.canvas.create_image(self.img.x, self.img.y, anchor=tk.NW, image=self.canvas.image, tags='background')

    def _draw_rectangle(self):
        self.canvas.create_rectangle(self.rect_x0, self.rect_y0, self.rect_x1, self.rect_y1, tags="rectangle")

    def _key_press(self, event):
        if event.char == '-' or event.char == "_":
            self.img.zoom_out(1.3)

        if event.char == '=' or event.char == "+":
            self.img.zoom_in(1.3)

        if event.char == '0' or event.char == ')':
            self.img.zoom_reset()
            self.canvas.delete("rectangle")
            self.x0_y0_set = False
            self.x1_y1_set = False
            self.img.x, self.img.y = 0, 0

        if event.char == 'w' or event.char == 'W':
            self.img.y += 20
            if 0 > self.img.y > (720 - self.img.pil.height):
                pass
            else:
                self.img.y -= 20

        if event.char == 'a' or event.char == 'A':
            self.img.x -= 20
            if 0 > self.img.x > (1280 - self.img.pil.width):
                pass
            else:
                self.img.x += 20

        if event.char == 's' or event.char == 'S':
            self.img.y -= 20
            if 0 > self.img.y > (720 - self.img.pil.height):
                pass
            else:
                self.img.y += 20

        if event.char == 'd' or event.char == 'D':
            self.img.x += 20
            if 0 > self.img.x > (1280 - self.img.pil.width):
                pass
            else:
                self.img.x -= 20

        self._update_canvas()

    def _left_click(self, event):
        self.canvas.delete("rectangle")
        self.x0_y0_set = False
        self.x1_y1_set = False
        self.rect_x0 = event.x
        self.rect_y0 = event.y
        self.x0_y0_set = True

    def _mouse_motion(self, event):
        if self.x0_y0_set == True and self.x1_y1_set == False:
            self.canvas.delete("rectangle")
            self.canvas.create_rectangle(self.rect_x0, self.rect_y0, event.x, event.y, tags="rectangle")

    def _middle_click(self, event):
        print(self.rect_x0, self.rect_y0, self.rect_x1, self.rect_y1)
        print(self.img.x, self.img.y)
        cropped_coordinates = (self.rect_x0 - self.img.x, self.rect_y0 - self.img.y,
                               self.rect_x1 - self.img.x, self.rect_y1 - self.img.y)
        new_img = self.img.pil.crop(cropped_coordinates)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = f"files/output_{timestamp}.png"
        new_img.save(fp=file_path)
        self._update_canvas()
        self.x0_y0_set = False
        self.x1_y1_set = False

    def _right_click(self, event):
        self.rect_x1 = event.x
        self.rect_y1 = event.y
        self.x1_y1_set = True
        self.canvas.delete("rectangle")
        self._draw_rectangle()

    def __init__(self):
        self.root = tk.Tk()
        self.root.bind("<Button-1>", self._left_click)
        self.root.bind("<Button-2>", self._middle_click)
        self.root.bind("<Button-3>", self._right_click)
        self.root.bind('<KeyPress>', self._key_press)
        self.root.bind('<Motion>', self._mouse_motion)

        self.img = MyTkImage(self.image_path)
        self.canvas = tk.Canvas(self.root, width=1280, height=720)
        self.canvas.pack()
        self.canvas.image = self.img.return_tk()
        self.canvas.image.x = 0
        self.canvas.image.y = 0
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.canvas.image, tags='background')

        self.rect_x0 = None
        self.rect_x1 = None
        self.rect_y0 = None
        self.rect_y1 = None

        self.x0_y0_set = False
        self.x1_y1_set = False
