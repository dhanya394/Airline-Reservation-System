#python project to implement Airline Reservation System
from Tkinter import *
from tkMessageBox import *
import sqlite3

#creating root window
window = Tk()
window.title("Airline Reservation System")
window.configure(background="black")

#creating database
con=sqlite3.Connection('Airline_db')
cur=con.cursor()
cur.execute("create table if not exists airline(name varchar(20) primary key not null, age varchar(20), class varchar(20), gender varchar(20), source varchar(20), destination varchar(20), date varchar(20))")
print("Table created successfully")

#function for click button
def click():
    #function for submit button

    def submit():
        showinfo('Message', 'Flight booked successfully')
    #function for view flight details button
    def view():
        #retrieving user values
        name1 = name.get()
        age1 = age.get()
        class1 = variable1.get()
        gender1 = gender.get()
        source1 = variable2.get()
        destination1 = variable3.get()
        date1 = date.get()
        if gender1==0:
            g = 'Male'
        else:
            g= 'Female'
        #inserting values into database
        l = (name1, age1, class1, g, source1, destination1, date1)
        cur.execute("INSERT INTO AIRLINE VALUES (?,?,?,?,?,?,?)",l)
        con.commit()
        #window for viewing flight details
        window2 = Toplevel(window)
        window2.configure(background="black")
        Label(window2, text="View Flight Details", bg='blue', fg='white', font='none 18 bold').pack()
        fr3=Frame(window2) #new frame
        fr3.config(bg='black')
        fr3.pack(side=LEFT, expand=1)
        #widgets for text field labels
        Label(fr3, text="Name : ", bg='black', fg='white', font='none 18 bold').grid(row=0, column=0, sticky=W)
        Label(fr3, text=name1, bg='black', fg='white', font='none 18 bold').grid(row=0, column=1, sticky=E)
        Label(fr3, text="Age : ", bg='black', fg='white', font='none 18 bold').grid(row=1, column=0, sticky=W)
        Label(fr3, text=age1, bg='black', fg='white', font='none 18 bold').grid(row=1, column=1, sticky=E)
        Label(fr3, text="Class : ", bg='black', fg='white', font='none 18 bold').grid(row=2, column=0, sticky=W)
        Label(fr3, text=class1, bg='black', fg='white', font='none 18 bold').grid(row=2, column=1, sticky=E)
        Label(fr3, text="Gender : ", bg='black', fg='white', font='none 18 bold').grid(row=3, column=0, sticky=W)
        if gender1==0:
            Label(fr3, text='Male', bg='black', fg='white', font='none 18 bold').grid(row=3, column=1, sticky=E)
        else:
            Label(fr3, text='Female', bg='black', fg='white', font='none 18 bold').grid(row=3, column=1, sticky=E)
        Label(fr3, text="Source : ", bg='black', fg='white', font='none 18 bold').grid(row=4, column=0, sticky=W)
        Label(fr3, text=source1, bg='black', fg='white', font='none 18 bold').grid(row=4, column=1, sticky=E)
        Label(fr3, text="Destination : ", bg='black', fg='white', font='none 18 bold').grid(row=5, column=0, sticky=W)
        Label(fr3, text=destination1, bg='black', fg='white', font='none 18 bold').grid(row=5, column=1, sticky=E)
        Label(fr3, text="Date of Travel : ", bg='black', fg='white', font='none 18 bold').grid(row=6, column=0, sticky=W)
        Label(fr3, text=date1, bg='black', fg='white', font='none 18 bold').grid(row=6, column=1, sticky=E)
        Label(fr3, text="Price : ", bg='black', fg='white', font='none 18 bold').grid(row=7, column=0, sticky=W)
        Label(fr3, text='3500', bg='black', fg='white', font='none 18 bold').grid(row=7, column=1, sticky=E)
        window2.mainloop()
    #book flight window
    window1 = Toplevel(window)
    window1.title("Book Flight")
    window1.configure(background="black")
    #adding scrollbar
    scrollbar = Scrollbar(window1)
    scrollbar.pack(side=RIGHT, fill=Y)
    Label(window1, text="Book Flight", bg='blue', fg='white', font='none 18 bold').pack()
    fr2 = Frame(window1)
    fr2.config(bg='black')
    fr2.pack(side=LEFT, expand=1)
    Label(fr2, text="Name", bg='black', fg='white', font='none 12 bold').grid(row=0,column=0,padx=10,pady=10,sticky=W)
    name = Entry(fr2, width=20, bg='white')
    name.grid(row=0, column=1, sticky=E)
    Label(fr2, text="Age", bg='black', fg='white', font='none 12 bold').grid(row=1, column=0, padx=10, pady=10,sticky=W)
    age = Entry(fr2, width=20, bg='white')
    age.grid(row=1, column=1, sticky=E)
    Label(fr2, text="Class", bg='black', fg='white', font='none 12 bold').grid(row=2, column=0, padx=10, pady=10,sticky=W)
    variable1 = StringVar(fr2)
    variable1.set("Class")
    Class = OptionMenu(fr2, variable1, "Economy", "Business", "Executive")
    Class.grid(row=2,column=1,sticky=E)
    Label(fr2, text="Gender", bg='black', fg='white', font='none 12 bold').grid(row=3, column=0, padx=10, pady=10,sticky=W)
    gender = IntVar()
    Radiobutton(fr2, text="Male", variable=gender, value=0, fg="black").grid(row=3, column=1,sticky=E)
    Radiobutton(fr2, text="Female", variable=gender, value=1, fg="black").grid(row=3, column=2,sticky=E)
    Label(fr2, text="Source", bg='black', fg='white', font='none 12 bold').grid(row=4, column=0, padx=10, pady=10,sticky=W)
    variable2 = StringVar(fr2)
    variable2.set("Source")
    #creating optionmenu
    Source = OptionMenu(fr2, variable2, "Chennai", "Delhi", "Kolkata", "Mumbai")
    Source.grid(row=4, column=1, sticky=E)
    #source = Entry(fr2, width=20, bg='white')
    #source.grid(row=4, column=1, sticky=E)
    Label(fr2, text="Destination", bg='black', fg='white', font='none 12 bold').grid(row=5, column=0, padx=10, pady=10,sticky=W)
    variable3 = StringVar(fr2)
    variable3.set("Destination")
    destination = OptionMenu(fr2, variable3, "Chennai", "Delhi", "Kolkata", "Mumbai")
    destination.grid(row=5, column=1, sticky=E)
    #destination = Entry(fr2, width=20, bg='white')
    #destination.grid(row=5, column=1, sticky=E)
    Label(fr2, text="Date of travel", bg='black', fg='white', font='none 12 bold').grid(row=6, column=0, padx=10, pady=10,sticky=W)
    date = Entry(fr2, width=15, font='none 12 bold', bg='black', fg="white")
    date.grid(row=6, column=1)
    date.insert(0, "DD/MM/YYYY")
    Button(fr2, text='Submit', width=20, command=submit).grid(row=7, column=1, padx=10, pady=10)
    Button(fr2, text='View Flight Details', width=20, command=view).grid(row=8, column=1, padx=10, pady=10)
    window1.mainloop()

#initial widgets for the window
#we use pack and grid geometry managers
Label (window, text="Airline Reservation System", bg='black', fg='white', font='none 20 bold').pack()
fr1=Frame() #creating a new frame
fr1.config(bg='black')
fr1.pack(side=LEFT,expand=1)
#text label
Label (fr1, text="Welcome to Airline Reservation System", bg='black', fg='blue', font='none 12 bold').grid(row=0,column=1,padx=10,pady=10)
a=PhotoImage(file="airline.gif") #loads image
Label(fr1,image=a).grid(row=1,column=1,padx=10,pady=10)
#fr1.pack(expand=1)
Label (fr1, text="Made by - Dhanya Sasikumar", bg='black', fg='white', font='none 12 bold').grid(row=2,column=1,padx=10,pady=10)
#button opens a new window
Button (fr1, text='Click to proceed', width=20, command=click).grid(row=3,column=1,padx=10,pady=10)

window.mainloop() #executing the window

#displaying database values
print("The table values are : ")
cursor = cur.execute("select * from airline")
for row in cursor:
    print(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]))

