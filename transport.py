from tkinter import *
import datetime
import time
def file_handel():
    Label(text="Congrats Your Request Has Been Submitted",fg="green").grid(row=9,column=2)

    l=datetime.datetime.now()
    if food.get()==1:
        j="they want food"
    else :
        j="they don't want food"
    with open("detail.txt","a") as f:
        f.writelines([f"\n \n \n date is {l}",f"\nthe name is {name.get()}","\n",f"phone no. is {phone.get()}",
                f"\nemergency contact is {eme.get()}",f"\ndestination and amount is{dest.get()},{amo.get()}"
                ,f"\n{j}"])
root=Tk()

root.geometry("544x344")
root.title("HIMANSHU_TRAVELS")
root.iconposition(120,6)
root.maxsize(544,344)

Label(
    text="Welcome To Himanshu Travels",font="latin 13 bold"
    ,bd=3,relief=SUNKEN
).grid(row=0,column=2)
Label(root,text=" NAME ",).grid(row=1,column=1,pady=10)
Label(root,text=" Phone No. ").grid(row=2,column=1,pady=5)
Label(root,text=" Emergency phone No.").grid(row=3,column=1,pady=5)
Label(root,text=" Destination ").grid(row=4,column=1,pady=5)
Label(root,text=" Amount Range ").grid(row=5,column=1,pady=5)

"""time for entry
"""
name=StringVar()
phone=StringVar()
eme=StringVar()
dest=StringVar()
amo=StringVar()
food=IntVar()
Entry(root,textvariable=name,selectbackground="green",width=30).grid(row=1,column=2)
Entry(root,textvariable=phone,selectbackground="green",width=30).grid(row=2,column=2)
Entry(root,textvariable=eme,selectbackground="green",width=30).grid(row=3,column=2)
Entry(root,textvariable=dest,selectbackground="green",width=30).grid(row=4,column=2)
Entry(root,textvariable=amo,selectbackground="green",fg="red",width=30).grid(row=5,column=2)

"""checkbutton"""
Checkbutton(root,text="Want Food",variable=food).grid(row=6,column=2)
"""button"""
Button(text="Submit",bd=3,relief="raised",bg="gray",
       command=file_handel).grid(row=8,column=2,pady=20)
root.mainloop()
