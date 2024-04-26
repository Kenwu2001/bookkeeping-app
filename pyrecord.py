import sys
import os

class Record:
    """Represent a record."""
    def __init__(self, date, category, description, amount):
        self._date = date
        self._category = category
        self._description = description
        self._amount = amount
    @property
    def date(self): return self._date
    @property
    def category(self): return self._category
    @property
    def description(self): return self._description
    @property
    def amount(self): return int(self._amount)

class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        # 1. Read from 'records.txt' or prompt for initial amount of money.
        # 2. Initialize the attributes (self._records and self._initial_money)
        #    from the file or user input.
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'],\
                        'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            dir_name = dir_path + "/records.txt"
            fh = open(dir_name,"r+")
        except FileNotFoundError:
            while True:
                try:
                    self._initial_money = int(input('How much money do you have?'))    
                except ValueError:                                              # Error 1
                    sys.stderr.write(f'invalid input!!!\n')
                else:
                    self._records = []
                    #print('now you have: %d' % self._initial_money)
                    break
        else:
            print('welcome back!!!') 
            try:
                self._records = []
                self._initial_money = int(fh.readline())
            except ValueError:   
                if fh.readline() == '' or fh.readline == '\n':          # nothing in the file
                    sys.stderr.write('nothin in the file!!!\n')             # Error 8
                    self._initial_money = int(input('How much money do you have?'))                            
                else:
                    sys.stderr.write('first line is not an integer!!!\n')       # Error 9
                    self._initial_money = int(input('How much money do you have?'))     
            finally:
                for line in fh.readlines():
                    current_record = line.split()
                    try:
                        (date,category,description,money) = (current_record[0],current_record[1],current_record[2],int(current_record[3]))
                    except IndexError:
                        sys.stderr.write('record error,it should be the form : a b 30\n')   # Error 10

                    except ValueError:
                        sys.stderr.write('record error, you should type (string string int)\n')   # Error 11
                    else:
                        self._records.append((date,category,description,money))    # using list of tuple to get info in txt
 
    def add(self, record, categories):
        """add a record into the list"""
        #split_record = record.split()
        if categories.is_category_valid(self._categories,record.category) != True:
            sys.stderr.write('the category is not in the existing category\n')
        else:
            current_record = (record.date, record.category, record.description, record.amount)
            self._records.append(current_record)
            self._initial_money = self._initial_money + record.amount
 
    def view(self):
        """view the records"""
        # 1. Print all the records and report the balance.
        print('here is your records:')
        print('Date        Category        Description    Amount  ')
        for i in self._records:
            print(f'{i[0]:<12}{i[1]:<15} {i[2]:<15}{i[3]}')
        print('==========> now you have: %d dollars' % self._initial_money)
 
    def delete(self, record):
        """delete a record"""
        if (record.date, record.category, record.description, record.amount) in self._records:
            self._records.remove((record.date, record.category, record.description, record.amount))
            self._initial_money = self._initial_money - record.amount
        else:
            sys.stderr.write('the record is not in the list\n') 
 
    def find(self, L): # L is a list
        """find everything under the category"""
        # 1. Define the formal parameter to accept a non-nested list
        #    (returned from find_subcategories)
        # 2. Print the records whose category is in the list passed in
        #    and report the total amount of money of the listed records.
        totalAmount = 0
        try:
            filtered = list(filter(lambda x: x[1] in L, self._records))
            print(f"Here's your expense and income records under category \"{L[0]}\":" )
            print('Date        Category        Description     Amount')
            print("= = = = = = = = = = = = = = = = = =")
            for ele in filtered:
                #if ele[1] in L:
                print('{:<12}{:<15} {:<15} {}'.format(ele[0], ele[1], ele[2],ele[3]))
                totalAmount += ele[3]
            print("= = = = = = = = = = = = = = = =")
            print('The total amount above is %d' % totalAmount)
        except:
            print('The specified category is not in the category list.')
            print('You can check the category list by command "view categories".')
            '''pop = tkinter.Toplevel(root)
            pop.geometry("250x30")
            pop_label = tkinter.Label(pop,text="error!!!!")
            pop_label.pack(pady=10)'''
 
    def save(self):
        records_string = []
        for i in self._records:
            record = i[0]+' '+i[1] +' '+str(i[2])+' '+str(i[3])+'\n' 
            records_string.append(record)               # using list of string to save
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_name = dir_path + "/records.txt"
        #fh = open(dir_name,"r+")
        with open(dir_name, 'w') as fh:
            fh.write('%s\n' % str(self._initial_money))
            fh.writelines(records_string)
        # 1. Write the initial money and all the records to 'records.txt'.