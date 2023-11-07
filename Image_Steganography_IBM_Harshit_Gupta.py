from tkinter import *
import random       #i used this for colour 
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk #it is for importing image for the device
from stegano import lsb #Least Significant Bit - It is a method of steganography, which is the practice of hiding one piece of information within another. Specifically, in the context of steganography with images, LSB steganography involves hiding data within the least significant bits of the pixel values of an image.
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)   

def animate_label_color(label):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    label.config(fg=random.choice(colors))
    root.after(500, lambda: animate_label_color(label))

root = Tk()
root.title("Hiding Message in an Image")
root.geometry("950x750")
root.resizable(False, False)

# Load the background image
bg_image = Image.open("bg111.png")  # Change this path to your image file
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label widget to display the background image
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Cover the entire window

root.iconbitmap(resource_path("assets/Logo.ico"))



def show_image():
    
    hint_label1.destroy()
    hint_label2.destroy()
    hint_label3.destroy()
    hint_label4.destroy()
    hint_label5.destroy()
    hint_label6.destroy()
    hint_label7.destroy()
    hint_label8.destroy()
    hint_label9.destroy()
    hint_label10.destroy()
    hint_label11.destroy()
    thank_you_label.destroy()
    thank_you_label1.destroy()

    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image",
        filetype=(
            ("Image Files", "*.png *.jpeg *.jpg *.bmp *.gif *.tiff"),
            ("All Files", "*.*")
        )
    )
    img = Image.open(filename)
    img = img.resize((450, 450), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

def hide_data():
    global secret
    message = text1.get(1.0, END)
    
    secret = lsb.hide(str(filename), message)

def show_data():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    if 'secret' in globals():
        secret.save(resource_path("Hidden.png"))
    else:
        
        print("No secret data to save.")


logo = PhotoImage(file=resource_path("assets/output-onlinepngtools.png"))
Label(root, image=logo, bg="#34495e").place(x=10, y=10)


Label(root, text="Hiding Message in an Image Project", bg="#34495e", fg="white", font="arial 15 bold").place(x=90, y=10)
Label(root, text="BY- HARSHIT GUPTA", bg="#34495e", fg="white", font="arial 15 bold").place(x=90, y=42)

#for left above container
f = Frame(root, bd=3, bg="#b2ebf2", width=450, height=450, relief=GROOVE)
f.place(x=17, y=80)

lbl = Label(f, bg="#2c3e50")
lbl.place(x=10, y=5)

frame2 = Frame(root, bd=3, width=450, height=450, relief=GROOVE, bg="#34495e")
frame2.place(x=480, y=80)

#for the text
text1 = Text(frame2, font="Roboto 14", bg="black", fg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=450, height=450)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=430, y=0, height=445)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3 = Frame(root, bd=3, bg="#2f4155", width=450, height=150, relief=GROOVE)
frame3.place(x=10, y=550)

 #Create the instruction label
hint_label1 = Label(f, text="INSTRUCTIONS FOR ENCRYPTING:", bg="#b2ebf2", fg="black", font="arial 10")
hint_label1.place(x=10, y=5)
hint_label1.config(font=("arial", 10, "underline"))

hint_label2 = Label(f, text="1. Click on the Open Image button", bg="#b2ebf2", fg="black", font="arial 10")
hint_label2.place(x=10, y=30)

hint_label3 = Label(f, text="2. Then click the black window and write the message", bg="#b2ebf2", fg="black", font="arial 10")
hint_label3.place(x=10, y=55)

hint_label4 = Label(f, text="3. Then click on hide message", bg="#b2ebf2", fg="black", font="arial 10")
hint_label4.place(x=10, y=80)

hint_label5 = Label(f, text="4. Save it", bg="#b2ebf2", fg="black", font="arial 10")
hint_label5.place(x=10, y=105)

hint_label6 = Label(f, text="5. Congratulations, you are done", bg="#b2ebf2", fg="black", font="arial 10")
hint_label6.place(x=10, y=130)

# Create the instruction labels for decrypting
hint_label7 = Label(f, text="INSTRUCTIONS FOR DECRYPTING:", bg="#b2ebf2", fg="black", font="arial 10")
hint_label7.place(x=10, y=155)
hint_label7.config(font=("arial", 10, "underline"))  # Underline the text

hint_label8 = Label(f, text="1. Click on the Open Image button to select the encrypted image.", bg="#b2ebf2", fg="black", font="arial 10")
hint_label8.place(x=10, y=180)

hint_label9 = Label(f, text="2. Click on 'Show Data' to decrypt the message from the image.", bg="#b2ebf2", fg="black", font="arial 10")
hint_label9.place(x=10, y=205)

hint_label10 = Label(f, text="3. The decrypted message will be displayed in the black window.", bg="#b2ebf2", fg="black", font="arial 10")
hint_label10.place(x=10, y=230)

hint_label11 = Label(f, text="4. Congratulations, you have successfully decrypted the message.", bg="#b2ebf2", fg="black", font="arial 10")
hint_label11.place(x=10, y=255)

# Create and place the "Thank You, IBM" label
thank_you_label = Label(root, text="This was completed during my internship at IBM", bg="#b2ebf2", fg="red", font="arial 10", relief="ridge", pady=10)
thank_you_label.place(x=25, y=400)

# Create and place the "Thank You, IBM" label
thank_you_label1 = Label(root, text="Thanks to them", bg="#b2ebf2", fg="red", font="arial 10", relief="ridge", pady=10)
thank_you_label1.place(x=25, y=440)

# Animate the "Thank You, IBM" label
animate_label_color(thank_you_label)
animate_label_color(thank_you_label1)


# Animate the "Thank You, IBM" label
animate_label_color(thank_you_label)



Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=show_image).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=230, y=30)

frame4 = Frame(root, bd=3, bg="#2f4155", width=450, height=150, relief=GROOVE)
frame4.place(x=480, y=550)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=hide_data).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=show_data).place(x=230, y=30)



root.mainloop()
