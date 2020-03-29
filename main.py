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
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv') 

                # --------------- What's happening here? --------------- #
                # Set text file output parameters
                # --------------- Code listed below -------------------- #
text_file_path = "output.txt"

                # --------------- What's happening here? --------------- #
                # Set variables, empty lists & text formatting
                # --------------- Code listed below -------------------- #
total_votes = 0
candidates = {}
candidates_percentage = {}
winner = ""
winner_count = 0

                # --------------- What's happening here? --------------- #
                # The "with open" function is not translating in PyPoll
                # --------------- Code listed below -------------------- #

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


                # --------------- What's happening here? --------------- #
                # Thought process is not clicking
                # --------------- Code listed below -------------------- #

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

                # --------------- What's happening here? --------------- #
                # Attempting to work backwards and figure out structure
                # --------------- Code listed below -------------------- #

    firstrow = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] in candidates.keys():
            candidates[row[2]] +=1

        else:
            candidates[row[2]] +=1

    for key, value in candidates.items():
        candidates_percentage[key] = round((value/total_votes)*100,2)

    for key in candidates.keys():
        if candidates[key] > winner_count:
            winner = key
            winner_count = candidates[key]

    print("Election Results")
