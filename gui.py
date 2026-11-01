import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from function import *

window = Tk()
window.title("Employee Management System")
window.geometry("900x650")


notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True, padx=10, pady=10)


emp_tab  = Frame(notebook)

att_tab  = Frame(notebook)

dept_tab = Frame(notebook)

notebook.add(emp_tab,  text="👤 Employees")
notebook.add(att_tab,  text="📅 Attendance")
notebook.add(dept_tab, text="🏢 Departments")


Label(emp_tab, text="Employee ID").pack()
entry_id = Entry(emp_tab)
entry_id.pack()

Label(emp_tab, text="Name").pack()
entry_name = Entry(emp_tab)
entry_name.pack()
 
Label(emp_tab, text="Age").pack()
entry_age = Entry(emp_tab)
entry_age.pack()

Label(emp_tab, text="Gender").pack()
entry_gender = Entry(emp_tab)
entry_gender.pack()

Label(emp_tab, text="DOB").pack()
entry_dob = Entry(emp_tab)
entry_dob.pack()

Label(emp_tab, text="Phone").pack()
entry_phone = Entry(emp_tab)
entry_phone.pack()

Label(emp_tab, text="Salary").pack()
entry_salary = Entry(emp_tab)
entry_salary.pack()



def add_emp():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    dob = entry_dob.get()
    phone = entry_phone.get()
    salary = entry_salary.get()

    add_employee(name,age,gender,dob,phone,salary)
    print("Employee Added Successfully")

def view_emp():
    data = view_employee()

    for row in data:
        print(row)

def search_emp():
    emp_id = entry_id.get()

    result = search_employee(emp_id)

    if result:
        entry_name.delete(0,END)
        entry_age.delete(0,END)
        entry_gender.delete(0,END)
        entry_dob.delete(0,END)
        entry_phone.delete(0,END)
        entry_salary.delete(0,END)

        entry_name.insert(0,result[1])
        entry_age.insert(0,result[2])
        entry_gender.insert(0,result[3])
        entry_dob.insert(0,result[4])
        entry_phone.insert(0,result[5])
        entry_salary.insert(0,result[6])

    else:
        print("Employee not found")

def show_count():
    count = employee_count()
    print("Total Employees:",count)

def clear_fields():
    entry_id.delete(0,END)
    entry_name.delete(0,END)
    entry_age.delete(0,END)
    entry_gender.delete(0,END)
    entry_dob.delete(0,END)
    entry_phone.delete(0,END)
    entry_salary.delete(0,END)

button_frame = Frame(window)
button_frame.pack(pady=20)

Button(button_frame, text="Add Employee", command=add_emp,
       width=15, bg="lightgreen", font=("Arial",10,"bold")).grid(row=0,column=0,padx=10,pady=10)

Button(button_frame, text="View Employees", command=view_emp,
       width=15, bg="lightblue", font=("Arial",10,"bold")).grid(row=0,column=1,padx=10,pady=10)

Button(button_frame, text="Search Employee", command=search_emp,
       width=15, bg="orange", font=("Arial",10,"bold")).grid(row=1,column=0,padx=10,pady=10)

Button(button_frame, text="Employee Count", command=show_count,
       width=15, bg="pink", font=("Arial",10,"bold")).grid(row=1,column=1,padx=10,pady=10)

Button(button_frame, text="Clear Fields", command=clear_fields,
       width=15, bg="lightgray", font=("Arial",10,"bold")).grid(row=2,column=0,columnspan=2,pady=10)


