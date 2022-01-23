from tkinter import *
from tkinter import messagebox
password="iamkd"
attempt=0
root=Tk()
def pass_check():
    usrpass=e.get()
    global attempt
    global ln
    if password == usrpass:
        f1.destroy()
        f2 = LabelFrame(root, padx=260, pady=450)
        f2.pack()
        wl=Label(f2,text="WELCOME").pack()
    elif attempt<1:
        ln.destroy()
        messagebox.showinfo('info',"WRONG PASSWORD!")
        rn = Label(f1, text="RENTER PASSWORD").grid(row=0,column=0)
        attempt+=1
        e.delete(0,END)
    elif attempt<2:
        attempt+=1
        messagebox.showinfo('info', "WRONG PASSWORD!")
        e.delete(0, END)
    else:
        messagebox.showwarning("lock","MAXiMUM ATTEMPTS REACHED SYSTEM LOCKED!")
        root.quit()
f1=LabelFrame(root,padx=200,pady=400)
ln=Label(f1,text="ENTER PASSWORD")
ln.grid(row=0,column=0)
e=Entry(f1)
e.grid(row=1,column=0)
b=Button(f1,text="SUBMIT",command=pass_check).grid(row=2,column=0)
f1.pack()
root.mainloop()
