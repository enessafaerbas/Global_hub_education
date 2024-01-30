# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:58:47 2024

@author: Enes Safa
"""


class HealthInsurance:
    def __init__(self, company_name, foundation_year, founder_name, company_slogan, num_of_employees, num_of_clients):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.num_of_employees = num_of_employees
        self.num_of_clients = num_of_clients
        
    def print_report(self):
        print(f"""The Company {self.company_name} was founded in {self.foundation_year}.
              The founder of the company is {self.founder_name}.
              Company slogan: {self.company_slogan}
              Number of employees: {self.num_of_employees}
              Number of clients: {self.num_of_clients}""")
              
    def sup_health_insurance(self, age, chronic_disease, income):
        
        if age >=60 and chronic_disease == True and income < 6000:
            print("we are Sorry! You are not eligible for supplemental health insurance.")
        elif age < 60 and income >=6000 or chronic_disease == False:
            print("Congratulations! you can get supplemental health insurance.")
    
    def update_num_clients(self,new_number):
        self.num_of_clients =new_number
        print(f"Number Of clients has been changet to {self.num_of_clients}")
        
        
#HI_company1= HealthInsurance('Health',2012,'Bob Mayer','we care for you.',3500,13230)

#HI_company1.sup_health_insurance(36,True,6000)

#HI_company1.update_num_clients(13231)

#HI_company1.print_report()





class Logistic:
    
    def __init__(self,company_name, foundation_year, founder_name, company_slogan, inventor_space):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.inventor_space = inventor_space
        
        
    def print_report(self):
       
        print(f"""The Company {self.company_name} was founded in {self.foundation_year}.
              The founder of the company is {self.founder_name}.
              Company slogan: {self.company_slogan}
              Inventory space of the company: {self.inventor_space}""")
              
    
    def update_inventory_space(self, new_storage_space):
        self.inventor_space= new_storage_space /2 
        print(f" Inventory space has been changed to {self.inventor_space}")
        
        
logistic_company1 =Logistic("LogCom",1990,"Laura McCartey","There is no place we Cannot reach",5000)
        
logistic_company1.update_inventory_space(4500)

#logistic_company1.print_report()
        
        
class Trading:
    def __init__(self,company_name, foundation_year, founder_name, company_slogan, sales, expenses, revenue ):
        
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.sales = sales
        self.expenses = expenses
        self.revenue = revenue
        
        
    
    def print_report(self):
        
        print(f"""The Company {self.company_name} was founded in {self.foundation_year}.
              The founder of the company is {self.founder_name}.
              Company slogan: {self.company_slogan}
              Total sales: {self.sales}
              Total expenses: {self.expenses}
              Total revenue : {self.revenue}""")
              
             
    def update_sales_and_expenses(self, new_sales, new_expenses):
        self.sales += new_sales
        self.expenses += new_expenses
        print("Sales and expenses are updated")
        
    def calculate_revenue(self):
        self.revenue = self.sales - self.expenses
        print(f" The revenue of the Company is : {self.revenue}")
        
        
#trading_company1=Trading('TraCom',2005,'Chong Wu','we revolutionize trading',5000,2000,3000)


#trading_company1.update_sales_and_expenses(100,50)

#trading_company1.calculate_revenue()

#trading_company1.print_report()























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    






















