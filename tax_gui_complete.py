from tkinter import *
import tax_calc
import pickle

class Calculator:
    def __init__(self, Any):
        self.Any = Any

    def tax_pack_mode(self):
        root = Tk()
        root.title('US Tax Pack')
        root.geometry('800x400')

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

        # Input fields
        self.salary_label = Label(self.root, text="Enter your gross salary: ")
        self.salary_label.grid(row=0, column=0, sticky=W)
        self.salary_entry = Entry(self.root)
        self.salary_entry.grid(row=0, column=1)

        self.state_label = Label(self.root, text="Enter your state: ")
        self.state_label.grid(row=1, column=0, sticky=W)
        self.state_entry = Entry(self.root)
        self.state_entry.grid(row=1, column=1)

        self.city_label = Label(self.root, text="Enter your city: ")
        self.city_label.grid(row=2, column=0, sticky=W)
        self.city_entry = Entry(self.root)
        self.city_entry.grid(row=2, column=1)

        self.calculate_button = Button(self.root, text="Calculate Tax", command=self.calculate_tax)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

        # Text field for output
        self.output_text = Text(self.root, height=10, width=40)
        self.output_text.grid(row=4, column=0, columnspan=2)

    def show_add_tax_data(self):
        self.root = Toplevel()
        self.root.title('Add Taxational Information')
        self.root.geometry('400x400')

        # Radio buttons for specifying the subject type
        self.subject_type = StringVar()
        Radiobutton(self.root, text="State", variable=self.subject_type, value="State").grid(row=0, column=0, sticky=E)
        Radiobutton(self.root, text="City", variable=self.subject_type, value="City").grid(row=0, column=1, sticky=W)

        # Input fields for adding taxational information
        self.subject_label = Label(self.root, text="Enter the name of the state/city: ")
        self.subject_label.grid(row=1, column=0, sticky=W)
        self.subject_entry = Entry(self.root)
        self.subject_entry.grid(row=1, column=1)

        self.deduction_label = Label(self.root, text="Enter the standard tax deduction: ")
        self.deduction_label.grid(row=2, column=0, sticky=W)
        self.deduction_entry = Entry(self.root)
        self.deduction_entry.grid(row=2, column=1)

        self.brackets_label = Label(self.root, text="Enter the tax brackets (comma-separated): ")
        self.brackets_label.grid(row=3, column=0, sticky=W)
        self.brackets_entry = Entry(self.root)
        self.brackets_entry.grid(row=3, column=1)

        self.add_info_button = Button(self.root, text="Add Taxational Data", command=self.add_tax_data)
        self.add_info_button.grid(row=4, column=0, columnspan=2)

        # Text field for output
        self.output_text = Text(self.root, height=10, width=40)
        self.output_text.grid(row=5, column=0, columnspan=2)


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
        print(tax_list)
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
            brackets.append((float(income_threshold), float(tax_rate)))

        # Adding data to proper dictionary of DataBase
        subject_tax_data[subject] = {f'{subject_type}_standard_deduction':deduction, f'{subject_type}_tax_brackets':brackets}
        print(subject_tax_data[subject])

        with open(r"usa_taxation.txt", "wb") as f:     
                pickle.dump(tax_list[0], f)
                pickle.dump(tax_list[1], f)
                pickle.dump(tax_list[2], f)

        self.output_text.insert(END, f"Taxational information for {subject_type}: {subject}\n")       
        self.output_text.insert(END, f"Standard deduction in {subject}: {deduction}\n")
        self.output_text.insert(END, f"Tax brackets in {subject}: {brackets}\n")
        self.output_text.insert(END, f"Data for {subject} added successfully")
        #self.output_text.insert(END, f"Taxational information for {subject} added successfully: {brackets}")
        

if __name__ == "__main__":
    Any = 10e12
    c = Calculator(Any)
    c.tax_pack_mode()
    c.add_tax_data()


def add_tax_data1(self):
    # Get the selected subject type from the radio buttons
    subject_type = self.subject_type.get()

    # Get other input fields
    subject = self.subject_entry.get()
    deduction = self.deduction_entry.get()
    brackets_str = self.brackets_entry.get()
    
    try:
        # Convert deduction to float
        deduction = float(deduction)
        
        # Split the input string by commas and then create a list of tuples of floats
        #brackets = [tuple(map(float, bracket.split())) for bracket in brackets_str.split(',')]
        
        # Display the type of subject being added in the output text field
        self.output_text.insert(END, f"Adding taxational information for {subject_type}: {subject}\n")

        # Add taxational information to the output text field
        self.output_text.insert(END, f"Taxational information for {subject} added successfully: {brackets}\n")
    except ValueError:
        self.output_text.insert(END, "Error: Invalid input format for tax brackets.\n")


