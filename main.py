import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageFont, ImageDraw


def watermark_text(input_img, output_img, text):
    # creates the image object
    original_img = Image.open(input_img)
    copy_img = original_img.copy()
    width, height = original_img.size
    # Draw on image
    water_mark = ImageDraw.Draw(copy_img)
    # set font
    font_size = int(width / 11)
    font = ImageFont.truetype("arial.ttf", font_size)
    x, y = int(width / 2), int(height / 1.5)
    # Adding watermark to image
    water_mark.text((x, y), text, font=font, fill="#FFF", stroke_width=3, stroke_fill="#222", anchor="ms")
    copy_img.save(output_img)


def watermark_img(input_img, output_img, logo_image):
    original_img = Image.open(input_img)
    # make a copy of the original image
    copy_img = original_img.copy()
    width, height = original_img.size
    x, y = int(width / 1.5), int(height / 2)
    logo = Image.open(logo_image)
    copy_img.paste(logo, (x, y))
    copy_img.save(output_img)


def first_image():
    path = filedialog.askopenfilename()
    entry1.delete(0, tkinter.END)
    entry1.insert(0, path)


def logo_img():
    path = filedialog.askopenfilename()
    entry2.delete(0, tkinter.END)
    entry2.insert(0, path)


def processed_img():
    path = filedialog.asksaveasfilename(defaultextension=".png")
    entry3.delete(0, END)
    entry3.insert(0, path)


def watermark():
    path1 = entry1.get()
    path2 = entry3.get()
    path3 = entry2.get()
    text = entry4.get()
    if not path1 or not path2 or (not text and not path1):
        messagebox.showerror("Error", "All needs to be filled")
        return
    if text:
        watermark_text(path1, path2, text)
    else:
        watermark_img(path1, path2, path3)
    messagebox.showinfo("Success", "Image Saved")


window = Tk()
window.title("Image Watermark")
window.minsize(width=500, height=300)

# original image frame
frame1 = Frame(window)
frame1.pack(pady=20)
# create first label on frame
label1 = Label(frame1, text="Image to Watermark:   ")
label1.pack(side="left", padx=10)
# create first entry on frame
entry1 = Entry(frame1, width=30)
entry1.pack(side="left")
# create first button on frame
button1 = Button(frame1, text="select file", width=20, command=first_image)
button1.pack(side="right", padx=10)


# Logo image frame
frame2 = Frame(window)
frame2.pack(pady=20)
# create second label on frame
label2 = Label(frame2, text="Logo to be watermarked:")
label2.pack(side="left", padx=10)
# create second entry on frame
entry2 = Entry(frame2, width=30)
entry2.pack(side="left")
# create second button on frame
button2 = Button(frame2, text="select file", width=20, command=logo_img)
button2.pack(side="right", padx=10)


# Save Watermarked Image
frame3 = Frame(window)
frame3.pack(pady=20)
# create third label on frame
label3 = Label(frame3, text="Save watermarked image:")
label3.pack(side="left", padx=10)
# create third entry on frame
entry3 = Entry(frame3, width=30)
entry3.pack(side="left")
# create third button on frame
button3 = Button(frame3, text="Save", width=20, command=processed_img)
button3.pack(side="right", padx=10)


frame4 = Frame(window)
frame4.pack(pady=20)
label4 = Label(frame4, text="Enter Text:")
label4.pack(side="left", padx=10)
entry4 = Entry(frame4, width=30)
entry4.pack(side="left")

# Run watermark button
button4 = Button(window, width=20, text="Watermark", command=watermark)
button4.pack(expand=True)

window.mainloop()
