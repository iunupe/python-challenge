                # --------------- What's happening here? --------------- #
                # Import os module - allows us to create file paths across
                # operating systems
                # Import csv module for reading csv files
                # --------------- Code listed below -------------------- #
import os
import csv
                # --------------- What's happening here? --------------- #
                # Set path & "join" file         
                # --------------- Code listed below -------------------- #
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv') 

                # --------------- What's happening here? --------------- #
                # Set text file output parameters
                # --------------- Code listed below -------------------- #
text_file_path = "output.txt"

                # --------------- What's happening here? --------------- #
                # Set variables, empty lists & text formatting
                # --------------- Code listed below -------------------- #
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
revenue_average = 0
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

                # --------------- What's happening here? --------------- #
                # Now, we can open the csv file, using "with open"
                # --------------- Code listed below -------------------- #
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')                
                
                # --------------- What's happening here? --------------- #   
                # Read the header row first (skip this step if there is no header)
                # --------------- Code listed below -------------------- #
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
                                                              
                # --------------- What's happening here? --------------- #
                # Loop through column 1 (index=0) to find total months
                # --------------- Code listed below -------------------- #               
    #month_counter = 0
    for row in csvreader:
        #month_counter += 1
        # print(row)
        total_months += 1
    #print(month_counter)                    # Total # of months = 86 
    print(total_months)            

                # --------------- What's happening here? --------------- #
                # Calculate total revenue over entire period
                # --------------- Code listed below -------------------- # 
       # total_revenue = total_revenue + float(row["Profit/Losses"])  
   # print(total_revenue)    

                # --------------- What's happening here? --------------- #
                # Calculate avgerage monthly change in revenue over entire
                # period 
                # --------------- Code listed below -------------------- # 
revenue_change = float(row["Profit/Losses"]) - previous_revenue
previous_revenue = float(row["Profit/Losses"])
revenue_change_list = revenue_change_list + [revenue_change]
month_of_change = [month_of_change] + [row["Date"]]
        




                # --------------- What's happening here? --------------- #
                # Calculate total revenue over entire period
                # --------------- Code listed below -------------------- # 


                # --------------- What's happening here? --------------- #
                # Calculate total revenue over entire period
                # --------------- Code listed below -------------------- # 


                # --------------- What's happening here? --------------- #
                # Calculate total revenue over entire period
                # --------------- Code listed below -------------------- # 





















# greatest_increase = revenue[0]
# greatest_decrease = revenue[0]
# total_revenue = 0

# for garfield in range(len(revenue)):

#     if revenue[garfield] >= greatest_increase:
#        greatest_increase = revenue[garfield]
#        greatest_increase_month = months[garfield]

#     elif revenue[garfield] <= greatest_decrease:
#        greatest_decrease = revenue[garfield]
#        greatest_decrease_month = months[garfield]

#     total_revenue += revenue[garfield]

# print(total_revenue)


