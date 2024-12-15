# Converts JSON text into CSV formatted output
import json
import csv

def json_to_csv(json_file, csv_file):
    with open(csv_file, 'w', newline=''):
        writer = csv.DictWriter(csv_file, fieldnames=json_file[0].keys())
        writer.writeheader()
        writer.writerows(json_file)