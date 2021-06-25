from Tkinter import *
from tkMessageBox import *
import sqlite3
import tkFont
from splashscreen import *
con=sqlite3.Connection('Phonebook3')
cur=con.cursor()
cur.execute("PRAGMA foreign_keys=ON")
cur.execute('create table if not exists contact_details(contact_id integer primary key autoincrement,first_name varchar(15),m_name varchar(15),last_name varchar(15),company varchar(20),address varchar(50),city varchar(15),pin number(6),website varchar(50),birth_date varchar(20))')
cur.execute('create table if not exists number(contact_id integer,contact_type varchar(10),phone_number number(10),primary key(contact_id,phone_number),foreign key (contact_id) references contact_details (contact_id) on delete cascade)')
cur.execute('create table if not exists email (contact_id integer, emailid_type varchar(10),email_id varchar(50),primary key (contact_id,email_id),foreign key (contact_id) references contact_details (contact_id) on delete cascade)')

root=Tk()
root.title('Phone Book')
a=PhotoImage(file='phonebook1.gif')
root.configure(background='#A6B7C8')
Label(root,image=a).grid(row=0,column=2)
Label(root,text='Phone Book',font='arial 20',foreground='blue').grid(row=1,column=2)
Label(root,text='First Name',font='italic 15').grid(row=2,column=1)
e1=Entry()
e1.grid(row=2,column=2)
Label(root,text='Middle Name',font='italic 15').grid(row=3,column=1)
e2=Entry()
e2.grid(row=3,column=2)
Label(root,text='Last Name',font='italic 15').grid(row=4,column=1)
e3=Entry()
e3.grid(row=4,column=2)
Label(root,text='Company Name',font='italic 15').grid(row=5,column=1)
e4=Entry()
e4.grid(row=5,column=2)
Label(root,text='Address',font='italic 15').grid(row=6,column=1)
e5=Entry()
e5.grid(row=6,column=2)
Label(root,text='City',font='italic 15').grid(row=7,column=1)
e6=Entry()
e6.grid(row=7,column=2)
Label(root,text='Pin Code',font='italic 15').grid(row=8,column=1)
e7=Entry()
e7.grid(row=8,column=2)
Label(root,text='Website URL',font='italic 15').grid(row=9,column=1)
e8=Entry()
e8.grid(row=9,column=2)
Label(root,text='Date Of Birth',font='italic 15').grid(row=10,column=1)
e9=Entry()
e9.grid(row=10,column=2)
Label(root,text='Select phone type',font='italic 15',foreground='blue').grid(row=11,column=1)
v1=IntVar()
R1=Radiobutton(root,text='office',variable=v1,value=1).grid(row=11,column=2)
R2=Radiobutton(root,text='Home',variable=v1,value=2).grid(row=11,column=3)
R3=Radiobutton(root,text='Mobile',variable=v1,value=3).grid(row=11,column=4)
Label(root,text='Phone number',font='italic 15').grid(row=12,column=1)
e10=Entry()
e10.grid(row=12,column=2)
def add():
    d={1:'Office',2:'Home',3:'Mobile'}
    e={1:'Office',2:'Personal'}
    if (len(e1.get())== 0 and len(e2.get())== 0 and len(e3.get())== 0 and len(e4.get())== 0 and len(e5.get())== 0 and len(e6.get())== 0 and len(e7.get())== 0 and len(e8.get())== 0 and len(e9.get())== 0 and len(e10.get())== 0 and len(e12.get())== 0):
        showerror('Error','No Value is Entered')
    else:    
        a=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
        cur.execute("insert into contact_details(first_name,m_name,last_name,company,address,city,pin,website,birth_date) values(?,?,?,?,?,?,?,?,?)",a)
        cur.execute("select contact_id curval from contact_details")
        ab=cur.fetchall()
        le=len(ab)-1
        b=(ab[le][0],d.get(v1.get()),e10.get())
        cur.execute("insert into number(contact_id,contact_type,phone_number) values (?,?,?)",b)
        c=(ab[le][0],e.get(v2.get()),e12.get())
        cur.execute("insert into email(contact_id,emailid_type,email_id) values (?,?,?)",c)
        
        con.commit()
        
        showinfo('Save','Contact Saved Successfully')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e12.delete(0,END)
        v1.set(0)
        v2.set(0)
        
