import pandas 
import os
import matplotlib.pyplot as plt
import csv


FILE="expense.csv"

    



def logexpense():
   cat=input("Enter the category : ")
   amount=int(input("Enter the amount : "))
   date1=input("Enter date (YYYY-MM-DD): ")
   try:
            file=open(FILE,'r')
            file.close()
   except:
            file=open(FILE,mode='w',newline='')
            writer=csv.writer(file)
            writer.writerow(["category","amount","date"])
            file.close()
   row=[cat,amount,date1]
   file=open(FILE,'a')
   writer=csv.writer(file)
   writer.writerow(row)
   file.close()

def analysedata():
            pd=pandas.read_csv(FILE)
            print(pd.tail(10))
            sum=0
            for i in pd["amount"]:
                  sum=sum+i
            print("total = ",sum)

def visualdata():
        pd=pandas.read_csv(FILE)
   
        show=pd.groupby("category")["amount"].sum()
        show.plot(kind="bar", figsize=(8, 6), title="Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        
        
        show1=pd.groupby("date")["amount"].sum()
        show1.plot(kind="bar", figsize=(8, 6), title="Expenses by date")
        plt.xlabel("date")
        plt.ylabel("Total Amount")
        plt.show()

while True:
    print("enter a choice: \n 1.Log Expenses\n2.Analyse Data\n3.Visualize Data\n4.User friendly navigation")
    choice=int(input("enter a choice"))
    if choice==1:
        logexpense()
    elif choice==2:
        analysedata()
    elif choice==3:
        visualdata()
    #elif choice==4:
    #     usernavigation()
    else:
        break
