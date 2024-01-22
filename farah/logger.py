import os
import csv


log_dir = "log"
header_row = ["date", "product_id", "type", "attr", "from", "to"]


def create_log_file(filename):
    # make sure the directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if not os.path.exists(filename):
        # Create the file and write the header row
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header_row)


def log_product_changes(log):
    log_file = os.path.join(log_dir, f"{log['date']}.csv")
    create_log_file(log_file)

    rows = []
    for change in log['log']:
        rows.append([log['date'], log['product'], "change", change['attr'], change['from'], change['to']])

    # Append new rows to the CSV file
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print[rows]