def exit():
    root.destroy()
def search():
    root1=Tk()
    root1.geometry("550x700")
    root1.title("Search")
    Label(root1,text='Searching Phonebook',font='arial 20',background='green').grid(sticky=W+E+N+S)
    Label(root1,text='Enter Name',font='arial 15').grid(row=1,column=0,columnspan= 5, sticky=W)
    e11=Entry(root1)
    e11.grid(row=1,column=0)
    lb=Listbox(root1,height='35',width='90',background='LIGHT GREY',fg='BLUE')
    lb.grid()
    cur.execute("select contact_id,first_name,m_name,last_name from contact_details ")
    s=cur.fetchall()
    global az
    az=s
    def showvalue(e=1):
        #u=unicode(e11.get())
        #u=("%"+u+"%")
        lb.delete(0,END)
        global az
        cur.execute("select contact_id,first_name,m_name,last_name from contact_details where (first_name like (?) or m_name like (?) or last_name like (?))order by first_name,m_name,last_name",("%"+e11.get()+"%","%"+e11.get()+"%","%"+e11.get()+"%"))
        az=cur.fetchall()
        for i in range(len(az)):
            lb.insert(i,az[i][1]+" "+az[i][2]+" "+az[i][3])

    
    def click(e=1):
        
        
        
        def delete():
            cur.execute("delete from contact_details where contact_id =?",(iq,))
            cur.execute("delete from number where contact_id =?",(iq,))
            cur.execute("delete from email where contact_id =?",(iq,))
            con.commit()
            showinfo('Delete','Contact Removed Successfully')
            close()
        Button(root1,text="Delete",command=delete).grid(row=3,column=0,sticky=E+N+S)

        temp=lb.curselection()
        global az
        
        iq=az[temp[0]][0]
        
    
        cur.execute("select first_name,m_name,last_name,company,address,city,pin,website,birth_date from contact_details where contact_id=?",(iq,))
        li1= cur.fetchall()
        cur.execute("select contact_type,phone_number from number where contact_id =?",(iq,))
        li2=cur.fetchall()
        cur.execute("select emailid_type,email_id from email where contact_id=?",(iq,))
        li3=cur.fetchall()
        
        lb.delete(0,END)
        lb.insert(0,"FIRST NAME     :" + (str)(li1[0][0]))
        lb.insert(1,"MIDDLE NAME    :" + (str)(li1[0][1]))
        lb.insert(2,"LAST NAME      :" + (str)(li1[0][2]))
        lb.insert(3,"COMPANY        :" + (str)(li1[0][3]))
        lb.insert(4,"ADDRESS        :" + (str)(li1[0][4]))
        lb.insert(5,"CITY           :" + (str)(li1[0][5]))
        lb.insert(6,"PIN            :" + (str)(li1[0][6]))
        lb.insert(7,"WEBSITE URL    :" + (str)(li1[0][7]))
        lb.insert(8,"DATE OF BIRTH  :" + (str)(li1[0][8]))

        lb.insert(9,"PHONE DETAILS..........")
        lb.insert(10,(str)(li2[0][0])+"   :"+(str)(li2[0][1]))

        lb.insert(11,"EMAIL ADDRESSES.......")
        lb.insert(12,(str)(li3[0][0])+"    :"+(str)(li3[0][1]))

    #entering values in listbox when entry is empty
    cur.execute("select contact_id curval from contact_details")
    b= cur.fetchall()
    l=len(b)
        
    
    
    for i in range(l):
        cur.execute("select first_name,m_name,last_name from contact_details where contact_id=(?)",(b[i][0],))
        s=cur.fetchall()
        
        lb.insert(i,s[0][0]+" "+s[0][1]+" "+s[0][2])

        
        
    lb.bind("<Double-Button-1>",click)
    e11.bind('<KeyRelease>',showvalue)
                    
    def close():
        root1.destroy()
    Button(root1,text='Close',command=close).grid(row=3,column=0)
    root1.mainloop()




