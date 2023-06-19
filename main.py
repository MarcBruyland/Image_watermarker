from tkinter import *
# To get the dialog box to open when required
from tkinter import filedialog

# loading Python Imaging Library
from PIL import ImageTk, Image, ImageDraw, ImageFont

MIN_WINDOW_WIDTH = 1366
MIN_WINDOW_HEIGHT = 768
PADDING = 50
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300


def openfilename():
    #  open file dialog box to select image
    filename = filedialog.askopenfilename(title='Open')
    lbl_filename['text'] = filename
    return filename


def open_img():
    # PIL part: get PIL image
    x = openfilename()      # Select the Image-name from a folder
    img_pil_without_watermark = Image.open(x)     # opens the PIL image
    # resize the image and apply a high-quality down sampling filter
    img_pil_without_watermark = img_pil_without_watermark.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)

    # Tkinter part: PhotoImage class is used to add image to widgets, icons etc - show the image without watermark
    img_tk_without_watermark = ImageTk.PhotoImage(img_pil_without_watermark)      # Tkinter image without watermark
    # coordinates point to the center of the canvas
    canvas1.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=img_tk_without_watermark)
    # create a label
    label_img_tk_without_watermark = Label(window, image=img_tk_without_watermark)
    label_img_tk_without_watermark.image = img_tk_without_watermark
    label_img_tk_without_watermark.grid(row=3, column=0)


def add_watermark():
    # PIL part: get PIL image and add watermark
    img_pil_with_watermark = Image.open(lbl_filename['text'])    # PIL image
    # resize the image and apply a high-quality down sampling filter
    img_pil_with_watermark = img_pil_with_watermark.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
    draw = ImageDraw.Draw(img_pil_with_watermark)
    font = ImageFont.truetype("arial.ttf", 15)
    text = watermark_entry.get()
    draw.text((5, 5), text, font=font, align="left")

    # Tkinter part: image with watermark - show the image with watermark
    img_tk_with_watermark = ImageTk.PhotoImage(img_pil_with_watermark)
    # coordinates point to the center of the canvas
    canvas2.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=img_tk_with_watermark)
    label_img_tk_with_watermark = Label(window, image=img_tk_with_watermark)
    label_img_tk_with_watermark.image = img_tk_with_watermark
    label_img_tk_with_watermark.grid(row=3, column=1)


def save_image_with_watermark():
    # determine the filename for the watermarked PIL image (derived from old filename)
    filename = lbl_filename['text']
    lst = filename.split('.')
    filename = ""
    for i in range(len(lst)):
        if i < len(lst) - 1 :
            filename += lst[i] + '.'
        else:
            filename = filename[:-1]
            filename += "_with watermark." + lst[i]

    # PIL part: again, get the PIL image and add the watermark
    img_pil_with_watermark = Image.open(lbl_filename['text'])    # PIL image
    # resize the image and apply a high-quality down sampling filter
    img_pil_with_watermark = img_pil_with_watermark.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
    draw = ImageDraw.Draw(img_pil_with_watermark)
    font = ImageFont.truetype("arial.ttf", 15)
    text = watermark_entry.get()
    draw.text((5, 5), text, font=font, align="left")
    # save the watermarked PIL image with the new filename
    img_pil_with_watermark.save(filename)


def set_text(entry, text):
    entry.delete(0, END)
    entry.insert(0, text)
    return


# ---------------------------------------------------------------------------------
# Create a window
window = Tk()
window.title("Image Loader")                        # set title
window.minsize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT) # set the resolution of window
window.config(padx=PADDING, pady=PADDING)           # set the padding of the window
window.resizable(width=True, height=True)           # Allow Window to be resizable

# row 0
btn1 = Button(window, text='Open image', command=open_img)
btn1.grid(row=0, column=0, sticky='W')

lbl_filename = Label(window)
lbl_filename.grid(row=0, column=1, sticky='W')

# row 1
btn2 = Button(window, text='Add watermark', command=add_watermark)
btn2.grid(row=1, column=0, sticky='W')

watermark_entry = Entry(width=35)  # width is a property of Entry, not of grid !
watermark_entry.grid(row=1, column=1, sticky='W')
set_text(watermark_entry, "Marc")
watermark_entry.focus()

# row 2
btn3 = Button(window, text='Save image with watermark', command=save_image_with_watermark)
btn3.grid(row=2, column=1, sticky='W')

# row 3
canvas1 = Canvas(height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
canvas1.grid(row=3, column=0)

canvas2 = Canvas(height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
canvas2.grid(row=3, column=1)

window.mainloop()
