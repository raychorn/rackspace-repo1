'''

Question 3 of 6


 
 Settings  Help 
 


Employee
Constructor:
accepts First Name, Last Name, Pay Rate, Yearly Vacation (num days)
Public Methods:
get_name - returns the employee’s name in the format “Last Name, First Name"
get_pay_rate - returns hourly pay rate
get_yearly_vacation - returns the amount of yearly vacation for the employee

Contractor
Constructor:
accepts First Name, Last Name, Pay Rate, Agency Name (Note: By policy, all contractors have 0 days of vacation)
Public Methods:
get_name - returns the contractor's name in the format “Last Name, First Name [ C ]"
get_pay_rate - returns hourly pay rate
get_yearly_vacation - returns the amount of yearly vacation for the contractor
get_agency - returns the name of the contracting agency that represents the contractor

Temporary
Constructor:
accepts First Name, Last Name, Pay Rate, Agency Name (Note: By policy, all temporaries have 0 days of vacation)
Public Methods:
get_name - returns the contractor's name in the format “Last Name, First Name [ T ]"
get_pay_rate - returns hourly pay rate
get_yearly_vacation - returns the amount of yearly vacation for the temporary
get_agency - returns the name of the temp agency that represents the temporary
Output: 
A class heirarchy

'''

class Employee():
    def __init__(self, first_name, last_name, pay_rate, vacation_days):
        '''
        First Name, Last Name, Pay Rate, Yearly Vacation (num days)
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.pay_rate = pay_rate
        self.vacation_days = vacation_days
    
    def get_name(self):
        return self.last_name+', '+self.first_name
    
    def get_pay_rate(self):
        return self.pay_rate
    
    def get_yearly_vacation(self):
        return self.vacation_days
    
class Contractor(Employee):
    def __init__(self, first_name, last_name, pay_rate, agency_name, vacation_days=0):
        '''
        accepts First Name, Last Name, Pay Rate, Agency Name (Note: By policy, all contractors have 0 days of vacation)
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.pay_rate = pay_rate
        self.vacation_days = vacation_days
        self.agency_name = agency_name
        
    def get_agency(self):
        return self.agency_name
    
class Temporary(Contractor):
    def __init__(self, first_name, last_name, pay_rate, agency_name, vacation_days=0):
        '''
        accepts First Name, Last Name, Pay Rate, Agency Name (Note: By policy, all temporaries have 0 days of vacation)
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.pay_rate = pay_rate
        self.vacation_days = vacation_days
        self.agency_name = agency_name

if (__name__ == '__main__'):
    e = Employee('first_name1', 'last_name1', 10.00, 100)
    print e.get_name()
    print e.get_pay_rate()
    print e.get_yearly_vacation()
    print
    
    c = Contractor('first_name2', 'last_name2', 11.00, 'agency2')
    print c.get_name()
    print c.get_pay_rate()
    print c.get_yearly_vacation()
    print c.get_agency()
    print
    
    t = Temporary('first_name3', 'last_name3', 12.00, 'agency3')
    print t.get_name()
    print t.get_pay_rate()
    print t.get_yearly_vacation()
    print t.get_agency()
    print
    