# Election Analysis

## Overview

The purpose of this challenge was to create a script that could compute the winner of an election along with the county turnout results. The designed script would make calculating the results easier than manually counting.

## Results

- In total, 369,711 votes were cast in the election.

- The votes were count included three counties; Jefferson, Denver, and Arapahoe. Jefferson County had 38,855 votes cast in the election accounting for 10.5% of the total vote. Denver County had 306,055 votes cast which were 82.8% of the vote count. Arapahoe ended with 24,801 ballots cast, totaling 6.7% of the vote.

- Denver County ended with the largest vote total.

- The election was between three candidates; Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. Stockham received 85,213 votes, DeGette received 272,892 votes, and Doane received 11,606 votes.

- Diana DeGette won the election, earning 272,892 ballots totaling 73.8% of the vote.

## Summary

This script can be used in future elections with by only making a couple of changes.
The first necessary change is updating the csv file. Taking this code  file_to_load = os.path.join("Resources", "") and entering the csv file into the empty "" will allow the commission to return the same results for future elections.

The commission could also find the percent turnout for the three counties. Doing this would require the total number of eligible voters in the counties beforehand, but I believe it would be an excellent way to gauge the involvement of the communities.

For this example, let's assume we only have the total eligible voters of all three counties combined. Once we had the required information, finding the percent turnout would only involve adding a few steps to the script.

The first would be creating a new variable called `total_population = #A number`

Then we would create a new varible called `percent_turnout = total_votes / total_population * 100`
Adding this variable to our results would look like the following.
```
election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
	f"Percent Voter Turnout:{percent_turnout:.1f}%\n\n"
        f"County Votes:\n")
    print(election_results, end="")

txt_file.write(election_results)
```
Running this will add the percent turnout to the txt file right underneath the total votes of the election.
