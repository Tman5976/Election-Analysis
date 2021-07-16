# The data we need to retrive
# 1. The total number of votes case
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Open the election results and read the file.
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

election_data = open(file_to_load, 'r')
with open(file_to_load) as electtion_data:

    # perform analysis
    file_reader = csv.reader(election_data)
    # for row in file_reader:
    #     print(row[])

    headers = next(file_reader)
    print(headers)


# with open(file_to_save, "w") as txt_file:

#     # write the county names in file
#     txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

