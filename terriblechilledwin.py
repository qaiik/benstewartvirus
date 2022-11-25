import tkinter
from PIL import Image, ImageTk
from pyautogui import grab
import glitch_this
import pyttsx3 as b
import PIL.ImageOps
from playsound import playsound as sound


class Displayer:
    def fitDisplay(self,pil_image,killafter):
        self.root = tkinter.Tk()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.focus_set()
        self.root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
        canvas = tkinter.Canvas(self.root, width=w, height=h, highlightthickness=0)
        canvas.pack()
        canvas.configure(background='black')

        img_width, img_height = pil_image.size
        ratio = min(w / img_width, h / img_height)
        img_width = int(img_width * ratio)
        img_height = int(img_height * ratio)
        pil_image = pil_image.resize((img_width, img_height), Image.ANTIALIAS)

        image = ImageTk.PhotoImage(pil_image)
        imagesprite = canvas.create_image(w / 2, h / 2, image=image)
        def kill():
            self.root.destroy()
            
        self.root.after(killafter,kill)
        self.root.mainloop()
    def say(self,text):
        engine = b.init()
        engine.say(text)
        engine.runAndWait()


def screenshot():
    return grab()

def distort(screenshot, lvl):
    return glitch_this.ImageGlitcher().glitch_image(screenshot, lvl)

def rotate(screenshot,by):
    return screenshot.rotate(by)

def gray(screenshot):
    return PIL.ImageOps.grayscale(screenshot)

def invert(screenshot):
    return PIL.ImageOps.invert(screenshot)



