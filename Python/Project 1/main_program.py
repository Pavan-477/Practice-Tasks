import re,json 
#-------------------------------ADMIN FUNCTIONALITIES----------------------------------

class Restaurent:

        def __init__(self):
                self.f_items={1:{'Name':'Tandoori Chicken','Quantity':'4piece','Price':240,'Discount': 10,'stock':400},
                2:{'Name':'Vegan Burger','Quantity':'1piece','Price':320,'Discount': 10,'stock':100},
                3:{'Name':'Truffle Cake','Quantity':'500gms','Price':900,'Discount': 10,'stock':50}}
                with open('Menu.json','w') as f:
                        json.dump(self.f_items,f)  
                self.users_list={1:{'name': 'Demo User 1', 'phno': '9885712345', 'mail': 'abc@gmail.com','adrss': 'VJA', 'password': '12312'},
                2:{'name': 'Demo User 2', 'phno': '9517534682', 'mail': 'xyz@gmail.com','adrss': 'HYD', 'password': '1212'}}
                with open('Users.json','w') as f:
                    json.dump(self.users_list,f)
                self.order_hist={}           #Stores all the previous orders
                self.order_tester={}         # Stores the details of the current order
                self.grand_total=0           #stores grand total of an order
                self.gt={}                   # Stores grand totals of all previous orders
                self.admin={'phno':7588926677,'password':'123456'} 
        #Only one admin credentials are initialised and functionality to add more admins/edit existing credentials of admin is restricted
                with open('Admin.json','w') as f:
                        json.dump(self.admin,f)

        def Menu(self):
                print("||============================ MENU ============================||\n")
                print('-'*65)
                print('| FOOD ID       ITEM               QUANTITY      PRICE(INR)      |')
                print('-'*65)
                for i,j in self.f_items.items():
                        if len(j['Name'])<20:
                            p=20-len(j['Name'])
                            q=" "*p
                            adj=j['Name']+q
                        else :
                            adj=j['Name']
                        print('|  ',i,'   ',adj,'---> ',j['Quantity'],' ---> ',j['Price'])
                print('='*31,'X','='*31)
        
        def add_food(self):
                new_food={}
                new_food['Name'] =input("Enter Food item you want to Add : \n")
                new_food['Quantity'] =input("Enter its quantity (for eg:- 4pieces/250gm/100ml) \n")
                new_food['Price'] =int(input("Enter Food's selling price in INR : \n"))
                new_food['Discount']=int(input('Enter discount you want to give on this item : \n'))
                new_food['stock']=int(input('Enter stock of this item you want to maintain  : \n'))
                try:
                        choice=int(input("Are you sure you want to add this new item ? ,\nPress 1 to confirm.\nPress any other number to cancel this new item entry \n "))
                except ValueError:
                        print('Invalid Entry , Item addition cancelled!!')
                else:
                        if choice==1:
                                
                                self.f_items[len(self.f_items)+1]=new_food
                                print("Item added successfully")
                                print("New menu is \n")
                                with open('Menu.json','w') as f:
                                    json.dump(self.f_items,f)  
                                self.Menu()
                        else :
                                print('Insertion of New item is cancelled ')
                                new_food.clear()
                
                        
        def edit_food(self):
                self.Menu()
                ed_id=int(input("Enter FoodID whose details you want to edit")) #To be edited food ID
                if ed_id in self.f_items:
                       pass
                else:
                       print("Enter a valid number from the given options :/")
                       return ''
                print("Existing details of that item : \n",self.f_items[ed_id])
                print("Enter 1 to edit food item name\nEnter 2 to edit food quantity\nEnter 3 to edit price")
                print("Enter 4 to edit discount on this item \nEnter 5 to edit the stock")
                try:
                    choice=int(input("Enter your choice : \n"))
                except :
                        print("Invalid input, please enter again among integers(1-5)\n")
                else:
                        if choice==1:
                                self.f_items[ed_id]['Name']=input("Enter New food name")
                        elif choice==2:
                                self.f_items[ed_id]['Quantity'] =input("Enter its quantity (for eg:- 4pieces/250gm/100ml) \n")
                        elif choice==3:
                                self.f_items[ed_id]['Price'] =input("Enter Food's selling price \n")
                        elif choice==4:
                                self.f_items[ed_id]['Discount'] =input("Enter Discount on this item \n")
                        elif choice==5:
                                self.f_items[ed_id]['Stock'] =input("Enter stock you want to maintain for this item \n")
                        
                        with open('Menu.json','w') as f:
                                json.dump(self.f_items,f)  
                        print("Updated menu is \n")
                        self.Menu()

        def delete_food(self):
            self.Menu()
            try:
                    ed_id=int(input("Enter FoodID whose details you want to delete \n"))  #edited food ID
                    if ed_id in self.f_items.keys():
                        print("Existing details of that item : \n",self.f_items[ed_id])
                    else:
                        print("Food ID:",ed_id,"does not exist ,choose from the available food ID's")

            except ValueError:
                    print("Invalid input, please enter only integers \n")
            else:
                    try:
                        choice=int(input("Are you sure you want to delete this new item ?\nPress 1 to confirm.\nPress any other number to cancel this new item entry\n "))
                    except ValueError:
                        print('Invalid Entry , Item deletion cancelled!!')
                    else:
                        if choice==1:
                                del self.f_items[ed_id]
                                print("Item deleted successfully")
                                print("New menu is \n")
                                with open('Menu.json','w') as f:
                                    json.dump(self.f_items,f)  
                                self.Menu()
                        else :
                                print('Deletion of food item is cancelled ')
                                return ''

        #----------------------------------USER FUNCTIONALITIES----------------------------------

        def user_reg(self):
                users={}                                #To add new users
                users['name']=input('Enter full name : ')
                phno=input('Enter your mobile number : ')
                m=re.fullmatch('[6-9][0-9]{9}',phno)
                if m!=None:
                        users['phno']=phno
                else:
                        print('Please enter a valid number')
                        print('User registration failed,Try again!!')
                        users.clear()
                        return 'failed'
                mail=input('Enter mail id :')
                m=re.search('@[a-z]*.com$',mail)
                if m!=None:
                        
                        users['mail']=mail
                else:
                        print('invalid mail id')
                        print('User registration failed,Try again!!')
                        users.clear()
                        return 'failed'
                
                users['adrss']=input('Enter address : ')
                users['password']=input('Enter password : ')
                print('User Registered successfully')
                for i,j in users.items():
                    print(i,':-',j)
                self.users_list[len(self.users_list)+1]=users       #Adding new user to our existing user data
                with open('Users.json','w') as f:
                    json.dump(self.users_list,f)

        
        def login(self):#This method returns if the person is user or admin so store this stuff in a variable
                print("\nHello, Welcome :")
                print("Enter 1 if you are a new user\nEnter 2 if you are an existing user\nEnter 3 if you are an admin\n")
                try:
                    choice=int(input("Enter your choice : "))
                except ValueError:
                    print('Invalid Entry ,Choose from the given options!!')
                    print()
                    self.login()
                else:
                    if choice==1:
                            val=self.user_reg()
                            if val!='failed':
                                print('Login successfull')
                                print()
                                return 'user'
                            else:
                                   self.login()

                    elif choice == 2:
                            num=input("Enter your mobile number : ")                
                            paswd=input("Enter your password : ")
                            counter=0
                            length=len(self.users_list)
                            for i in self.users_list:
                                    counter+=1
                                    if num == self.users_list[i]['phno']:                        #Validating Phone Number if it exists
                                            if paswd == self.users_list[i]['password']:          #Validating Password given that the Phone number already exists
                                                    print("User login successful")
                                                    print()
                                                    return 'user'

                                    else:
                                        if counter!=length:
                                            pass
                                        else:
                                            print("INVALID CREDENTIALS ! !")
                                            print()               

                    elif choice==3:
                            num=int(input("Enter your mobile number : "))
                            paswd=input("Enter your password : ")
                            if (num==self.admin['phno']) and (paswd==self.admin['password']):
                                    print('Admin login successful')
                                    print()
                                    return 'admin'
                            else :
                                print('INVALID CREDENTIALS ! ! !')
                                self.login()
                    else :
                        print('Invalid entry ,Try again ')
                        self.login()

        def order_placer(self):
                self.Menu()
                order_summary={}        #Stores the details of an Food item (item by item) in the current order
                print('Select items using their FoodID')
                try:
                    choice=int(input())
                except ValueError:
                    print("Invalid input,enter only integers")
                    return ''
                if choice not in self.f_items:
                    print("Invalid entry choose from the available options")
                    return ''
        
                if choice in self.f_items:
                    print(self.f_items[choice]['Name'],'---->',self.f_items[choice]['Quantity'],'---->',self.f_items[choice]['Price'])
                    print('You will get a discount of',self.f_items[choice]['Discount'],'% on this item')
                    price=self.f_items[choice]['Price']-(self.f_items[choice]['Price']*(self.f_items[choice]['Discount']/100))
                    qty=int(input("Enter how many units of this item you want : "))
                    price*=qty
                    self.grand_total+=price
                    order_summary['Name']=self.f_items[choice]['Name']
                    order_summary['Quantity']=qty
                    order_summary['Price']=price
                    self.order_tester[len(self.order_tester)+1]=order_summary
                    print()
                    print("Current items on cart :")
                    for i,j in self.order_tester.items():                    #Displaying Current items on cart
                            print(i,end='--')
                            for k,m in j.items():
                                print(m,end='  ')
                            print()

                    print("Grand total --------",self.grand_total)
                    print()
                    self.f_items[choice]['stock']-=qty               #Updating stock
                    if self.f_items[choice]['stock']<1:
                            print(self.f_items[choice]['Name']," is in low Stock ,This item delivery is not guaranteed,")
                            print("Still we are keeping this in your cart for you and will try our best to deliver it to to you :)")
                    subc=int(input("Enter 1 to add more items \nEnter 2 to proceed with the current items\n"))          #Subjective_choice  
                    print()
                    if subc==1:
                            self.order_placer()
                    elif subc==2:
                            print("Alright heading towards placing the order")
                            conf=input('Are you sure you want to place the order ?\nPress 1 to confirm\nPress 2 to Exit\n')
                            if conf=='1':
                                    self.gt[len(self.gt)+1]=self.grand_total
                                    self.order_tester[len(self.order_tester)]=order_summary
                                    self.order_hist[len(self.order_hist)+1]=self.order_tester
                                    self.order_tester={}
                                    self.grand_total=0
                                    print("Order placed successfully , Enjoy the food !!!!")
                                    print('Order will be delivered to your address ')
                        
                            else:
                                    print("ORDER CANCELLED")
                    else:
                           print('Invalid input ,Order cancelled')

                else:
                    print("Something went wrong please try again")

        def Order_History(self):

                if len(self.order_hist)==0:
                       print('No orders made yet!')
                       return ''
                else:       
                        print("ORDER HISTORY ")
                        print('-'*40)
                        count=0
                        for i,j in self.order_hist.items():
                                print('Order ',i)
                                for k,m in j.items():                    
                                        print(k,'  ',list(m.values()))
                                        count+=1
                                print('Grand total for this order',self.gt[i])
                                print()
                        print()
                        print('-'*40)

        def profile_updater(self):
            
                num=input("Enter your mobile number : ")
                paswd=input("Enter your password : ")        
                counter=0
                key=0
                length=len(self.users_list)
                for i in self.users_list:
                        counter+=1
                        if num in self.users_list[i]['phno']:
                                
                                if paswd in self.users_list[i]['password']:
                                    print("User login successful")
                                    key=i
                                    for i,j in self.users_list[key].items():
                                        print(i,'--',j)                         
                                print()
                                break
                        else:
                                if counter!=length:
                                        pass
                                else:
                                    print("INVALID CREDENTIALS ! !")
                                    print()

                print('What do you want to edit in your profile Details')
                print('Enter 1 for editing name\nEnter 2 for editing number')
                print('Enter 3 for editing mail\nEnter 4 for editing address')
                print('Enter 5 for editing password')
                try:
                    choice=int(input())
                except ValueError:
                    print('Invalid Entry ,\nEnter only numbers\nChoose from the given options!!')
                    print()
                else:
                    if choice==1:
                            self.users_list[key]['name']=input('Enter full name : ')
                    elif choice==2:
                            phno=input('Enter your mobile number :')
                            m=re.fullmatch('[6-9][0-9]{9}',phno)
                            if m!=None:
                                    self.users_list[key]=phno
                            else:
                                    print('Please enter a valid number')
                                    print('User registration failed,Try again!!')
                                    self.profile_updater()

                    elif choice==3:
                                    mail=input('Enter mail id :')
                                    m=re.search('@[a-z]*.com$',mail)
                                    if m!=None:
                                            self.users_list[key]['phno']=mail
                                    else:
                                            print('invalid mail id')
                                            print('User registration failed,Try again!!')
                                            self.profile_updater()

                    elif choice==4:            
                                    self.users_list[key]['adrss']=input('Enter address : ')

                    elif choice==5:    
                                    self.users_list[key]['password']=input('Enter password : ')
                    else:
                            print('Kindly enter from the given choices')
                            return ''

                    print('Profile edited successfully')
                    print('-'*50)
                    for i,j in self.users_list[key].items():
                            print(i,':-',j)
                    print('-'*50)
                    with open('Users.json','w') as f:
                            json.dump(self.users_list,f)
                        
