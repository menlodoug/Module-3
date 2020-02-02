# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate, county options and candidate, county votes.
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest turnout county, largest county percentage, largest county vote
largest_county_name = ""
largest_county_count = 0
largest_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the candidate to
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Get the county name from each row
        county_name = row[1]
        # If the county does not match any existing county, add the county to
        # the county list.
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Determine the final vote count.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n")

    # Print the final vote count to the terminal.
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Print "County votes:" header
    county_votes_header = (
        f"County votes:\n"
    )
    print(county_votes_header,end="")
    txt_file.write(county_votes_header)

    for county in county_votes:
       # Retrieve vote count and percentage.
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print the votes by county to the terminal.
        print(county_results, end="")
        # Save the county results to the text file.
        txt_file.write(county_results)

    for county in county_votes:
       # Retrieve vote counts by county and select the one with largest turnout.
        votes = county_votes[county]
        if (votes > largest_county_count):
            largest_county_count = votes
            largest_county_name = county

    county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_name}\n"
        f"-------------------------\n"
        f"                         \n")
                   
    # Print the largest turnout results to the terminal.
    print(county_summary, end="")
    # Save the largest turnout results to the text file.
    txt_file.write(county_summary)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results, end="")
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
 
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)