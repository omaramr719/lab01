import csv

file_name = input("Enter CSV file name: ")

with open(file_name, "r") as file:
    reader = csv.reader(file)

    rows = list(reader)

    for row in rows[:3]:
        print(row)