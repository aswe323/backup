import os
import time
import pickle

#creating a new customer object and saving it into a seprate .obj file.
def createCustomer():

    naming = input("name of customer:")

    emailContact = input("email of the customer:")

    phoneNumber = input("mobie phone number:")

    #next contact needs a way to know the current date and compare the dueDate
    dueDate = input("next next time the customer will need our attetion\n ")
    newCustomer = customer(naming,emailContact,phoneNumber,dueDate)
    saveThis = input("""would you like to save the customer with the folowing details?
                        %s
                        email:%s
                        phone number:%s
                        next contact date %s
                        type y to save or n to discard, then ENTER: \n""" % (naming , emailContact, phoneNumber, dueDate ))
    if saveThis == "y":

            #setting path to current working directory
            customerFile = os.getcwd() + "Customers.obj"

            #creating a variable that access the file in write mod
            writingCustmer = open(customerFile,"wb")

            #saving the customer details to the .obj file
            pickle.dump(newCustomer, writingCustmer)
            
    elif saveThis == "n":
            print("discarded")         
            return
    else:
            print("invaid input. discarding")
            return


#retriving and object and showing its contests in a readble format.
def showCustomer():
    #TODO

 return


#customer class takes the customer details and logs the date of creation of the object. an empty log exists in the form of a lists veriable with no enterys
class customer:
    "customer details and contact information, contact log"
    def __init__(self,name, email, phone, nextContact):

        #custmmer name and last name
        self.name = name

        #customer email of contact
        self.email = email

        #customer mobile phone number
        self.phone = phone
        
        #next date contact this customer
        self.nextContact = nextContact

        self.log = []
    #date of submission of the customer to the system
    logDate = time.asctime(time.localtime(time.time()))



    
