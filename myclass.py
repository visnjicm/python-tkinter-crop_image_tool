from PIL import Image, ImageTk


class MyTkImage:

    def __init__(self, fp: str):
        self.fp = fp
        self.pil = Image.open(fp)
        self.tk_img = ImageTk.PhotoImage(Image.open(fp))

    def update_tk(self):
        self.tk_img = ImageTk.PhotoImage(self.pil)

    def zoom_in(self, factor: float):
        width = round(float(self.pil.width) * factor)
        height = round(float(self.pil.height) * factor)
        self.pil = self.pil.resize((width, height))
        self.update_tk()

    def zoom_out(self, factor: int):
        width = self.pil.width // factor
        height = self.pil.height // factor
        self.pil = self.pil.resize((width, height))
        self.update_tk()

    def zoom_reset(self):
        self.pil = Image.open(self.fp)
        self.update_tk()

    def return_pil(self):
        return self.pil

    def return_tk(self):
        return self.tk_img