print('*'*60)
print("Welcome to Foodie Bytes")
print('Kindly login to make use of take full advantage of our services')
person=Restaurent()

if __name__ == '__main__':
    p=person.login()

while True:
        
        if p=='user':
                
                try:
                      print('\nEnter 1 for placing a new order\nEnter 2 for checking order history\nEnter 3 for updating profile')
                      print('Enter 4 for Quitting the app')
                      opt=int(input())

                except ValueError:
                      print("Something went wrong please enter only integers(1-4)\n")
                else:
                        if opt==1:
                                person.order_placer()
                        elif opt==2:
                                person.Order_History()
                        elif opt==3:
                                person.profile_updater()
                        elif opt==4:
                                quit()
                        else:
                              print('Choose and Enter only from the given options\n')
                

        elif p=='admin':
                try:
                        print('\nEnter 1 for adding an item to the menu\nEnter 2 for editing menu')
                        print('Enter 3 for viewing menu')
                        print('Enter 5 for deleting an item from menu\nEnter 6 for Quitting the app')
                        opt=int(input())
                except ValueError:
                      print("Something went wrong please enter only integers(1-5)\n")

                else:
                        if opt==1:
                                person.Menu()
                                person.add_food()
                        elif opt==2:
                                person.edit_food()
                        elif opt==3:
                                person.Menu()
                        elif opt==4:
                                person.delete_food()       
                        elif opt==5:
                                quit()
                        else:
                              print('Choose and Enter only from the given options\n')
        else:
               print('Something went wrong Re-run the program')
               p=person.login()