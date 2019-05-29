import csv
import pandas as pd
import numpy
import itertools

csvpath = 'data/election_data.csv'
candidates_df = pd.read_csv(csvpath)

# candidates =[]

candidatesCount = candidates_df["Candidate"].value_counts()
# candidatesCount ### print for Jupyter

votes = candidates_df["Voter ID"].count()
# print("total votes: " + format(votes, ",.0f"))

candidates_grp = candidates_df.groupby(["Candidate"]).count()
candidates_grp.columns=["Votes", "County"]
candidates_grp["Pct"] = candidates_grp["Votes"]/votes
columns = ["Votes", "Pct"]
candidates_grp = candidates_grp[columns]
# candidates_grp ### print for Jupyter

winVoteTot = candidates_grp["Votes"].max()
# winVoteTot ### print for Jupyter

print("Election Results")
print("--------------------------------------------------------------")
print("Total Votes: " + format(votes, ",.0f"))
print("--------------------------------------------------------------")
print("The votes and percentages for each candidate are as follows: ")
print(candidates_grp)
print("--------------------------------------------------------------")
print("The wiinner is the one with " + format(winVoteTot, ",.0f") + " votes; and I don't know how to get his name. I think it's an issue with calling the dictionary name after the groupby by I'm stuck")




# with open(csvpath, newline='') as dataFile:
#     csvreader = csv.reader(dataFile, delimiter=',')
    
#     csv_header = next(csvreader)

#     for row in csvreader:
#         try:
#             candidates.index(row[2])
        
#         except ValueError:
#             candidates.append(row[2])


# print("This is the end " + candidates)
