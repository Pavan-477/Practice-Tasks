#====================Assignment 6.1==================

#---------------------Question 1----------------------

#-----------Approach 1---------------------------
import json

emps={'emp1':['Pavan','03/11/2000','6ft','Vijayawada','Andhra Pradesh'],
      'emp2':['Ramya','23/11/2000','5.9ft','Vijayawada','Andhra Pradesh'],
      'emp3':['Pravin','13/11/2000','5.5ft','Nalgonda','Telangana'],
      'emp4':['Pushpa','03/01/2000','5ft','Vijayawada','Andhra Pradesh'],
      'emp5':['Keshava','02/10/2000','6ft','Chittoor','Andhra Pradesh']
      }
with open('employee.json','w') as f:
    json.dump(emps,f)                                #Written into a JSON file

with open('employee.json','r') as f:
    y=json.load(f)                                  #Reading from a JSON file

print("Data read from the JSON file is : \n")
print(y,'\n')

class Employee:
    def __init__(self,e):
        self.e=list(e)
        self.e1=self.e[0]
        self.e2=self.e[1]
        self.e3=self.e[2]
        self.e4=self.e[3]
        self.e5=self.e[4]    

        

        
    def display(self):
        print("Data displayed thru Employee class is : \n")
        print(self.e1,'\n',self.e2,'\n',self.e3,'\n',self.e4,'\n',self.e5)




p=y.values()
emp_obj=Employee(p)
emp_obj.display()

#--------------Approach 2-----------------------

import json

emps={'emp1':['Pavan','03/11/2000','6ft','Vijayawada','Andhra Pradesh'],
      'emp2':['Ramya','23/11/2000','5.9ft','Vijayawada','Andhra Pradesh'],
      'emp3':['Pravin','13/11/2000','5.5ft','Nalgonda','Telangana'],
      'emp4':['Pushpa','03/01/2000','5ft','Vijayawada','Andhra Pradesh'],
      'emp5':['Keshava','02/10/2000','6ft','Chittoor','Andhra Pradesh']
      }
with open('employee.json','w') as f:
    json.dump(emps,f)                                #Written into a JSON file

with open('employee.json','r') as f:
    y=json.load(f)                                  #Reading from a JSON file

print(y)

class Employee:
    def __init__(self,e):

        self.e=e
        
    def display(self):
        
        print(self.e)


for i in y.values():
    emp_obj=Employee(i)                       #Creating an object and display every single employee thru iteration
    emp_obj.display()




#---------------------Question 2----------------------


st_caps={'Andhra Pradesh':'Vijayawada','Telangana':'Hyderabad','Karnataka':'Bengaluru',
'Tamil Nadu':'Chennai','Maharashtra':'Mumbai','Rajasthan':'Jaipur','Gujarat':'Ahmedabad'}

with open('state_capitals.json','w')as f:
    json.dump(st_caps,f)
    print('Writing the dict object into JSON file complete\n')

with open('state_capitals.json','r')as f:
    x=json.load(f)
    print('Reading content from the json file\n')
    print(x)
    print('\nReading content from the json file complete')