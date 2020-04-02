    #   ------------------------------ NOTES! ------------------------------ #
    #   Import dependencies: os module & csv module
    #   os - allows you to create file paths across operating systems
    #   csv - for reading csv files
    #   ---------------------------- CODE BELOW ---------------------------- #
import os
import csv
    #   ------------------------------ NOTES! ------------------------------ #
    #   Set path & "join" file         
    #   ---------------------------- CODE BELOW ---------------------------- #
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv') 

    #   ------------------------------ NOTES! ------------------------------ #
    #   Set text file output parameters
    #   ---------------------------- CODE BELOW ---------------------------- #
#text_file_path = "output.txt"

    #   ------------------------------ NOTES! ------------------------------ #
    #   Set variables, empty lists, dictionaries & string/text formatting
    #   ---------------------------- CODE BELOW ---------------------------- #
total_votes = 0
candidates = {}
candidates_percentage = {}
winner = ""
winner_count = 0

    #   ------------------------------ NOTES! ------------------------------ #
    #   Open file using "read" mode; Specify variable to hold contents
    #
    #   Note: "print(cvsreader)" ONLY prints out an object to read the csv
    #   file line-by-line. It doesn't actually take any action. It essentially
    #   prints out the location where the infomation is stored and is not
    #   useful for viewing purposes
    #   ---------------------------- CODE BELOW ---------------------------- #
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print("-" * 30)
    #print(csvreader)
    #print("-" * 30)

    #   ------------------------------ NOTES! ------------------------------ #
    #   Reading header row first and printing to screen
    #   ---------------------------- CODE BELOW ---------------------------- #
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    print("")

    #   ------------------------------ NOTES! ------------------------------ #
    #   Loop through each row of data after the header
    #   ---------------------------- CODE BELOW ---------------------------- #
    for row in csvreader:
        name = row[2]
        total_votes += 1
      
        if name in candidates.keys():
            candidates[name] +=1
        else:
            candidates[name] = 1

    #   ------------------------------ NOTES! ------------------------------ #
    #   {candidates} is the dictionary...missing step is adding name to
    #   candidate keys, since there should be a [key] and a [value]
    #
    #   Google how to add a key to the existing dictionary called "candidates"
    #   Note: you can increment a key, but not a string
    #   ---------------------------- CODE BELOW ---------------------------- #
for key, value in candidates.items():
    candidates_percentage[key] = round((value/total_votes)*100,2)
#print(candidates_percentage)

    #   ------------------------------ NOTES! ------------------------------ #
    #   Loop through candidate list to establish a winner by total vote count
    #   ---------------------------- CODE BELOW ---------------------------- #
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

    #   ------------------------------ NOTES! ------------------------------ #
    #   Printing output/results to screen as a preview
    #   ---------------------------- CODE BELOW ---------------------------- #
print("Election Results")
print("-" * 30)
print("Total Votes: " + str("{:,}".format(total_votes)))
print("-" * 30)

for key, value in candidates.items():
    print(key + ": " + str(candidates_percentage[key]) + "% (" + str("{:,}".format(value) + ")"))
print("-" * 30)       
    #print(candidates)
    #print("")
print("Winner: " + winner)
print("-" * 30)       
    #print(candidates.keys())
    #print("")

    #   ------------------------------ NOTES! ------------------------------ #
    #   Specify the file to write to (set exit path)
    #   ---------------------------- CODE BELOW ---------------------------- #
pypoll_output = os.path.join('PyPoll', 'Resources', 'election_results.txt') 

    #   ------------------------------ NOTES! ------------------------------ #
    #   Open the output file using "write" mode
    #   Specify the variable to hold the contents
    #   Write out results to text file
    #   ---------------------------- CODE BELOW ---------------------------- #
with open(pypoll_output, "w") as txtfile:

    #   ------------------------------ NOTES! ------------------------------ #
    #   Write data to new file
    #   ---------------------------- CODE BELOW ---------------------------- #
    txtfile.write("\n")
    txtfile.write("Election Results" + '\n')
    txtfile.write(("-" * 30) + '\n')
    txtfile.write("Total Votes: " + str("{:,}".format(total_votes)) + '\n')
    txtfile.write(("-" * 30) + '\n')
    for key, value in candidates.items():
        txtfile.write(key + ": " + str(candidates_percentage[key]) + "% (" + str("{:,}".format(value) + ")") + '\n')
    txtfile.write(("-" * 30) + '\n')
    txtfile.write("Winner: " + winner + '\n')
    txtfile.write(("-" * 30) + '\n')
