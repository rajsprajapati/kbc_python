from tkinter import *

#function for start game 

main_root=Tk()
main_root.title("Kon banega crorepati")

main_root.geometry('1100x600')
main_root.minsize(1100, 600)
main_root.maxsize(1100, 600)
#creating secondary loop
def start():
    #craeting fream
    second_root=Tk()
    second_root.title("Kon banega crorepati")
    second_root.geometry('1100x600')
    second_root.minsize(1100, 600)
        
    menubar=Menu(second_root)
    filemenu=Menu(menubar,tearoff=0)

    '''filemenu.add_command(label="---",command=quit)
    filemenu.add_command(label="New",command=quit)
    filemenu.add_command(label="Exit",command=exit)
    second_root.config(menu=menubar)
    menubar.add_cascade(label="File",menu=filemenu)'''


    
    f1=Frame(second_root,relief=SUNKEN, highlightbackground="black", highlightthickness=2,width=150,bg="#836FFF")
    f1.pack(side=LEFT, fill='y')

    f2=Frame(second_root, relief=SUNKEN, highlightbackground="black", highlightthickness=2,height=20,bg="#836FFF")
    f2.pack(side=TOP, fill="x")

    f3=Frame(second_root, relief=SUNKEN, highlightbackground="black", highlightthickness=2,width=150,height=50,bg="#836FFF")
    f3.pack()




    #creating label
    l=Label(f1,text="  Price Money  ",bg='white',fg='black',font="bold")
    l.pack()

    """l=Label(f1,text="  Price Money  ",bg='white',fg='black',font="bold")
    l.pack()"""

    l=Label(f2,text=" KBC ",bg='skyblue',fg='black',font="bold")
    l.pack()

    msg="Hello World!"
    #question=

    l=Label(f3,text=msg,bg='white',fg='black',font="bolditalic")
    l.pack(side=TOP,pady=30)

    button_option1=Button(second_root,text="button1",font="bold",bg="black",fg="white")
    button_option1.pack(side=LEFT,anchor="nw",padx=120,pady=120)

    button_option2=Button(second_root,text="button2",font="bold",bg="black",fg="white")
    button_option2.pack(side=RIGHT,anchor="ne",padx=120,pady=120)

    button_option3=Button(second_root,text="button3",font="bold",bg="black",fg="white")
    button_option3.pack(side=LEFT,anchor="sw",padx=120,pady=120)

    button_option4=Button(second_root,text="button4",font="bold",bg="black",fg="white")
    button_option4.pack(side=RIGHT,anchor="se",padx=120,pady=120)
    

    second_root.mainloop()

    def exit():
        main_root.destroy
        second_root.destroy

#adding image in bg

bg1 = PhotoImage(file="kbc2image.png")
labell=Label(main_root,image = bg1)
labell.place(x=0,y=0)
bg = PhotoImage(file="kbcimage.png")
label1=Label(main_root,image = bg,bg="black")
label1.place(x=430,y=150)


#creating button
button_open =Button(main_root,text="Start the Game",bg='black',fg='white',command=start)
button_open.pack(side=BOTTOM, anchor="ne",padx=500,pady=180)

button_close =Button(main_root,text="Exit the Game",bg='black',fg='white',command=exit)
button_close.pack(side=TOP, anchor="ne",padx=2,pady=7)


labletext=Label(main_root,text="Wellcome to Kon banega crorepati",font="bold",bg='black',fg="white")
labletext.pack()


main_root.mainloop()