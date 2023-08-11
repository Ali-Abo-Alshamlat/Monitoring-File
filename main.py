from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as scrol
import os
import time
import threading

root = Tk()
root.geometry('800x500')
root.title('Security File')
root.configure(background='whitesmoke')
root.iconbitmap('')

#===== Function =====
def openfile () :
    global of
    of = filedialog.askopenfilename(
        initialdir="C:/Users/",
        title = '[Ali] open file',
        filetypes = (("Text Files", "*.txt"),)
    )
    en1.insert(END,of)
    global file_size1
    file_size1 = os.path.getsize(of)
    en2.insert(END,file_size1)

def sec() :
    while True :
        new_path = of
        size = os.path.getsize(new_path)
        if file_size1 == size :
            txt.insert('end','✅','black')
            txt.insert('end','Health File is : ','green')
            txt.insert('end',time.ctime(),'black')
            txt.insert('end','\n\n')
            get_time = int(en3.get()) 
            time.sleep(get_time)
            continue
        else:
            txt.insert('end','[X]','black')
            txt.insert('end','There Hackers :','red')
            txt.insert('end',time.ctime(),'black')
            txt.insert('end','\n\n')
            break
def go() :
    threading.Thread(target=sec).start()

#===== Tittle Top =====
tittle = Label(root,
               text='Monitoring File',
               font=('Courier',18),
               bg='#5D9C59',
               fg='white'
               )
tittle.pack(fill=X)

#==== Image Logo ====
pic = PhotoImage(file='file.png')
ph = Label(root, image=pic)
ph.place(y=33,width='300',height='150')

#==== Button ====
button=Button(root, 
              text='Select File',
              width=25,
              heigh=2,
              cursor='hand2',
              fg='white',
              bg='#5D9C59',
              bd=0,relief=RIDGE,command=openfile
              )
button.place(x=40,y=200)

#==== Entry path ====
en1 = Entry(root,font=('Courier',10))
en1.place(x=48,y=240)


#==== Frame label with entry ====
f2 = Frame(root,width=260,heigh=210,bg='white',bd=0,relief=GROOVE)
f2.place(x=12,y=265)

L1 = Label(f2, text="File Options :",bg='white',fg='blue',font=('Courier',15))
L1.place(x=5,y=10)

L2 = Label(f2, text="File Size :",bg='white',fg='red',font=('Courier',10))
L2.place(x=14,y=45)
en2 = Entry(f2,font=('Courier',11),justify=CENTER)
en2.place(x=15,y=80,width=80,height=35)

L3 = Label(f2, text="Set Time :",bg='white',fg='red',font=('Courier',10))
L3.place(x=144,y=45)
en3 = Entry(f2,font=('Courier',11),justify=CENTER)
en3.place(x=144,y=80,width=80,height=35)

L4 = Label(f2, text="Start to secure your file :",bg='white',fg='black',font=('Courier',10))
L4.place(x=10,y=110)

B1 = Button(f2, text='Start Scan',
            border='10',
            cursor='hand2',
            width=10,bd=0,relief=RIDGE,bg='green',command=go)
B1.place(x=70,y=140)

#==== Text and scroll for results ====
txt= scrol.ScrolledText(root,bg='white')
txt['font']=('Courier','12')
txt.place(x=300,y=33,width=560,heigh=480)
txt.tag_config('green',background='green',foreground='white')
txt.tag_config('black',background='white',foreground='black')
txt.tag_config('red',background='green',foreground='white')
root.mainloop()