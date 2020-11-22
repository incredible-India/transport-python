from tkinter import *
from tkinter.ttk import  Combobox
import tkinter.messagebox as hj
from googletrans import Translator,LANGUAGES
from gtts import gTTS
import os
from tkinter import colorchooser



p=["Hindi","English","Punjabi","Marathi","Malayalam","Kannada"
    ,"Gujarati","Tamil","Telugu","Bengali","Urdu",
   "Albanian","Italian","Dutch"
    ,"Romanian" ,
   "Japanese","French","Spanish","Greek",
   "Filipino","Persian","Nepali","Thai","Latin","Russian","German"
   ,"Chinese","Uzbek","Afrikaans","Arabic"]

root=Tk()

"""fn"""
def clear_me():
    t1.delete(1.0,END)
    pass
def clear_me2():
    t2.delete(1.0,END)
    pass

def converti():

    if combo.get()=="Convert in":
        hj.showerror("Empty Selection","Please select the Languages in which you want to\n convert ")

    elif combo.get()==p[0]:
            de="hi"

    elif combo.get() == p[1]:
        de = "en"

    elif combo.get() == p[2]:
        de = "pa"

    elif combo.get() == p[3]:
        de = "mr"

    elif combo.get() == p[4]:
        de = "ml"

    elif combo.get() == p[5]:
        de= "kn"

    elif combo.get() == p[6]:
        de = "gu"

    elif combo.get() == p[7]:
        de = "ta"

    elif combo.get() == p[8]:
        de = "te"

    elif combo.get() == p[9]:
        de = "bn"

    elif combo.get() == p[10]:
        de = "ur"

    elif combo.get() == p[11]:
        de = "sq"

    elif combo.get() == p[12]:
        de = "it"

    elif combo.get() == p[13]:
        de = "nl"

    elif combo.get() == p[14]:
        de= "ro"

    elif combo.get() == p[15]:
        de = "ja"

    elif combo.get() == p[16]:
        de = "fr"

    elif combo.get() == p[17]:
        de = "es"

    elif combo.get() == p[18]:
        de = "el"

    elif combo.get() == p[19]:
        de = "tl"

    elif combo.get() == p[20]:
        de = "fa"

    elif combo.get() == p[21]:
        de = "ne"

    elif combo.get() == p[22]:
        de = "th"

    elif combo.get() == p[23]:
        de = "la"

    elif combo.get() == p[24]:
        de = "ru"

    elif combo.get() == p[25]:
        de = "de"

    elif combo.get() == p[26]:
        de = "zn"

    elif combo.get() == p[27]:
        de= "uz"

    elif combo.get() == p[28]:
        de = "af"

    elif combo.get() == p[29]:
        de = "ar"




    return  de



"""src fn"""


def convertio(a,b,c):
    if var.get()=="":
        print("hey")
    elif var.get()==p[0]:
        sourc="hi"

    elif var.get()==p[1]:
        sourc="en"

    elif var.get()==p[2]:
        sourc="pa"

    elif var.get()==p[3]:
        sourc="mr"

    elif var.get()==p[4]:
        sourc="ml"

    elif var.get()==p[5]:
        sourc="kn"

    elif var.get()==p[6]:
        sourc="gu"

    elif var.get()==p[7]:
        sourc="ta"

    elif var.get()==p[8]:
        sourc="te"

    elif var.get()==p[9]:
        sourc="bn"

    elif var.get()==p[10]:
        sourc="ur"

    elif var.get()==p[11]:
        sourc="sq"

    elif var.get()==p[12]:
        sourc="it"

    elif var.get()==p[13]:
        sourc="nl"

    elif var.get()==p[14]:
        sourc="ro"

    elif var.get()==p[15]:
        sourc="ja"

    elif var.get()==p[16]:
        sourc="fr"

    elif var.get()==p[17]:
        sourc="es"

    elif var.get() == p[18]:
        sourc = "el"

    elif var.get() == p[19]:
        sourc = "tl"

    elif var.get() == p[20]:
        sourc = "fa"

    elif var.get() == p[21]:
        sourc = "ne"

    elif var.get() == p[22]:
        sourc = "th"

    elif var.get() == p[23]:
        sourc = "la"

    elif var.get() == p[24]:
        sourc = "ru"

    elif var.get() == p[25]:
        sourc = "de"

    elif var.get() == p[26]:
        sourc = "zn"

    elif var.get() == p[27]:
        sourc = "uz"

    elif var.get() == p[28]:
        sourc = "af"

    elif var.get() == p[29]:
        sourc = "ar"



    return sourc

"""return converts fn"""



def transd():
    from datetime import datetime

    try:
        k=convertio(1,1,1)
        l=converti()

        trans=Translator()
        p=trans.translate(str(t1.get(1.0,END)),
                          src=k,dest=l)
        t2.insert(INSERT,f"{str(p.text)} \n")
    except Exception as e:
        hj.showerror("NO Connection","404 Error\nPlease connect to the internet ")
        pass
    with open("history.txt", "a") as c:
        c.writelines([f" \nTIME : {datetime.now()} \n {str(t1.get(1.0, END))}  "])



"""speak original"""
def speak():
    try:
        k=gTTS(text=str(t1.get(1.0,END)),slow=False)
        k.save("speak.mp3")
        os.system("speak.mp3")
        os.remove("speak.mp3")
    except Exception as e:
        hj.showerror("Connection lost","Please connect  your device the internet service ")




"""speak final"""
def speak11():
    try:
        k=gTTS(text=str(t2.get(1.0,END)),slow=False)
        k.save("speak.mp3")
        os.system("speak.mp3")
        os.remove("speak.mp3")
    except Exception as e:
        hj.showerror("Connection lost","Please connect  your device the internet service ")