Label(att_tab, text="Employee ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
att_emp_id = Entry(att_tab); att_emp_id.grid(row=0, column=1, padx=10, pady=5)

Label(att_tab, text="Date (YYYY-MM-DD)").grid(row=1, column=0, padx=10, pady=5, sticky="w")
att_date = Entry(att_tab); att_date.grid(row=1, column=1, padx=10, pady=5)

Label(att_tab, text="Status").grid(row=2, column=0, padx=10, pady=5, sticky="w")
att_status_var = StringVar(value="Present")
ttk.Combobox(att_tab, textvariable=att_status_var,
             values=["Present","Absent","Leave"],
             state="readonly", width=18).grid(row=2, column=1, padx=10, pady=5)

Label(att_tab, text="Filter by Emp ID (optional)").grid(row=3, column=0, padx=10, pady=5, sticky="w")
att_filter = Entry(att_tab); att_filter.grid(row=3, column=1, padx=10, pady=5)

def att_mark():
    if not att_emp_id.get() or not att_date.get():
        messagebox.showwarning("Input Error", "Employee ID and Date are required.")
        return
    mark_attendance(att_emp_id.get(), att_date.get(), att_status_var.get())
    messagebox.showinfo("Success", "Attendance marked!")
    att_refresh()

def att_refresh():
    for row in att_tree.get_children():
        att_tree.delete(row)
    fid = att_filter.get().strip() or None
    for row in view_attendance(fid):
        att_tree.insert("", "end", values=row)

def att_summary():
    if not att_emp_id.get():
        messagebox.showwarning("Input Error", "Enter Employee ID for summary.")
        return
    s = attendance_summary(att_emp_id.get())
    messagebox.showinfo("Summary",
        f"Present: {s['Present']}\nAbsent: {s['Absent']}\nLeave: {s['Leave']}")

def att_delete():
    sel = att_tree.selection()
    if not sel:
        messagebox.showwarning("Select", "Select a row to delete.")
        return
    att_id = att_tree.item(sel[0])["values"][0]
    if messagebox.askyesno("Confirm", "Delete this attendance record?"):
        delete_attendance(att_id)
        att_refresh()

att_btn_frame = Frame(att_tab)
att_btn_frame.grid(row=4, column=0, columnspan=2, pady=10)
Button(att_btn_frame, text="Mark Attendance", command=att_mark,
       bg="lightgreen", font=("Arial",10,"bold"), width=16).grid(row=0, column=0, padx=6)
Button(att_btn_frame, text="View / Refresh", command=att_refresh,
       bg="lightblue", font=("Arial",10,"bold"), width=16).grid(row=0, column=1, padx=6)
Button(att_btn_frame, text="Summary", command=att_summary,
       bg="orange", font=("Arial",10,"bold"), width=16).grid(row=0, column=2, padx=6)
Button(att_btn_frame, text="Delete Record", command=att_delete,
       bg="salmon", font=("Arial",10,"bold"), width=16).grid(row=0, column=3, padx=6)

att_tree = ttk.Treeview(att_tab, columns=("Att ID","Employee","Date","Status"),
                         show="headings", height=14)
for col in ("Att ID","Employee","Date","Status"):
    att_tree.heading(col, text=col); att_tree.column(col, width=150, anchor="center")
att_tree.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
att_refresh()



Label(dept_tab, text="Department ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
dept_id_entry = Entry(dept_tab); dept_id_entry.grid(row=0, column=1, padx=10, pady=5)

Label(dept_tab, text="Department Name").grid(row=1, column=0, padx=10, pady=5, sticky="w")
dept_name_entry = Entry(dept_tab); dept_name_entry.grid(row=1, column=1, padx=10, pady=5)

Label(dept_tab, text="Manager").grid(row=2, column=0, padx=10, pady=5, sticky="w")
dept_manager_entry = Entry(dept_tab); dept_manager_entry.grid(row=2, column=1, padx=10, pady=5)

Label(dept_tab, text="Location").grid(row=3, column=0, padx=10, pady=5, sticky="w")
dept_location_entry = Entry(dept_tab); dept_location_entry.grid(row=3, column=1, padx=10, pady=5)

def dept_clear():
    for w in [dept_id_entry, dept_name_entry, dept_manager_entry, dept_location_entry]:
        w.delete(0, END)

def dept_add():
    if not dept_name_entry.get():
        messagebox.showwarning("Input Error", "Department name is required.")
        return
    add_department(dept_name_entry.get(), dept_manager_entry.get(), dept_location_entry.get())
    messagebox.showinfo("Success", "Department added!")
    dept_clear(); dept_refresh()

def dept_refresh():
    for row in dept_tree.get_children():
        dept_tree.delete(row)
    for row in view_departments():
        dept_tree.insert("", "end", values=row)

def dept_update():
    if not dept_id_entry.get():
        messagebox.showwarning("Input Error", "Enter Department ID to update.")
        return
    update_department(dept_id_entry.get(), dept_name_entry.get(),
                      dept_manager_entry.get(), dept_location_entry.get())
    messagebox.showinfo("Success", "Department updated!")
    dept_clear(); dept_refresh()

def dept_delete():
    if not dept_id_entry.get():
        messagebox.showwarning("Input Error", "Enter Department ID to delete.")
        return
    if messagebox.askyesno("Confirm", "Delete this department?"):
        delete_department(dept_id_entry.get())
        messagebox.showinfo("Deleted", "Department deleted.")
        dept_clear(); dept_refresh()

def dept_view_employees():
    if not dept_id_entry.get():
        messagebox.showwarning("Input Error", "Enter Department ID.")
        return
    rows = employees_in_department(dept_id_entry.get())
    if not rows:
        messagebox.showinfo("Info", "No employees in this department.")
        return
    popup = Toplevel(window)
    popup.title("Employees in Department")
    popup.geometry("600x300")
    pt = ttk.Treeview(popup, columns=("ID","Name","Age","Gender","Phone","Salary"),
                      show="headings", height=10)
    for col in ("ID","Name","Age","Gender","Phone","Salary"):
        pt.heading(col, text=col); pt.column(col, width=90, anchor="center")
    pt.pack(fill="both", expand=True, padx=10, pady=10)
    for row in rows:
        pt.insert("", "end", values=row)

def on_dept_select(event):
    sel = dept_tree.selection()
    if sel:
        vals = dept_tree.item(sel[0])["values"]
        dept_clear()
        dept_id_entry.insert(0, vals[0])
        dept_name_entry.insert(0, vals[1])
        dept_manager_entry.insert(0, vals[2])
        dept_location_entry.insert(0, vals[3])

dept_btn_frame = Frame(dept_tab)
dept_btn_frame.grid(row=4, column=0, columnspan=2, pady=10)
Button(dept_btn_frame, text="Add Dept",       command=dept_add,            bg="lightgreen", font=("Arial",10,"bold"), width=14).grid(row=0,column=0,padx=5)
Button(dept_btn_frame, text="Update Dept",    command=dept_update,         bg="orange",     font=("Arial",10,"bold"), width=14).grid(row=0,column=1,padx=5)
Button(dept_btn_frame, text="Delete Dept",    command=dept_delete,         bg="salmon",     font=("Arial",10,"bold"), width=14).grid(row=0,column=2,padx=5)
Button(dept_btn_frame, text="Refresh",        command=dept_refresh,        bg="lightblue",  font=("Arial",10,"bold"), width=14).grid(row=0,column=3,padx=5)
Button(dept_btn_frame, text="View Employees", command=dept_view_employees, bg="pink",       font=("Arial",10,"bold"), width=14).grid(row=0,column=4,padx=5)

dept_tree = ttk.Treeview(dept_tab, columns=("Dept ID","Dept Name","Manager","Location"),
                          show="headings", height=14)
for col in ("Dept ID","Dept Name","Manager","Location"):
    dept_tree.heading(col, text=col); dept_tree.column(col, width=160, anchor="center")
dept_tree.grid(row=5, column=0, columnspan=5, padx=10, pady=10)
dept_tree.bind("<<TreeviewSelect>>", on_dept_select)
dept_refresh()




window.mainloop()