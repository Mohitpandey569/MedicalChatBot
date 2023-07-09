import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="pink")
root.geometry("300x200")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Voice Based Medical Assistant Chatbot")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('b1.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


#
label_l2 = tk.Label(root, text="Voice Based Medical Assistant Chatbot",font=("times", 30, 'bold','italic'),
                    background="green", fg="white", width=70, height=2)
label_l2.place(x=0, y=0)

#logo

img = Image.open('logo.jpg')
img = img.resize((100,75), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)

logo_label.image = logo_image
logo_label.place(x=21, y=10)


# label image
img1 = Image.open('r2.jpg')
img1 = img1.resize((600,650), Image.ANTIALIAS)
logo_image1 = ImageTk.PhotoImage(img1)

logo_label1 = tk.Label(root, image=logo_image1,bd=5 )
logo_label1.image = logo_image1
logo_label1.place(x=40, y=130)


frame_alpr = tk.LabelFrame(root, text=" --Details-- ", width=680, height=630, bd=5, font=('times', 14, ' bold '),bg="pink")
frame_alpr.place(x=640, y=130)



# label_l2 = tk.Text(root,font=("Times New Roman", 15, 'italic'),
#                     background="#220A29", fg="white", width=72, height=29)
# label_l2.place(x=840, y=130)






img = Image.open('r1.jpg')
img = img.resize((200,150), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(frame_alpr, image=logo_image)

logo_label.image = logo_image
logo_label.place(x=220,y=50)

label_l2 = tk.Label(root,text="Voice Based Medical Assistant Chatbot",font=("Times New Roman",20, 'bold','italic'),
                    background="pink", fg="black")
label_l2.place(x=750, y=380)
    
def window():
  root.destroy()
  
  
def log():
    from subprocess import call
    call(["python","login.py"])
  
def register():
    from subprocess import call
    call(["python","registration.py"])
    
    
    

    
button1 = tk.Button(frame_alpr, text="LOGIN", command=log, width=12, height=1,font=('times 15 bold italic '),bd=5, bg="blue", fg="white")
button1.place(x=250, y=400)

button2 = tk.Button(frame_alpr, text="REGISTER",command=register,width=12, height=1,font=('times 15 bold italic'), bd=5,bg="blue", fg="white")
button2.place(x=250, y=300)

button4 = tk.Button(frame_alpr, text="EXIT", command=window, width=12, height=1,font=('times 15 bold italic'),bd=5,bg="red", fg="white")
button4.place(x=250, y=500)




label_l1 = tk.Label(root, text="** Mental Healthcare Chatbot System @ 2021 by _____ **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=250, height=2)
label_l1.place(x=0, y=798)



root.mainloop()