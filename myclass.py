from PIL import Image, ImageTk


class MyTkImage:

    def __init__(self, fp: str):
        self.pil = Image.open(fp)
        self.tk_img = ImageTk.PhotoImage(Image.open(fp))

    def update_tk(self):
        self.tk_img = ImageTk.PhotoImage(self.pil)

    def zoom_in(self, factor: int):
        width = self.pil.width * factor
        height = self.pil.height * factor
        self.pil = self.pil.resize((width, height))
        self.update_tk()

    def zoom_out(self, factor: int):
        width = self.pil.width // factor
        height = self.pil.height // factor
        self.pil = self.pil.resize((width, height))
        self.update_tk()

    def return_pil(self):
        return self.pil

    def return_tk(self):
        return self.tk_img
