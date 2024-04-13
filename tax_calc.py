import pickle

class TaxCalculator:
    def gross_salary(self):
        gross_salary = input('Enter your gross salary, $ a year ')
        return gross_salary
    
    def state(self):
        state = input('Enter the state name ')
        return state
    
    def city(self):
        city = input('Enter the city in the state ')
        return city

    def usa_taxation_stats(self):
        with open(r'usa_taxation.txt', 'rb') as f:
            federal_taxation = pickle.load(f)
            states_taxation = pickle.load(f)
            cities_taxation = pickle.load(f)
        return federal_taxation, states_taxation, cities_taxation

    def calculate_tax(self, salary, brackets, standard_deduction):
        gross_salary_deducted = salary - standard_deduction
        tax_payments = 0
        for i, bracket in enumerate(brackets):
            if i == 0 or gross_salary_deducted > bracket[0]:
                tax_payments += (min(gross_salary_deducted, bracket[0]) - (brackets[i-1][0] if i > 0 else 0)) * bracket[1]
            else:
                break
        return tax_payments

    def federal_tax_calculation(self, salary):
        federal_taxation = self.usa_taxation_stats()[0]
        return self.calculate_tax(salary, federal_taxation['Federal_tax_brackets'], federal_taxation['Federal_standard_deduction'])

    def fica(self, salary):
        federal_taxation = self.usa_taxation_stats()[0]
        return federal_taxation['FICA'] * salary

    def state_tax_calculation(self, salary, state):
        states_taxation = self.usa_taxation_stats()[1]
        return self.calculate_tax(salary, states_taxation[state]['State_tax_brackets'], states_taxation[state]['State_standard_deduction'])

    def city_tax_calculation(self, salary, city):
        cities_taxation = self.usa_taxation_stats()[2]
        return self.calculate_tax(salary, cities_taxation[city]['City_tax_brackets'], cities_taxation[city]['City_standard_deduction'])

    # ... (rest of the methods, refactored similarly)

    def tax_output(self, salary, state, city, fica, federal_tax_payments, state_tax_payments, city_tax_payments):
        print(f'Gross_salary = {salary:.1f}')
        print(f'Fica = {fica:.1f}')
        print(f'federal_tax_payments = {federal_tax_payments:.1f}')
        print('State = ', state)
        print(f'state_tax_payments = {state_tax_payments:.1f}')
        print('City = ', city)
        print(f'city_tax_payments = {city_tax_payments:.1f}')
        total_tax_payments = fica + federal_tax_payments + state_tax_payments + city_tax_payments
        net_salary = salary - total_tax_payments
        print(f'total_tax_payments = {total_tax_payments:.1f}')
        print(f'net_salary = {net_salary:.1f}')

# ... (rest of the code to instantiate and use the TaxCalculator)
    def main(self, salary, state, city):        
        fica = self.fica(salary)
        federal_tax_payments = self.federal_tax_calculation(salary)
        state_tax_payments = self.state_tax_calculation(salary, state)
        city_tax_payments = self.city_tax_calculation(salary, city)

        output = f"Gross_salary = {salary:.1f}\n"
        output += f'Fica = {fica:.1f}\n'
        output += f'federal_tax_payments = {federal_tax_payments:.1f}\n'
        output += f'State = {state}\n'
        output += f'state_tax_payments = {state_tax_payments:.1f}\n'
        output += f'City = {city}\n'
        output += f'city_tax_payments = {city_tax_payments:.1f}\n'

        total_tax_payments = fica + federal_tax_payments + state_tax_payments + city_tax_payments
        net_salary = salary - total_tax_payments
        output += f'total_tax_payments = {total_tax_payments:.1f}\n'
        output += f'net_salary = {net_salary:.1f}'

        return output


   







                    

                                  