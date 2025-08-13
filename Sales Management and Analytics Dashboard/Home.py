import pandas as pd
import matplotlib.pyplot as plt
from DataMgt import DataMgt as dm
from Visualize import Visualize
import Datee as dt 

class Home:
    
    dmObj=dm()
    viObj=Visualize()

    def __init__(self):
        op1=int(input("\nFor Staff Login 1\nFor Admin Login2\nFor Logout 3\nEnter : "))
        if(op1==1): self.showStaffOp()
        elif(op1==2): self.showAdminOp()
        elif(op1==3):
            dm.closeConn(self.dmObj) #closing db Connection after staff exits
            print('Logout Successful..')
        else:
            print('Invalid Option..')
    
    def showAdminOp(self):
        admin=dm.authAdmin(self.dmObj)
        if(admin): #checking if true admin present intrue else no admin found in the crendential
            print('\nWelcome ',admin[1]) #Printing name
            while(True):
                print("\n1 for total earnings by Products\n2 for total earning by Dates")
                print("3 for earnings between dates\n4 for total product sale count\nAny key to exit..")
                adOp=int(input("\nEnter :  "))
                if(adOp==1):
                    Visualize.CH_earnByPro(self.viObj)
                elif(adOp==2):
                    Visualize.CH_earnByDate(self.viObj)
                elif(adOp==3):
                    Visualize.CH_earnBtwDate(self.viObj)
                elif(adOp==4):
                    Visualize.ch_ProSaleCount(self.viObj)
                else:
                    print('Invalid Option')
                    break
        else:
            print("Invalid credentials")
        self.__init__()
    
    def showStaffOp(self):
        print('Enter Date(YYYY-MM-DD)',end=' ')
        isDate,datee=dt.getDate()
        if(isDate):
            while(True):
                sttOp=int(input('\nEnter 1 for Product Entry, 2 for Exit : \n'))
                if(sttOp==1):
                    proCode=int(input('Enter Product Code : '))
                    proQty=int(input('Enter Product Quantity : '))
                    dm.insertRecord(self.dmObj,datee,proCode,proQty)
                elif(sttOp==2):break
                else:
                    print('Invalid Options')
        else:
            self.showStaffOp()
        self.__init__()

#program starts here
Home()