#definition of edit:
def edit(e=1):
    root2=Tk()
    root2.geometry("550x700")
    root2.title("Search")
    Label(root2,text='Searching Phonebook',font='arial 20',background='green').grid(sticky=W+E+N+S)
    Label(root2,text='Enter Name',font='arial 15').grid(row=1,column=0,columnspan= 5, sticky=W)
    e21=Entry(root2)
    e21.grid(row=1,column=0)
    lb1=Listbox(root2,height='35',width='90',background='LIGHT GREY',fg='BLUE')
    lb1.grid()
    cur.execute("select contact_id,first_name,m_name,last_name from contact_details")
    ss=cur.fetchall()
    global aza
    aza=ss
    cur.execute("select contact_id curval from contact_details")
    bb= cur.fetchall()
    ll=len(bb)
        
    
    
    for i in range(ll):
        cur.execute("select first_name,m_name,last_name from contact_details where contact_id=? order by first_name,m_name,last_name",(bb[i][0],))
        s1=cur.fetchall()
        
        lb1.insert(i,s1[0][0]+" "+s1[0][1]+" "+s1[0][2])
    def showvalue1(e=1):
        #u=unicode(e11.get())
        #u=("%"+u+"%")
        
        lb1.delete(0,END)
        global aza
        cur.execute("select contact_id,first_name,m_name,last_name from contact_details where (first_name like (?) or m_name like (?) or last_name like (?))order by first_name,m_name,last_name",("%"+e21.get()+"%","%"+e21.get()+"%","%"+e21.get()+"%"))
        aza=cur.fetchall()
        
        for i in range(len(aza)):
            lb1.insert(i,aza[i][1]+" "+aza[i][2]+" "+aza[i][3])
        cur.execute("select contact_id curval from contact_details")
    b1= cur.fetchall()
    lz=len(b1)
        
    
    
    for i in range(lz):
        cur.execute("select first_name,m_name,last_name from contact_details where contact_id=? order by first_name,m_name,last_name",(b1[i][0],))
        s=cur.fetchall()
        
        lb1.insert(i,s[0][0]+" "+s[0][1]+" "+s[0][2])


    #for double button:
    def double(e=1):
        root3=Tk()
        root3.title('Phone Book')
        
        root3.configure(background='#A6B7C8')
        
        Label(root3,text='Phone Book',font='arial 20',foreground='blue').grid(row=1,column=2)
        Label(root3,text='First Name',font='italic 15').grid(row=2,column=1)
        e1a=Entry(root3)
        e1a.grid(row=2,column=2)
        Label(root3,text='Middle Name',font='italic 15').grid(row=3,column=1)
        e2a=Entry(root3)
        e2a.grid(row=3,column=2)
        Label(root3,text='Last Name',font='italic 15').grid(row=4,column=1)
        e3a=Entry(root3)
        e3a.grid(row=4,column=2)
        Label(root3,text='Company Name',font='italic 15').grid(row=5,column=1)
        e4a=Entry(root3)
        e4a.grid(row=5,column=2)
        Label(root3,text='Address',font='italic 15').grid(row=6,column=1)
        e5a=Entry(root3)
        e5a.grid(row=6,column=2)
        Label(root3,text='City',font='italic 15').grid(row=7,column=1)
        e6a=Entry(root3)
        e6a.grid(row=7,column=2)
        Label(root3,text='Pin Code',font='italic 15').grid(row=8,column=1)
        e7a=Entry(root3)
        e7a.grid(row=8,column=2)
        Label(root3,text='Website URL',font='italic 15').grid(row=9,column=1)
        e8a=Entry(root3)
        e8a.grid(row=9,column=2)
        Label(root3,text='Date Of Birth',font='italic 15').grid(row=10,column=1)
        e9a=Entry(root3)
        e9a.grid(row=10,column=2)
        Label(root3,text='Select phone type',font='italic 15',foreground='blue').grid(row=11,column=1)
        v1a=IntVar(root3)
        r1=Radiobutton(root3,text='office',variable=v1a,value=1).grid(row=11,column=2)
        r2=Radiobutton(root3,text='Home',variable=v1a,value=2).grid(row=11,column=3)
        r3=Radiobutton(root3,text='Mobile',variable=v1a,value=3).grid(row=11,column=4)
        Label(root3,text='Phone number',font='italic 15').grid(row=12,column=1)
        e10a=Entry(root3)
        e10a.grid(row=12,column=2)
        Label(root3,text='Select email type',font='italic 15',foreground='blue').grid(row=13,column=1)
        v2a=IntVar()
        r4=Radiobutton(root3,text='Office',variable=v2a,value=1).grid(row=13,column=2)
        r5=Radiobutton(root3,text='Personal',variable=v2a,value=2).grid(row=13,column=3)
        Label(root3,text='Email Id',font='italic 15').grid(row=14,column=1)
        e12a=Entry(root3)
        e12a.grid(row=14,column=2)
        global aza
        zz=lb1.curselection()
        
        fk=aza[zz[0]][0]
        
        
        cur.execute("select first_name,m_name,last_name,company,address,city,pin,website,birth_date from contact_details where contact_id =?",(fk,))
        dd=cur.fetchall()
        e1a.insert(0,dd[0][0])
        e2a.insert(0,dd[0][1])
        e3a.insert(0,dd[0][2])
        e4a.insert(0,dd[0][3])
        e5a.insert(0,dd[0][4])
        e6a.insert(0,dd[0][5])
        e7a.insert(0,dd[0][6])
        e8a.insert(0,dd[0][7])
        e9a.insert(0,dd[0][8])
        cur.execute("select contact_type,phone_number from number where contact_id=?",(fk,))
        z1=cur.fetchall()
        
        e10a.insert(0,z1[0][1])
        cur.execute("select emailid_type,email_id from email where contact_id=?",(fk,))
        z2=cur.fetchall()
        e12a.insert(0,z2[0][1])
        d1={1:'Office',2:'Home',3:'Mobile'}
        e1={1:'Office',2:'Personal'}
        uni=unicode (z1[0][0])
        res=d1.get(uni)
        
        if res==1:
            r1.select()
        elif res==2:
            r2.select()
        elif res==3:
            r3.select()
        def close():
            root3.destroy()
        Button(root3,text='Close',command=close).grid(row=15,column=0)
        def saveedit():
                t1=e1a.get()
                t2=e2a.get()
                t3=e3a.get()
                t4=e4a.get()
                t5=e5a.get()
                t6=e6a.get()
                t7=e7a.get()
                t8=e8a.get()
                t9=e9a.get()
                t10=e10a.get()
                t11=e12a.get()
                
                
                cur.execute("update contact_details set first_name=(?),m_name=(?),last_name=(?),company=(?),address=(?),city=(?),pin=(?),website=(?),birth_date=(?) where contact_id=(?)",(t1,t2,t3,t4,t5,t6,t7,t8,t9,fk))
                cur.execute("update number set contact_type=(?),phone_number=(?) where contact_id=(?)",(d1.get(v1a.get()),t10,fk))
                cur.execute("update email set emailid_type=(?),email_id=(?) where contact_id=(?)",(e1.get(v2a.get()),t11,fk))
                con.commit()
                showinfo('Update','Update Successfull')
                
                
            
        Button(root3,text='Save',command=saveedit).grid(row=15,column=1)    
    
    lb1.bind("<Double-Button-1>",double)
    e21.bind('<KeyRelease>',showvalue1)
                    
    def close():
        root2.destroy()
    Button(root2,text='Close',command=close).grid(row=3,column=0)
    root2.mainloop()












Label(root,text='Select email type',font='italic 15',foreground='blue').grid(row=13,column=1)
v2=IntVar()
Radiobutton(root,text='Office',variable=v2,value=1).grid(row=13,column=2)
Radiobutton(root,text='Personal',variable=v2,value=2).grid(row=13,column=3)
Label(root,text='Email Id',font='italic 15').grid(row=14,column=1)
e12=Entry(root)
e12.grid(row=14,column=2)


Button(root,text='Save',command=add).grid(row=15,column=1)
Button(root,text='Search',command=search).grid(row=15,column=2)
Button(root,text='Close',command=exit).grid(row=15,column=3)
Button(root,text='Edit',command=edit).grid(row=15,column=4)
root.mainloop()      

