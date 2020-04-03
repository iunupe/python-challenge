    #   ------------------------------ NOTES! ------------------------------ #
    #   Import dependencies: os module & csv module
    #   os - allows you to create file paths across operating systems
    #   csv - for reading in csv files
    #   ---------------------------- CODE BELOW ---------------------------- #
import os
import csv
    
    #   ------------------------------ NOTES! ------------------------------ #
    #   Set path & "join" file         
    #   ---------------------------- CODE BELOW ---------------------------- #
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv') 

    #   ------------------------------ NOTES! ------------------------------ #
    #   Name the output file         
    #   ---------------------------- CODE BELOW ---------------------------- #
#output_file = "pybank_results.txt"

    #   ------------------------------ NOTES! ------------------------------ #
    #   Set variables, empty lists, dictionaries & string/text formatting        
    #   ---------------------------- CODE BELOW ---------------------------- #
dates = []
transactions = []
change = []

    #   ------------------------------ NOTES! ------------------------------ #
    #   Open & automatically close file using "with open" function        
    #   ---------------------------- CODE BELOW ---------------------------- #
with open('/Users/Tito/bootcamp_homework/python-challenge/PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')                      

    #   ------------------------------ NOTES! ------------------------------ #
    #   Use For loop and row counter to iterate through the data      
    #   ---------------------------- CODE BELOW ---------------------------- #
    row = 0
    for i in csvreader:

        if row >=1:
            dates.append(i[0])
            transactions.append(i[1])

        row = row +1
    
    #   ------------------------------ NOTES! ------------------------------ #
    #   Calculate total months, using "len" function      
    #   ---------------------------- CODE BELOW ---------------------------- #   
    months = len(dates)

    #   ------------------------------ NOTES! ------------------------------ #
    #   Calculate Profits/Losses over entire period, using list comprehension      
    #   ---------------------------- CODE BELOW ---------------------------- #   
    transactions = [int(i) for i in transactions]
    totals = sum(transactions)

    #   ------------------------------ NOTES! ------------------------------ #
    #   Calculate Average Change of Profits/Losses over entire period
    #   First, calculate change in value from day-to-day, then use Avg f(x)      
    #   ---------------------------- CODE BELOW ---------------------------- # 
    change = [y-x for x, y in zip(transactions[:-1], transactions[1:])]

    def Average(lst):
        return sum(lst) / len(lst)

    average = Average(change)

    #   ------------------------------ NOTES! ------------------------------ #
    #   Calculate greatest increase/decrease in profits and peg the dates      
    #   ---------------------------- CODE BELOW ---------------------------- #  
    Greatest_Increase = max(change)
    Greatest_Increase_Date = str(dates[change.index(max(change))])

    Greatest_Decrease = min(change)
    Greatest_Decrease_Date = str(dates[change.index(min(change))])

    #   ------------------------------ NOTES! ------------------------------ #
    #   Printing output/results to screen as a preview, using line method
    #   ---------------------------- CODE BELOW ---------------------------- #
line0 = '                   '
line1 = ' Financial Analysis'
line2 = ("-" *30)
line3 = ' Total Months: %d' %(months)
line4 = " Total: $" + str("{:,}".format(totals))
line5 = ' Average Change: ' '${:,.2f}'.format(average)
line6 = ' Greatest Increase in Profits: ' + Greatest_Increase_Date + ' $'+ str("{:,}".format((Greatest_Increase)))
line7 = ' Greatest Decrease in Profits: ' + Greatest_Decrease_Date + ' $'+ str("{:,}".format((Greatest_Decrease)))

output = line0 + '\n' + line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + line7
print(output)

    #   ------------------------------ NOTES! ------------------------------ #
    #   Specify the file to write to (set exit path)
    #   ---------------------------- CODE BELOW ---------------------------- #
pybank_output = os.path.join('/Users/Tito/bootcamp_homework/python-challenge/PyBank/Resources/pybank_results.txt') 


    #   ------------------------------ NOTES! ------------------------------ #
    #   Open the output file using "write" mode
    #   Write out results to text file
    #   ---------------------------- CODE BELOW ---------------------------- #
with open(pybank_output, 'w') as outputfile:
    outputfile.write(output)
