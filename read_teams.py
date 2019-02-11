# csv-mgmt/read_teams.py

import csv

csv_file_path = "teams.csv" # a relative filepath

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    for row in reader:
        print(row["city"], row["name"])