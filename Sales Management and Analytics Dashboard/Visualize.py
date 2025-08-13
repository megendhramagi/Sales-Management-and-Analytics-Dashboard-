import pandas as pd
import matplotlib.pyplot as plt
from DataMgt import DataMgt as dm
import Datee as dt

class Visualize:
    dmObj=dm()
    df=pd.DataFrame(dm.getRecord(dmObj))

    def CH_earnByPro(self):
        #total sales by products(totally how much we earned per product )
        earnings_p_prod=self.df.groupby(self.df[2])[5].sum().reset_index() #reset_index helps to put product name in 0 index if not its takes pro name has index val
        print('\n',earnings_p_prod)
        plt.bar(earnings_p_prod.iloc[:,0],earnings_p_prod.iloc[:,1])
        self.add_labels(earnings_p_prod.iloc[:,0],earnings_p_prod.iloc[:,1])
        plt.show()
    
    def CH_earnByDate(self):
        #total sales by date(totally how much we earn per date)
        earnings_p_day=self.df.groupby(self.df[2])[5].sum().reset_index() #reset_index helps to put product name in 0 index if not its takes pro name has index val
        print('\n',earnings_p_day)

        plt.plot(earnings_p_day.iloc[:,0],earnings_p_day.iloc[:,1],marker='s')
        plt.show()
    
    def CH_earnBtwDate(self):
        #sales between dates
        print('\nEnter Start Date ',end=' ')
        is_sDateOk,s_date= dt.getDate()
        print('\nEnter End Date ',end=' ')
        is_eDateOk,e_date= dt.getDate()
        if(is_sDateOk and is_eDateOk):
            date_filtered_df= self.df[(self.df[0]>=s_date) & (self.df[0]<=e_date)]
            earnings_btw_day=date_filtered_df.groupby(date_filtered_df[0])[5].sum().reset_index()
            print(earnings_btw_day)
            xval=[str(x) for x in earnings_btw_day.iloc[:,0]] #the date fromating not showing properly so i changed in str and show in x
            plt.plot(xval,earnings_btw_day.iloc[:,1],marker='o')
            plt.xlabel('Date')
            plt.ylabel('Earnings')
            plt.title('Earnings between Dates')
            plt.show()
    
    def add_labels(self,x,y): #for display y-val text above bars in chart
        for i in range(len(x)):
            plt.text(i,y[i],y[i],ha='center')

    def ch_ProSaleCount(self):
        sale_count = self.df.groupby(self.df[2])[4].sum().reset_index()
        print(sale_count)
        plt.bar(sale_count.iloc[:,0],sale_count.iloc[:,1])
        self.add_labels(sale_count.iloc[:,0],sale_count.iloc[:,1])
        plt.show()


    