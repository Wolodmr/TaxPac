''' Package TaxPac provides users primary searching their tax
payments in USA. It includes:
a) Script tax_gui.py, provides GUI,
b) Module tax_calc.py supplies the script with calculation
   methods,
c) DataBase usa_taxation.py,
d) states_taxation_data.py is a reserve database with data for 
   few states and sities, as well as for federal taxation,
e) __init__.py - file with main data about TaxPac

TaxPac can work in two modes. These two modes allow users:
1) 
To estimate their tax payments in USA, upon
their location - 
            state and city - and gross salary. 
Estimation of tax payments is provided basing on calculation of 
            federal, state, cities taxes and FICA. 
The calculations consider 
            standard deductions and tax brackets.

2)
To add necessary taxation data for states and cities, which are
still absent in a TacPac database. This functionality lets user 
easily correct data, which are present in the database: to do that, 
user just 


'''
from tkinter import *
import tax_calc
import pickle
import math
class Calculator:
    def __init__(self):
        pass

    def tax_pack_mode(self):
        root = Tk()
        root.title('US Tax Pack')
        root.geometry('300x80')

        app = Frame(root)
        app.grid()

        self.mode = StringVar()

        Radiobutton(app,
                    text='Tax Calculator',
                    variable=self.mode,
                    value='Tax Calculator',
                    command=self.show_tax_calculator
                    ).grid(row=2, column=0, sticky=W)

        Radiobutton(app,
                    text='Adding State/City to the Taxational DataBase',
                    variable=self.mode,
                    value='Add Taxational Info',
                    command=self.show_add_tax_data
                    ).grid(row=3, column=0, sticky=W)

        root.mainloop()

    def show_tax_calculator(self):
        self.root = Toplevel()
        self.root.title('Tax Calculator')
        self.root.geometry('400x400')

        Label(self.root).grid(row=0)

        # Input fields
        self.salary_label = Label(self.root, text="Enter your gross salary: ")
        self.salary_label.grid(row=1, column=0, sticky=W)
        self.salary_entry = Entry(self.root)
        self.salary_entry.grid(row=1, column=1)

        self.state_label = Label(self.root, text="Enter your state: ")
        self.state_label.grid(row=2, column=0, sticky=W)
        self.state_entry = Entry(self.root)
        self.state_entry.grid(row=2, column=1)

        self.city_label = Label(self.root, text="Enter your city: ")
        self.city_label.grid(row=3, column=0, sticky=W)
        self.city_entry = Entry(self.root)
        self.city_entry.grid(row=3, column=1)

        Label(self.root).grid(row=4)

        self.calculate_button = Button(self.root, text="Calculate Tax", command=self.calculate_tax)
        self.calculate_button.grid(row=5, column=0, columnspan=2)

        Label(self.root).grid(row=6)

        # Text field for output
        self.output_text = Text(self.root, height=10, width=40)
        self.output_text.grid(row=7, column=0, columnspan=2)

    def show_add_tax_data(self):
        self.root = Toplevel()
        self.root.title('Add Taxational Information')
        self.root.geometry('405x400')

        self.subject_label = Label(self.root, text="Select the taxational type of the subject to add: ")
        self.subject_label.grid(row=0, column=0, sticky=W)

        # Radio buttons for specifying the subject type
        self.subject_type = StringVar()
        Radiobutton(self.root, text="State", variable=self.subject_type, value="State").grid(row=0, column=1, sticky=W)
        Radiobutton(self.root, text="City", variable=self.subject_type, value="City").grid(row=0, column=1, sticky=E)

        # Input fields for adding taxational information
        self.subject_label = Label(self.root, text="Enter the name of the subject (state or city): ")
        self.subject_label.grid(row=2, column=0, sticky=W)
        self.subject_entry = Entry(self.root)
        self.subject_entry.grid(row=2, column=1)

        self.deduction_label = Label(self.root, text="Enter the subject standard tax deduction: ")
        self.deduction_label.grid(row=3, column=0, sticky=W)
        self.deduction_entry = Entry(self.root)
        self.deduction_entry.grid(row=3, column=1)

        self.brackets_label = Label(self.root, text="Enter the subject tax brackets (comma-separated): ")                              
        self.brackets_label.grid(row=4, column=0, sticky=W)
        self.brackets_entry = Entry(self.root)
        self.brackets_entry.grid(row=4, column=1)
        self.brackets_label = Label(self.root, text="If income top level is not indicated, type 'inf'.")
        self.brackets_label.grid(row=5, column=0, sticky=W)
        
        Label(self.root).grid(row=6)

        self.add_info_button = Button(self.root, text="Add Taxational Data", command=self.add_tax_data)
        self.add_info_button.grid(row=7, column=0, columnspan=2)

        Label(self.root).grid(row=8)

        # Text field for output
        self.output_text = Text(self.root, height=10, width=40)
        self.output_text.grid(row=9, column=0, columnspan=2)


    def calculate_tax(self):
        salary = float(self.salary_entry.get())
        state = self.state_entry.get()
        city = self.city_entry.get()
        output = tax_calc.TaxCalculator().main(salary, state, city)
        # Clear previous output
        self.output_text.delete(1.0, END)
        # Insert new output
        self.output_text.insert(END, output)

    def add_tax_data(self):
        tax_list = tax_calc.TaxCalculator().usa_taxation_stats()
        #print(tax_list)
        subject_type = self.subject_type.get()
        subject = self.subject_entry.get()
        deduction = self.deduction_entry.get()
        brackets_str = self.brackets_entry.get()

        # Defining tax subject to add data: State or City. Subject data will be passed 
        # to a proper dictionary of dictionaries - for States or for Cities in DataBase
        if subject_type == "State": subject_type_digit = 1
        else: subject_type_digit = 2

        subject_tax_data = tax_list[subject_type_digit]
        #try:
        # Convert deduction to float
        deduction = float(deduction)
        
        # Split the input string by commas and then create list of tuples of float
        #brackets = [tuple(map(float, brackets_str.split(',')))]
        brackets = []
        for bracket in brackets_str.split(','):
            income_threshold, tax_rate = bracket.split()
            if income_threshold == 'inf':income_threshold = '10e12'
            brackets.append((float(income_threshold), float(tax_rate)))

        # Adding data to proper dictionary of DataBase
        subject_tax_data[subject] = {f'{subject_type}_standard_deduction':deduction, f'{subject_type}_tax_brackets':brackets}
        #print(subject_tax_data[subject])

        with open(r"usa_taxation.txt", "wb") as f:     
                pickle.dump(tax_list[0], f)
                pickle.dump(tax_list[1], f)
                pickle.dump(tax_list[2], f)

        #self.output_text.insert(END, f"Taxational information for {subject} added successfully: {brackets}")
        self.output_text.insert(END, f"Taxational information for {subject_type}: {subject}\n")       
        self.output_text.insert(END, f"Standard deduction in {subject}: {deduction}\n")
        self.output_text.insert(END, f"Tax brackets in {subject}: {brackets}\n")
        self.output_text.insert(END, f"Data for {subject} added successfully")

if __name__ == "__main__":
    
    c = Calculator()
    c.tax_pack_mode()
    #c.add_tax_data()




