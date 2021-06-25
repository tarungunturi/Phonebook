from Tkinter import *
root=Tk()
root.geometry('1000x200')
Label(root,text='Project Title:PHONEBOOK',font='Times 20 bold',fg='#123456').grid(row=0,column=0)
Label(root,text='Project Of Python And Database',font='Times 20 bold',fg='#123456').grid(row=1,column=1)
Label(root,text='Developed By :TARUN GUNTURI(181B228)',font='Times 20 bold',fg='#123456').grid(row=2,column=1)
Label(root,text='---------------------------------------------',fg='#123456').grid(row=3,column=1)
Label(root,text='Make mouse moment over this screen to close',font='times 15 bold').grid(row=4,column=1)
def close(e=1):
    root.destroy()
root.bind('<Motion>',close)
root.mainloop()
    
