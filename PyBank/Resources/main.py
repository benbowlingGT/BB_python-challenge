import os
import csv

#reading our csv file
path_way = os.path.join("..", "Resources", "budget_data.csv")
#print(path_way)

#variables utilized 
months = []
net_list = []
total_months = 0
net_total_amt = 0
monthly_change = 0
monthly_change_list = []
current_row = 0
next_row = 0
net_change = 0
average_change = 0
greatest_increase_date = 0
greatest_increase_amt = 0
greatest_decrease_date = 0
greatest_decrease_amt = 0
 
#open file
with open(path_way) as csvfile:
        
#use csv.reader function to read in csvfile
        csv_reader = csv.DictReader(csvfile, delimiter=",")
        #created loop to find the total amount of months and the net total of the profit/losses column
        for col in csv_reader:
                #Created lists to bring the Date (list called months) and the Profit/Losses (list called net_list) columns from the csvfile into python
                months.append(col['Date'])
                net_list.append(col['Profit/Losses'])
                #Total amount of months listed in column a on csv,
                total_months += 1
                #Net total amount (sum) of profit/losses over entire period (column b on csv) and added int(integer) being that the column consist of numbers 
                net_total_amt = net_total_amt + int(col['Profit/Losses'])
        #print(months)
        #print(net_list)
        #Find the monthly change of profit and losses by creating a loop to cycle through all rows within the 86 months and to take the current row in the net_list minus the next row in the net_list and add that number to a new list called monthly_change_list
        for current_row in range(1,total_months):
                if current_row == 0:
                        monthly_change_list.append(0)
                else:
                        monthly_change_list.append(int(net_list[current_row])-int(net_list[next_row]))
                        next_row += 1
                        #print(monthly_change_list)
        #The average of the changes
        average_change = ((sum(monthly_change_list))/(len(monthly_change_list)))
        #Find greatest increase amt
        greatest_increase_amt = max(monthly_change_list)
        #Find greatest increase date
        greatest_increase_date = max(months)
        #Find greatest decrease amt
        greatest_decrease_amt = min(monthly_change_list)
        #Find greatest decrease date
        greatest_decrease_date = min(months)
        #Print the financial analysis
        financial_analysis = (
                f"Financial Analysis\n"
                f"--------------------------------\n"
                f"Total Months:{total_months}\n"
                f"Total: ${net_total_amt}\n"
                f"Average Change: ${round((average_change),2)}\n"
                f"Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase_amt})\n"
                f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease_amt})\n"
        )
        print(financial_analysis)
        #Export a text file with the results
        export_analysis = ("financial_analysis.txt")
        with open(export_analysis, "w") as textfile:
                textfile.write(financial_analysis)


   

  
   




      


       

