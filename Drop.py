# Importing necessary libraries for the GUI
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import _sqlite3

# Connect to the SQLite database named 'SQL_Drop.db'
con = _sqlite3.connect('SQL_Drop.db')
# Create a cursor object to execute SQL commands
cur = con.cursor()


# Creating a window with a title, size, and background color.
window = Tk()
window.title("ลงทะเบียนเพิกถอนรายวิชา")
window.geometry("650x450")
window.option_add('*font', 'tahoma 10')
window.resizable(0, 0)
window.config(bg='#15F043')
frame = Frame(window)
frame.config(bg='#9BFEB0')
frame.pack()

# Creating labels for the GUI.
idlable = Label(frame, text="บัญชีนนทรี", width=12, anchor=W)
idlable.grid(column=0, row=0, padx=5, pady=10)
pwlable = Label(frame, text="รหัสผ่าน", width=12, anchor=W)
pwlable.grid(column=0, row=1, padx=5, pady=5)
cpwlabel = Label(frame, text="ยืนยันรหัสผ่าน", width=12, anchor=W)
cpwlabel.grid(column=0, row=2, padx=5, pady=5)
adlable = Label(frame, text="อาจารย์ที่ปรึกษา", width=12, anchor=W)
adlable.grid(column=0, row=6, padx=20, pady=20)

# A variable that is used to store the value of the entry.
envar1 = StringVar()
entry1 = Entry(frame, textvariable=envar1, width=20)
entry1.grid(column=1, row=0, padx=5, pady=5,)
envar2 = StringVar()
entry2 = Entry(frame, textvariable=envar2, show="*", width=20)
entry2.grid(column=1, row=1, padx=5, pady=5)
envar3 = StringVar()
entry3 = Entry(frame, textvariable=envar3, show="*", width=20)
entry3.grid(column=1, row=2, padx=5, pady=5)
envar4 = StringVar()
entry4 = Entry(frame, textvariable=envar4, width=20)
entry4.grid(column=1, row=6, padx=5, pady=5, columnspan=2)


def getvalue():
    # Declare the variable as global
    global rtype
    # Create a dictionary to map the values of the radio button to their corresponding gender
    varlist = {1: "ชาย", 2: "หญิง"}
    # Assign the value of the selected radio button to the 'rtype' variable, using the varlist dictionary
    rtype = varlist[var.get()]


# Creating a radio button.
var = IntVar()
r1 = Radiobutton(frame, text="ชาย", width=10, variable=var, value=1, anchor=W, command=getvalue)
r1.grid(column=0, row=3, padx=5, pady=5)
r1 = Radiobutton(frame, text="หญิง", width=10, variable=var, value=2, anchor=W, command=getvalue)
r1.grid(column=1, row=3, padx=5, pady=5)

# Creating a label and a listbox.
lable4 = Label(frame, text="===== เลือกวิชาที่ดรอป =====", width=39)
lable4.grid(column=0, row=4, columnspan=2, padx=5)
lable4.config(font="tahoma 10 bold")
listbox1 = Listbox(frame, height=10, width=45)
listbox1.grid(column=0, row=5, columnspan=2)
scrolly1 = Scrollbar(frame, orient=VERTICAL, command=listbox1.yview)
scrolly1.grid(column=2, row=5, sticky=NW+SW)
listbox1.config(yscrollcommand=scrolly1.set)


def listbox1_select(event):
    # Get the widget associated with the event
    w = event.widget
    # Get the index of the selected item in the listbox
    data = int(w.curselection()[0])
    # Declare the variable as global
    global freeitem
    # Get the value of the selected item in the listbox
    freeitem = w.get(data)


# Bind the 'listbox1_select' function to the '<<ListboxSelect>>' event
listbox1.bind('<<ListboxSelect>>', listbox1_select)

# Create a list of course names
courselist = ["Engineering Mathematics I",
              "General Physics I",
              "Laboratory in Physics I",
              "Knowledge of the Land",
              "Green Technology",
              "Programming Fundamentals I",
              "Engineering Drawing"]

# Loop through the items in the 'courselist' and insert them into the 'listbox1'
for item in courselist:
    listbox1.insert(END, item)

# Creating a label and a combobox.
typelable = Label(frame, text="ชั้นปีการศึกษา", width=15, anchor=W)
typelable.grid(column=3, row=0, padx=5, pady=5)
ycombo = Combobox(frame, width=10)
ycombo.grid(column=4, row=0, padx=5)
yearlist = ["1", "2", "3", "4", "5", "6", "7", "8"]
ycombo['values'] = yearlist
ycombo.current(0)

# It sets the global variable facultytype to the value of the key in the facultylist dictionary that corresponds to the value of the variable var1
def getcvalue():
    global facultytype
    facultylist = {1: "วิศวกรรมศาสตร์", 
                   2: "วิทยาการจัดการ",
                   3: "วิทยาศาสตร์", 
                   4: "เศรษศาสตร์"}
    facultytype = facultylist[var1.get()]

