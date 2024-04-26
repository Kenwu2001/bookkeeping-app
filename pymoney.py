#from ast import Break
#from os import popen
from http.client import MOVED_PERMANENTLY
from pyrecord import Record
from pyrecord import Records
from pycategory import Categories
from datetime import date
import sys
all_category = ['expense', ['food', ['meal', 'snack', 'drink'],\
                        'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
categories = Categories()
records = Records()

import tkinter

in_category = False

def get_value():
    try:
        record_date=entering.get().split()[0]
        date.fromisoformat(record_date)
    except: # pop an error
        pop = tkinter.Toplevel(root)
        pop.geometry("250x30")
        pop_label = tkinter.Label(pop,text="error!!!!")
        pop_label.pack(pady=10)
    else:
        try:
            type(int(entering.get().split()[3])) == int
        except:
            pop = tkinter.Toplevel(root)
            pop.geometry("250x30")
            pop_label = tkinter.Label(pop,text="error!!!!")
            pop_label.pack(pady=10)
        else:
            records.add(Record(entering.get().split()[0],entering.get().split()[1],entering.get().split()[2],
                                int(entering.get().split()[3])), categories)
            box.insert("end",entering.get())
            money.set(records._initial_money)

def delete_value():
    global in_category
    if in_category == True:
        pop = tkinter.Toplevel(root)
        pop.geometry("250x30")
        pop_label = tkinter.Label(pop,text="error!!!!")
        pop_label.pack(pady=10)
        return
    for item in box.curselection():
        delete_record = box.get(item)
        box.delete(item)
        records.delete(Record(delete_record[0],delete_record[1],delete_record[2],int(delete_record[3])))
    money.set(records._initial_money)

def view_category():
    category = entering.get().split()[0]
    if categories.is_category_valid(all_category,category) == False:
        pop = tkinter.Toplevel(root)
        pop.geometry("250x30")
        pop_label = tkinter.Label(pop,text="error!!!!")
        pop_label.pack(pady=10)
    else:
        target_categories = categories.find_subcategories(category)
        filtered = list(filter(lambda x: x[1] in target_categories ,records._records))
        string_to_print = []
        for ele in filtered:
                record = ''
                record = ele[0] + ' '+ele[1]+' '+ele[2]+' '+str(ele[3])
                string_to_print.append(record)
        box.delete(0,"end")
        box.insert("end",*string_to_print)
        global in_category
        in_category = True

def quit_and_save():
    records.save()
    root.destroy()

def go_home():
    box.delete(0,"end")
    box.insert("end",*records._records)
    global in_category
    in_category = False


root = tkinter.Tk()
money = tkinter.StringVar()
f = tkinter.Frame(root, borderwidth=10)
box = tkinter.Listbox(f,width=50)
entering = tkinter.Entry(f,width=40)
#money_label = tkinter.Label(root, textvariable=money)
button_add = tkinter.Button(f, text='add', command=get_value)
button_delete = tkinter.Button(f, text='delete',command=delete_value)
button_category = tkinter.Button(f, text='category', command=view_category)
button_quit = tkinter.Button(f, text='quit', command=quit_and_save)
button_home = tkinter.Button(f, text='home', command=go_home)
box.insert("end",*records._records)

money.set(records._initial_money)

f.grid(row=0, column=0)
box.grid(row=1,column=0,columnspan=10,ipadx=5, pady=5)
entering.grid(row=2,column=0,columnspan=10,ipadx=5, pady=5)
tkinter.Label(f,textvariable=money).grid(row=3,column=0,columnspan=10,ipadx=5, pady=5)
#money_label.grid(row=3, column=1,ipadx=5)

button_add.grid(row=4, column=0,ipadx=5)
button_delete.grid(row=4, column=1,ipadx=5)
button_category.grid(row=4, column=2,ipadx=5)
button_quit.grid(row=4, column=3,ipadx=5)
button_home.grid(row=4, column=4,ipadx=5)

f.mainloop()


#help(categories.find_subcategories)

'''while True:
    command = input('\nWhat do you want to do (add / view / delete / view categories / find / exit)? ')
    if command == 'add':
        record = input('Add an expense or income record with ...:\n') # string type
        try:
            record_date = record.split()[0]
            date.fromisoformat(record_date)
        except:
            sys.stderr.write('date form should be xxxx-xx-xx or the date is not valid\n')
            continue
        try:
            type(int(record.split()[3])) == int
        except:
            sys.stderr.write('fourth description should be a number\n')
        else:
            records.add(Record(record.split()[0],record.split()[1],record.split()[2],int(record.split()[3])), categories)
            
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? ")
        try:
            record_date = delete_record.split()[0]
            date.fromisoformat(record_date)
        except:
            sys.stderr.write('date form should be xxxx-xx-xx or the date is not valid\n')
            continue
        try:
            type(int(delete_record.split()[3])) == int
        except:
            sys.stderr.write('fourth description should be a number\n')
        else:
            records.delete(Record(delete_record.split()[0],delete_record.split()[1],delete_record.split()[2],int(delete_record.split()[3])))
            
    elif command == 'view categories': 
        categories.view(categories._categories)
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        #print(target_categories)
        records.find(target_categories)
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')'''