"""fns for menu"""


def colorc():
    k=colorchooser.askcolor(title="Select the color")
    root.configure(background=f"{k[1]}")

def supported():

    k=Toplevel()


    l = Listbox(k,bg="pink",font="time 12 bold")
    for i in LANGUAGES:
        l.insert(END,LANGUAGES[i])


    l.pack(expand=True,fill=BOTH)
    sc=Scrollbar(l)
    sc.configure(command=l.yview)
    l.config(yscrollcommand=sc.set)
    sc.pack(side="right",fill=Y)
def currentl():

    k=Toplevel()

    l = Listbox(k,bg="gray",font="time 12 bold")

    l.insert(END,*p)

    l.pack(expand=TRUE,fill=BOTH)


def helpi():
    helo=["1: for this you need to internet connection ",
          "2:there are two text widget ",""
    "3: from left side text box will take the words(sentences) to convert"
          ,"4: right side's text box will show converted word(sentences)"
          ,"5: after giving input select the language formate",
          "6: and then select the language in which u have to select ",
          "7: and finally click \"convert\" button ",
          "8:the are two speak button simply click them ",
          "9 first one will speak entered words(sentences)",
          "10: secone one will speak converted words(sentences)"]
    k = Toplevel(width=300,height=100)

    l = Listbox(k, bg="gray", font="time 12 bold")

    l.insert(END, *helo)

    l.pack(expand=True,fill=BOTH)
    sc = Scrollbar(l)
    sc.configure(command=l.yview)
    l.config(yscrollcommand=sc.set)
    sc.pack(side="right", fill=Y)


def hist():
    with open("history.txt") as c:
       i=c.readlines()
    k = Toplevel(width=300, height=100)

    l = Listbox(k, bg="gray", font="time 12 bold")

    l.insert(END, *i)

    l.pack(expand=True,fill=BOTH)
    sc = Scrollbar(l)
    sc.configure(command=l.yview)
    l.config(yscrollcommand=sc.set)
    sc.pack(side="right", fill=Y)

"""root"""


root.geometry("1500x800")
root.configure(bg="#808080")
root.title("Third party Translator")

var=StringVar()
var1=StringVar()
"""mainmenu"""



mainmenu=Menu(root,)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Supported Languages",activebackground="gray",command=supported)
m1.add_command(label="Change background color",activebackground="gray",command=colorc)
m1.add_command(label="History",activebackground="gray",command=hist)
m1.add_command(label="Save this words",activebackground="gray")
m1.add_command(label="Open Saved word",activebackground="gray",activeforeground="Blue"
               ,command=hist)
m1.add_command(label="Help",activebackground="gray",command=helpi)
m1.add_separator()
m1.add_command(label="Exit",activebackground="black",command=exit)

mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="Current Language",command=currentl)
mainmenu.add_command(label="Exit",activebackground="pink",command=quit)

root.configure(menu=mainmenu)


"""status bar"""



f1=Frame(
    bg="#969696",height=23
)
f1.pack(side=BOTTOM,fill=X)


"""
text widget"""



f2=Frame(root,bg="gray")
f2.pack(anchor="nw",side=LEFT,padx=10)

f3=Frame(root,bg="gray")
f3.pack(anchor="ne",side=LEFT,padx=10)





scrollbar1=Scrollbar(f3)
scrollbar1.pack(side=LEFT,fill=Y,pady=10)


scrollbar=Scrollbar(f2)
scrollbar.pack(side=LEFT,fill=Y,pady=10)

t1=Text(f2,bg="#969696",font="lucida ",wrap=WORD,width=50,padx=10,pady=10,
        selectbackground="#282828"
        ,selectforeground="white",
bd=5,relief=SUNKEN,yscrollcommand=scrollbar.set)

scrollbar.configure(command=t1.yview)
t1.pack(anchor="nw",side=LEFT,pady=10,padx=10)
t1.insert(INSERT,"Text here....")

t2=Text(f3,bg="#969696",font="lucida ",
        width=50,wrap=WORD,padx=10,pady=10,selectbackground="#282828"
        ,selectforeground="white",
        bd=5,relief=SUNKEN,yscrollcommand=scrollbar1.set)
t2.pack(anchor="nw",side=RIGHT,pady=10,padx=10)

scrollbar1.configure(command=t2.yview)

"""option menu"""



var.set("Languages (from)")

OptionMenu(root,var,*p).pack(padx=10,pady=40,fill=BOTH)
Label(text="To",font="arial 12 bold",bg="gray").pack(fill=BOTH)
combo=Combobox(root,value=p)
combo.pack(padx=10,pady=40,fill=BOTH)
combo.set("Convert in")
var.trace("w",convertio)
"""buttons"""
b1=Button(f2,text="Clear",bg="gray",bd=3,relief=SUNKEN,padx=10,anchor="w",command=clear_me)
b1.pack(anchor="sw",side=BOTTOM,fill=BOTH)

convert=Button(root,text="Convert",bd=2,relief=SUNKEN,bg="green",padx=15,command=transd)
convert.pack(anchor=CENTER,pady=40,)


speai=Button(root,text="Speak Original",bd=2,relief=SUNKEN,bg="pink",padx=15,command=speak)
speai.pack(anchor=CENTER,pady=40,)

speak1=Button(root,text="Speak Final ",bd=2,relief=SUNKEN,bg="pink",padx=15,command=speak11)
speak1.pack(anchor=CENTER,pady=40,)


root.mainloop()