# Creating a label and a combobox.
lable2 = Label(frame, text="======== คณะ ========", width=30)
lable2.grid(column=3, row=1, columnspan=2, padx=5)
lable2.config(font="tahoma 10 bold")
var1 = IntVar()
c1 = Radiobutton(frame, text="วิศวกรรมศาสตร์", width=12, variable=var1, value=1, anchor=W, command=getcvalue)
c1.grid(column=3, row=2, padx=5, pady=5)
var2 = IntVar()
c2 = Radiobutton(frame, text="วิทยาการจัดการ", width=12, variable=var1, value=2, anchor=W, command=getcvalue)
c2.grid(column=4, row=2, padx=5, pady=5)
var3 = IntVar()
c3 = Radiobutton(frame, text="วิทยาศาสตร์", width=12, variable=var1, value=3, anchor=W, command=getcvalue)
c3.grid(column=3, row=3, padx=5, pady=5)
var4 = IntVar()
c4 = Radiobutton(frame, text="เศรษศาสตร์", width=12, variable=var1, value=4, anchor=W, command=getcvalue)
c4.grid(column=4, row=3, padx=5, pady=5)

# Creating a label and a textbox.
lable3 = Label(frame, text="===== ตรวจสอบข้อมูล =====", width=30)
lable3.grid(column=3, row=4, columnspan=2, padx=5)
lable3.config(font="tahoma 10 bold")
displaymsg = Text(frame, bg="white", height=10, width=35)
displaymsg.grid(column=3, row=5, columnspan=2, padx=5, sticky=E)
scrolly2 = Scrollbar(frame, orient=VERTICAL, command=displaymsg.yview)
scrolly2.grid(column=5, row=5, sticky=NW+SW)
displaymsg.config(yscrollcommand=scrolly2.set)


def get_data():
    # Declare the variable as global
    global entries
    # Create an empty list to store the data from the entries
    data2 = []
    # Loop through the list of entries and append their values to the 'data2' list
    for w in entries:
        data2.append(w)
    # Return the 'data2' list
    return data2



def add_data():
    # Create a SQL statement to insert data into the table
    sql = 'INSERT INTO รายชื่อนิสิตทะเบียนเพิกถอนรายวิชา VALUES (?, ?, ?, ?, ?, ?, ?)'
    
    # Get the data from the input fields
    data = get_data()
    # Execute the SQL statement with the data
    r = cur.execute(sql, data)
    # Check if the data was successfully inserted
    if r.rowcount == 1:
        # If successful, commit the changes and show a message box indicating success
        con.commit()
        messagebox.showinfo('Success', 'ข้อมูลบันทึกแล้ว')
        clear_data()
    else:
        # If not successful, show a message box indicating an error
        messagebox.showerror('Error', 'เกิดข้อผิดพลาด')



# It takes the data from the GUI and puts it into a list called entries. Then it calls the add_data function.
def checkdata():
    global entries
    displaymsg.delete("1.0", END)
    msg = "1. ชื่อบัญชีนนทรี: " + entry1.get() + "\n"
    msg += "2. รหัสผ่าน: " + entry2.get() + "\n"
    msg += "3. เพศ: " + rtype + "\n"
    msg += "4. ชั้นปีการศึกษา: " + ycombo.get() + "\n"
    msg += "3. คณะ: " + facultytype + "\n"
    msg += "4. วิชาที่เพิกถอน:\n    - " + freeitem + "\n"
    msg += "5. อาจารย์ที่ปรึกษา: " + entry4.get() + "\n"
    displaymsg.insert(INSERT, msg)
    entries = [str(entry1.get()), 
               str(entry2.get()), 
               str(rtype),
               str(ycombo.get()), 
               str(facultytype), 
               str(freeitem),
               str(entry4.get())]
    add_data()


# It clears the data from the entry boxes and the drop down menu.
def clear_data():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    ycombo.delete(0, END)


# If the two entries are not equal, show an error message. If they are equal, call the checkdata() function.
def save_data():
    if envar2.get() != envar3.get():
        messagebox.showerror("Error", "รหัสผ่านกับยืนยันรหัสผ่านไม่ตรงกัน")
    elif envar2.get() == envar3.get():
        checkdata()
        button1.focus_set()


# It creates a button with the text "บันทึก" and places it in the grid at column 3, row 6. 
# The button is 10 units wide and 3 units high. The command attribute is set to the save_data function.
button1 = Button(frame, text="บันทึก", width=10, height=3, compound="left", command=save_data)
button1.grid(column=3, row=6, padx=20, pady=20)

# A method that is used to run the main loop of the GUI.
window.mainloop()
